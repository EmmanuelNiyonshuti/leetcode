#!/usr/bin/env python3
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                nums.remove(nums[i]) 
            else:
                i += 1
        return len(nums), nums
if __name__ == "__main__":
    sln = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    n, arr = sln.removeDuplicates(nums)
    print(f"array length: {n}, array: {arr}")