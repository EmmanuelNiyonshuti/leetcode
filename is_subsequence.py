#!/usr/bin/env python3

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while j < len(s) and i < len(t):
            if s[j] == t[i]:
                j += 1
            i += 1
        return j == len(s)


if __name__ == "__main__":
    sln = Solution()
    b = sln.isSubsequence("aaaaaa", "bbaaaa")
    print(b)
