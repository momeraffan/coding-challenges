# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21

# Constraints:
# -231 <= x <= 231 - 1

class Solution:
    def reverse(self, x: int) -> int:
        if (x > 2147483647) or (x < -2147483648):
            return 0
        else:
            temp_str1 = str(x)
            temp_str2 = temp_str1[::-1]
            #print("ok: " , temp_str2)
            if temp_str1[0]=='-':
                temp_str2 = '-' + temp_str2[0:len(temp_str2)-1]
                if int(temp_str2) < -2147483648:
                    return 0
                else:
                    return int(temp_str2)
            else:
                if int(temp_str2) > 2147483647:
                    return 0
                else:
                    return int(temp_str2)
                    
# Runtime: 39 ms, faster than 69.16% of Python3 online submissions for Reverse Integer.
# Memory Usage: 13.9 MB, less than 63.94% of Python3 online submissions for Reverse Integer.
