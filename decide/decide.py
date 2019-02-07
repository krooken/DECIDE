def decide(
        numpoints,
        points,
        parameters,
        lcm,
        puv
):

    result = True
    for pue in puv:
        result &= not pue

    return result