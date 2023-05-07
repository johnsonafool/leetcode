from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [None] * (n + 1)
        for i in nums:
            arr[i] = i

        ans = arr.index(None)
        return ans


solve = Solution()

print(solve.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
