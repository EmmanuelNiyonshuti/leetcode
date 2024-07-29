#!/usr/bin/python3
from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not flowerbed:
            return n == 0
        length = len(flowerbed)
        if length == 1:
            if flowerbed[0] == 0:
                flowerbed[0] == 1
                n -= 1
        elif flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1
        if length > 1:
            if flowerbed[-1] == 0 and flowerbed[-2] == 0:
                flowerbed[-1] = 1
                n -= 1
        for i in range(1, length - 1):
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
            if n == 0:
                return True

        return n <= 0

if __name__ == "__main__":
    sln = Solution()
    flowerbed = [0]
    # flowerbed = [1,0,0,0,1,0,0]
    # flowerbed = [0,0,1,0,0]
    n = 1
    print(sln.canPlaceFlowers(flowerbed, n))
