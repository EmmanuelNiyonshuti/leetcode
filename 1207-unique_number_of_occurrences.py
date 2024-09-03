#!/usr/bin/env python3

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        dict_obj = {}
        for i in arr:
            if i in dict_obj:
                dict_obj[i] += 1
            else:
                dict_obj[i] = 0
        return len(set(dict_obj.values())) == len(dict_obj.values())

if __name__ == "__main__":
    # arr = [1,2,2,1,1,3]
    # arr = [1,2]
    arr = [-3,0,1,-3,1,1,1,-3,10,0]
    sln = Solution()
    print(sln.uniqueOccurrences(arr))