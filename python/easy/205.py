s = "google"

s_went = []
s_ls = []
t_went = []
t_ls = []

for i in s:
    if i not in s_went:
        s_went.append(i)
        s_ls.append(s_went.index(i))
        continue

    s_ls.append(s_went.index(i))

print(s_ls)
