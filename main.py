"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""


def two_sum(nums, target):
    for idx in range(len(nums)):

        this_num = nums[idx]
        for idx_aux in range(len(nums)):
            if idx_aux == idx:
                continue
            this_sum = this_num + nums[idx_aux]
            if this_sum == target:
                return idx, idx_aux

    return "The target value is not available within the possible sums of two individual numbers contained in the integer array"


print(two_sum([0, 1, -1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0))
