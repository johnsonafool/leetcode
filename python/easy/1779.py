import math

points = [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]

x, y = 3, 4

dist_ls = []
for i in points:
    # check point is valid
    if i[0] == x:
        valid_dis = abs(i[0] - x) + abs(i[1] - y)
        dist_ls.append(valid_dis)
        continue

    elif i[0] == y:
        valid_dis = abs(i[0] - x) + abs(i[1] - y)
        dist_ls.append(valid_dis)
        continue

    # count the mahattan distance
    # valid_dist = abs(i[0]-x) + abs(i[1]-y)
    invalid_point = math.inf
    dist_ls.append(invalid_point)


print(dist_ls)
# print(xy.index(min(xy)))
print(dist_ls.index(min(dist_ls)))
