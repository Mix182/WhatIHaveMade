def copy(list2d):
    nl = [[x for x in range(len(list2d[0]))]for y in range(len(list2d))]
    for y in range(len(list2d)):
        for x in range(len(list2d[y])):
            nl[y][x] = list2d[y][x]

    return nl