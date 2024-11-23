#!/usr/bin/python3
from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        nb_operations = 0
        left, right = 0, len(nums) - 1
        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum == k:
                nb_operations += 1
                left += 1
                right -= 1
            elif curr_sum < k:
                left += 1
            else:
                right -= 1
        return nb_operations

if __name__ == "__main__":
    sln = Solution()
    nums = [1,2,3,4]
    k = 5
    print(sln.maxOperations(nums, k))
