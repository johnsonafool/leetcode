# get all bit represent
dic = {}
for i, v in enumerate([0, 1, 2, 3, 4, 5, 6, 7, 8]):
    dic[v] = v.bit_count()

sort_dic = sorted((value, key) for (key, value) in dic.items())

print([i[1] for i in sort_dic])
