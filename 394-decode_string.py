#!/usr/bin/env python3

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substr)
        return "".join(stack)

if __name__ == "__main__":
    sln = Solution()
    s2 = "2[abc]3[cd]ef"
    print(f"{s2}: {sln.decodeString(s2)}")
    s1 = "3[a2[c]]"
    print(f"{s1}: {sln.decodeString(s1)}")
