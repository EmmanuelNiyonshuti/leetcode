#!/usr/bin/env python3

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        triangle = [[1], [1, 1]]
        for i in range(2, numRows):
            row = [1]
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
            triangle.append(row)
        return triangle

if __name__ == "__main__":
    sln = Solution()
    pascals_triangle = sln.generate(5)
    for rows in pascals_triangle:
        print(rows)

        