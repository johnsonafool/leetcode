# if s1 == s2:
#     return True

s1 = "yhy"

s2 = "hyc"

diff_pair = []
for i in zip(s1, s2):
    if len(diff_pair) > 2:
        print(False)
        # return False
    if i[0] != i[1]:
        diff_pair.append(set((i[0], i[1])))

if len(diff_pair) == 1:
    print(False)
    # return False

# if diff_pair[0] == diff_pair[1]:

# return False
