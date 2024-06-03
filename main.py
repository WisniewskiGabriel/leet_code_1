"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""


def two_sum(nums, target):
    for idx in range(len(nums)):

        int_sum = nums[(idx - 1)] + nums[idx]

        if int_sum == target:

            if nums[idx - 1] >= 0:
                num_0 = nums[idx - 1]
            else:
                num_0 = 0

            num_1 = nums[idx]

            str_res = str(num_0) + ", " + str(num_1)
            print(str_res)
            return str_res

        idx += 1


two_sum([1, 3, 2, 5, 6, 32, 2], 5)
