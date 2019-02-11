import numpy as np

LICS = 15

def decide(
        numpoints,
        points,
        parameters,
        lcm,
        puv
):

    # Launch Interception Conditions
    # The results are stored in the Conditions Met Vector, where every element corresponds to a LIC.
    launch_interception_conditions = LaunchInterceptionConditions(points,parameters)
    conditions_met_vector = np.full(LICS, False)
    conditions_met_vector[0] = launch_interception_conditions.check_lic0()
    conditions_met_vector[4] = launch_interception_conditions.check_lic4()

    # Populate the Preliminary Unlocking Matrix
    # The Logical Connector Matrix explains how pairs of LIC's should be combined into a boolena value.
    # The LCM and the CMV decide the boolean values in the Preliminary Unlocking Matrix.
    # A 1 (ANDD) at position [i,j] in the LCM means that PUM[i,j] should be set to (LICi AND LICj)
    # A 2 (ORR)at -"- should be set to (LICi OR LICj)
    # A 3 (NOTUSED) at -"- should be set to True
    pum = np.full((LICS,LICS), False)

    for row in range(LICS):
        for col in range(LICS):
            if lcm[row,col] == 1:
                pum[row,col] = conditions_met_vector[row] and conditions_met_vector[col]
            elif lcm[row,col] == 2:
                pum[row,col] = conditions_met_vector[row] or conditions_met_vector[col]
            else:
                pum[row,col] = True

    # Populate the Final Unlocking Vector
    # The FUV is set depending on the PUM and the Preliminary Unlocking Vector
    # If PUV[i] is set to true, then LICi should be used when determining whether a launch should be performed.
    # If LICi is to be used, then FUV[i] is set to true if the ith row of PUM only consists of true entries.
    # If FUV[i] is set to false, then LICi shall not be used to suppress a launch, and the value of FUV[i] is true.
    fuv = np.full(LICS, False)
    for row in range(LICS):
        if puv[row]:
            # This LIC shall be used, so loop through the corresponding row of PUM and check whether all values are true
            r = True
            for col in range(LICS):
                r &= pum[row,col]
            fuv[row] = r
        else:
            fuv[row] = True

    # Calculating the final launch decision by checking whether all elements in the FUV are true
    result = True
    for final_unlocking_element in fuv:
        result &= final_unlocking_element

    return result

def point_distance(point1,point2):

    # Calculate the euclidean distance between two points
    return ( (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2 )**0.5

def number_of_quadrants(quadrants):
    # Calculate the number of different quadrants in the input array
    one = 0
    two = 0
    three = 0
    four = 0
    for quadrant in quadrants:
        if quadrant == 1:
            one = 1
        elif quadrant == 2:
            two = 1
        elif quadrant == 3:
            three = 1
        elif quadrant == 4:
            four = 1

    return one + two + three + four

def quadrant(point):
    # Determines which quadrant a point lies in. If it belongs to several, lower numbered quadrants have priority.

    quadrant = 0

    if point[0] >= 0.0 and point[1] <= 0.0:
        # Lower right, i.e. IV
        quadrant = 4

    if point[0] <= 0.0 and point[1] <= 0.0:
        # Lower left, i.e. III
        quadrant = 3

    if point[0] <= 0.0 and point[1] >= 0.0:
        # Upper left, i.e. II
        quadrant = 2

    if point[0] >= 0.0 and point[1] >= 0.0:
        # Upper right, i.e. I
        quadrant = 1

    return quadrant

class LaunchInterceptionConditions:

    def __init__(self, points, parameters):
        self.points = points
        self.parameters = parameters

    def check_lic0(self):

        # Launch Interception Conditions 0
        # If two consecutive points are further apart than length1, then LIC0 is true.
        result = False
        for i in range(len(self.points)-1):
            if point_distance(self.points[i],self.points[i+1]) > self.parameters['length1']:
                result = True

        return result

    def check_lic4(self):
        # Launch Interception Condition 4
        # Check whether consecutive points are in several quadrants.
        # It should be q_pts consecutive points in at least quad quadrants.
        result = False
        quadrants = np.array([quadrant(x) for x in self.points])
        for i in range(len(self.points)-self.parameters['q_pts']+1):
            if number_of_quadrants(quadrants[i:i+self.parameters['q_pts']]) > self.parameters['quads']:
                result = True

        return result
