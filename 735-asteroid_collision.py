#!/usr/bin/env python3

from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        survivors = []
        for asteroid in asteroids:
            while survivors and asteroid < 0 and survivors[-1] > 0:
                if abs(survivors[-1]) > abs(asteroid):
                    asteroid = 0
                elif abs(survivors[-1]) < abs(asteroid):
                    survivors.pop()
                else:
                    asteroid = 0
                    survivors.pop()
            if asteroid:
                survivors.append(asteroid)
        return survivors

if __name__ == "__main__":
    sln = Solution()
    asteroids1 = [5,10,-5]
    asteroids2 = [8,-8]
    asteroids3 = [10,2,-5]
    print(f"asteroids: {asteroids1} output: {sln.asteroidCollision(asteroids1)}")
    print(f"asteroids: {asteroids2} output: {sln.asteroidCollision(asteroids2)}")
    print(f"asteroids: {asteroids3} output: {sln.asteroidCollision(asteroids3)}")
