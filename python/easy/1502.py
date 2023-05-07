arr = [0, 0, 1]


arr.sort()
pre_diff = None
for i in range(len(arr) - 1):
    diff = arr[i + 1] - arr[i]
    if not pre_diff:
        pre_diff = diff
    if abs(diff) != abs(pre_diff):
        print("false")
        # return False
    pre_diff = diff
