#!/usr/bin/python3

from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        write_pos = 0
        curr_char = chars[0]
        count = 1
        for i in range(1, len(chars)):
            if curr_char == chars[i]:
                count += 1
            else:
                chars[write_pos] = curr_char
                write_pos += 1

                if count > 1:
                    count_str = str(count)
                    for digit in count_str:
                        chars[write_pos] = digit
                        write_pos += 1
                curr_char = chars[i]
                count = 1
        chars[write_pos] = curr_char
        write_pos += 1
        if count > 1:
            count_str = str(count)
            for digit in count_str:
                chars[write_pos] = digit
                write_pos += 1
        return write_pos

if __name__ == "__main__":
    sln = Solution()
    #chars = ["a","a","b","b","c","c","c"]
    #chars = ["a"]
    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    print(sln.compress(chars))
