#!/usr/bin/env python3

from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # initialize two numbers to the biggest possible number
        min1 = min2 = float('inf')

        for num in nums:
            #if this num is less than min1 update min1
            if num <= min1:
                min1 = num

            #if this num is greater than min1 but less than min2, update min2
            elif num <= min2:
                min2 = num
            #if greater than both, triplet is found
            else:
                return True
        return False

if __name__ == "__main__":
    sln = Solution()
    nums1 = [1,2,3,4,5]
    nums2 = [5,4,3,2,1]
    nums3 = [2,1,5,0,4,6]
    print(sln.increasingTriplet(nums3))

