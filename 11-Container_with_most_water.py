#!/usr/bin/python3

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            short_height = min(height[left], height[right])
            area = width * short_height
            if area > max_area:
                max_area = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

if __name__ == "__main__":
    sln = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    print(sln.maxArea(height))
