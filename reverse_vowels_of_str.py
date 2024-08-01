#!/usr/bin/python3

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and s[left].lower() not in vowels:
                left += 1
            while left < right and s[right].lower() not in vowels:
                right -= 1
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return ''.join(s)




if __name__ == "__main__":
    sln = Solution()
    rev_str = sln.reverseVowels("leetcode")
    print(rev_str)