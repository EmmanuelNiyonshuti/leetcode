#!/usr/bin/env python3

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        Finds the max average of a sub array with length k in nums array
        using sliding window algorithm.
        Args:
            nums: array of integers.
            k: length of the subarray.
        Return:
            a float.
        """
        n = len(nums)
        curr_sum = sum(nums[:k])
        max_sum = curr_sum
        for i in range(k, n):
            curr_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, curr_sum)
        return max_sum / k


if __name__ == "__main__":
    sln = Solution()
    nums1 = [1, 12, -5, -6, 50, 3]
    k1 = 4
    nums2 = [5]
    k2 = 1
    print(f"Max average of {nums1} with k: {k1} is {sln.findMaxAverage(nums1, k1)}")
    print(f"Max average of {nums2} with k: {k2} is {sln.findMaxAverage(nums2, k2)}")



