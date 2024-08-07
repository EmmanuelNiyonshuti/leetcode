#!/usr/bin/env python3

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
       t_iter = iter(t)
       return all(char in t_iter for char in s)


if __name__ == "__main__":
    sln = Solution()
    b = sln.isSubsequence("aaaaaa", "bbaaaa")
    print(b)
