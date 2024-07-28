#!/usr/bin/python3
from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        #find max number of candies any kid has
        max_candies = max(candies)
        #creates a new list where each element is the result of condition
        return [candy + extraCandies >= max_candies for candy in candies]


if __name__ == "__main__":
    sln = Solution()
    # candies = [2,3,5,1,3]
    candies = [12,1,12]
    extraCandies = 3
    l = sln.kidsWithCandies(candies, extraCandies)
    print(l)
