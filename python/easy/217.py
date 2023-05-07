from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        tmp = set()
        for i in nums:
            if i in tmp:
                return True
            tmp.add(i)
        return False


solve = Solution()

print(solve.containsDuplicate(nums))
