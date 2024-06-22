"""
Merge the strings by adding letters in alternating order, starting with word1.
If a string is longer than the other,
append the additional letters onto the end of the merged string.
"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if type(word1) is not str or type(word2) is not str:
            return
        lst = []
        i = 0
        j = 0
        n1 = len(word1)
        n2 = len(word2)
        while i < n1 or j < n2:
            if i < n1:
                lst.append(word1[i])
                i += 1
            if j < n2:
                lst.append(word2[j])
                j += 1
        return "".join(lst)
