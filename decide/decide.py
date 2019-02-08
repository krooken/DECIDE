import numpy as np

def decide(
        numpoints,
        points,
        parameters,
        lcm,
        puv
):

    cmv = np.full(15, False)

    for i in range(len(points)-1):
        if (points[i+1][0] - points[i][0])**2 + (points[i+1][1] - points[i][1])**2 > parameters['length1']**2:
            cmv[0] = True

    pum = np.full((15,15), False)

    for row in range(15):
        for col in range(15):
            if lcm[row,col] == 1:
                pum[row,col] = cmv[row] and cmv[col]
            elif lcm[row,col] == 2:
                pum[row,col] = cmv[row] or cmv[col]
            else:
                pum[row,col] = True

    fuv = np.full(15, False)
    for row in range(15):
        if puv[row]:
            r = True
            for col in range(15):
                r &= pum[row,col]
            fuv[row] = r
        else:
            fuv[row] = True

    result = True
    for final_unlocking_element in fuv:
        result &= final_unlocking_element

    return result
