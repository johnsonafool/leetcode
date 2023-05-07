mat = [[1, 2], [3, 4]]


def matrixReshape(mat):
    # logic to doing the reshape in valid mat
    c = 4
    ans = []
    ls_c = []
    for i in mat:
        for j in i:
            ls_c.append(j)

            if len(ls_c) == c:
                ans.append(ls_c)
                ls_c = []
                continue

    print(ans)


matrixReshape(mat)
