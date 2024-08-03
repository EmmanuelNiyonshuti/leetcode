#!/usr/bin/env python3
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) - 1
        while l <= h:
            mid = (l + h)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                h = mid - 1
        return l
        
if __name__ == "__main__":
    sln = Solution()
    nums = [2,5]
    target = 5
    # nums = [1,3,5,6]
    # target = 7
    i = sln.searchInsert(nums, target)
    print(i)