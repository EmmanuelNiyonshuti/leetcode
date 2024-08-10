#!/usr/bin/env python3


class Solution:
    def reverseWords(self, s: str) -> str:
        #utizing builtins
        s = s.split()
        s.reverse()
        return " ".join(s)




if __name__ == "__main__":
    sln = Solution()
    s0 = "the sky is blue"
    s1 = "  hello world  "
    output = sln.reverseWords(s1)
    print(output)
