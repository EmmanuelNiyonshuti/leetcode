#!/usr/bin/python3

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        prefix = 1
        for i in range(n):
           answer[i] = prefix
           prefix *= nums[i]
        suffix = 1
        for i in range(n -1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        return answer


if __name__ == "__main__":
    sln = Solution()
    #nums = [1,2,3,4]
    nums = [-1,1,0,-3,3]
    ans = sln.productExceptSelf(nums)
    print(ans)
