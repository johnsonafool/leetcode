from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set(nums)
        dict = {}
        for i in s:
            # print(i)
            dict[i] = 0

        for i in nums:
            dict[i] += 1
            if dict[i] > 1:
                dict.pop(i)

        [(k, _)] = dict.items()

        return k


s = Solution()

sol = s.singleNumber(nums=[4, 1, 2, 1, 2])
