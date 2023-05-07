from typing import List


class Solution(object):
    def pivotIndex(self, nums):
        # Time: O(n)
        # Space: O(1)
        left, right = 0, sum(nums)
        for index, num in enumerate(nums):
            right -= num
            if left == right:
                print(index)
                return index
            left += num
        return -1


# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
#         pivot_index = len(nums) // 2
#         left_sum = 0
#         right_sum = 0
#         for i in nums[:pivot_index]:
#             left_sum += i

#         for i in nums[pivot_index + 1 :]:
#             right_sum += i

#         if right_sum == left_sum:
#             return pivot_index

#         r_diff = nums[pivot_index] - nums[pivot_index + 1]
#         l_diff = nums[pivot_index] - nums[pivot_index - 1]

#         def move():
#             if right_sum > left_sum:
#                 right_sum -= nums[pivot_index + 1]
#                 left_sum += nums[pivot_index - 1]
#                 pivot_index += 1

#             if right_sum < left_sum:
#                 right_sum += nums[pivot_index + 1]
#                 left_sum -= nums[pivot_index - 1]
#                 pivot_index -= 1

#             else:
#                 return pivot_index

#             move()

#         move()


sol = Solution()

sol.pivotIndex([1, 7, 3, 6, 5, 6])
