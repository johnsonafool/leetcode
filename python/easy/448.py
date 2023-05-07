from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = set(nums)
        ans = []
        arr = [None] * n
        # print(arr)
        for i in s:
            arr[i - 1] = i

        for index, value in enumerate(arr):
            # print(index)
            if value == None:
                ans.append(index + 1)

        return ans


solve = Solution()

print(solve.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
