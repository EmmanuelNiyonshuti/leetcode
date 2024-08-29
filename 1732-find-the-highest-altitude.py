#!/usr/bin/env python3

from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr_alt = 0
        max_alt = 0
        for g in gain:
            curr_alt += g
            if curr_alt > max_alt:
                max_alt = curr_alt
        return max_alt
        # alt = [0]
        # n = len(gain)
        # for g in range(0, n):
            # net_gain = alt[g] + gain[g]
            # alt.append(net_gain)
        # return max(alt)

if __name__ == "__main__":
    sln = Solution()
    gain = [-5,1,5,0,-7]
    # gain = [-4,-3,-2,-1,4,3,2]
    print(sln.largestAltitude(gain))
