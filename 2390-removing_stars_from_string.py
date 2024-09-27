#!/usr/bin/env python3

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "*":
                stack.append(char)
            else:
                stack.pop()
        return "".join(stack)

if __name__ == "__main__":
    sln = Solution()
    s1 = "leet**cod*e"
    s2 = "erase*****"
    print(f"{s1}: {sln.removeStars(s1)}")
    print(f"{s2}: {sln.removeStars(s2)}")

