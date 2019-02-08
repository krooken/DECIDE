def decide(
        numpoints,
        points,
        parameters,
        lcm,
        puv
):

    result = True
    for preliminary_unlocking_element in puv:
        result &= not preliminary_unlocking_element

    return result