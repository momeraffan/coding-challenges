### Given a string s, return the longest palindromic substring in s.

### Example 1:
### Input: s = "babad"
### Output: "bab"
### Explanation: "aba" is also a valid answer.

### Example 2:
### Input: s = "cbbd"
### Output: "bb"
 

### Constraints:
### 1 <= s.length <= 1000
### s consist of only digits and English letters.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        for xx in range(len(s)):
            for yy in range(xx+1):
                temp_num = yy+(len(s)-xx)
                temp_val1 = s[yy:temp_num]
                if temp_val1==temp_val1[::-1]:
                    del temp_num
                    return temp_val1



# Runtime: 9441 ms, faster than 5.01% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 14 MB, less than 62.01% of Python3 online submissions for Longest Palindromic Substring.
