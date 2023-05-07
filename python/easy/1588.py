from typing import List


def sumOddLengthSubarrays(arr: List[int]) -> int:
    ans = 0
    ls = []
    for i in range(len(arr) + 1):
        for j in range(i):
            ls.append(arr[j:i])

    for i, v in enumerate(ls):
        # print(v)
        if len(v) % 2 == 0:
            # ls.pop(i)
            continue
        ans += sum(v)
        # return

    # for i in ls:
    #     ans += sum(i)

    # print(ans)
    return ans


sumOddLengthSubarrays([1, 4, 2, 5, 3])
