nums = [5]
target = -5

h_index = len(nums) - 1
l_index = 0
mid_index = 0

while h_index >= l_index:
    mid_index = (h_index + l_index) // 2

    # case target greater
    if target > nums[mid_index]:
        l_index = mid_index + 1

    elif target < nums[mid_index]:
        h_index = mid_index - 1

    else:
        print(mid_index)

print(-1)
