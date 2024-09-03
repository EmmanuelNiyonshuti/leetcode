#!/usr/bin/env python3

class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        s1 = set(nums1)
        s2 = set(nums2)
        # ans = [[], []]
        # for i in s1:
            # if not i in s2:
                # ans[0].append(i)
        # for j in s2:
            # if not j in s1:
                # ans[1].append(j)
        # return ans
        return [list(s1.difference(s2)), list(s2.difference(s1))]


if __name__ == "__main__":
    nums1 = [1,2,3]
    nums2 = [2,4,6]
    # nums1 = [1,2,3,3]
    # nums2 = [1,1,2,2]

    sln = Solution()
    print(sln.findDifference(nums1, nums2))