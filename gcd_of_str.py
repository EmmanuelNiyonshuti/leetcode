#!/usr/bin/python3

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """If concatenations in both orders (str1 + str2 and str2 + str1)
        are not equal, return empty string."""
        if str1 + str2 != str2 + str1:
            return ""

        def gcd(a, b):
            """ calculate the GCD using euclidean algorithm"""
            while b:
                a, b = b, a % b
            return a
        #Find GCD of the lengths of the two strings
        gcd_len = gcd(len(str1), len(str2))
        #The GCD string will be the substring from either string up to the gcd_len
        return str1[:gcd_len]
    
if __name__ == "__main__":
    sln = Solution()
    print(sln.gcdOfStrings("ABCABC", "ABC"))
    print(sln.gcdOfStrings("ABABAB", "ABAB"))
    print(sln.gcdOfStrings("LEET", "CODE"))
