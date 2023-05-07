from typing import List


class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     d = {}

    #     for index, value in enumerate(nums):
    #         if value in d:
    #             return [d[value], index]
    #         else:
    #             k = target - value
    #             d[k] = index
    #     return
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, i_v in enumerate(nums):
            for j, j_v in enumerate(nums):
                # if i_v == j_v:
                #     continue
                if i_v + j_v == target:
                    # print([i, j])
                    return [i, j]


sol = Solution()

print(sol.twoSum(nums=[2, 7, 11, 15], target=9))
