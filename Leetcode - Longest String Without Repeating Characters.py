### Given a string s, find the length of the longest substring without repeating characters.

### Example 1:
### Input: s = "abcabcbb"
### Output: 3
### Explanation: The answer is "abc", with the length of 3.

### Example 2:
### Input: s = "bbbbb"
### Output: 1
### Explanation: The answer is "b", with the length of 1.

### Example 3:
### Input: s = "pwwkew"
### Output: 3
### Explanation: The answer is "wke", with the length of 3.
### Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

###Constraints:
### 0 <= s.length <= 5 * 104
### s consists of English letters, digits, symbols and spaces.



class Solution:
    from itertools import permutations
    def lengthOfLongestSubstring(self, s: str) -> int:
        list2 = list(set(list(s)))
        temp_substr = ''
        if len(list2)==len(s):
            return len(s)
        else:
            for x in range(len(list2)):
                temp_count = len(list2)-x
                possible_substrings = permutations(list2,temp_count)
                possible_substrings = list(possible_substrings)
                for substr in possible_substrings:
                    temp_substr = "".join(list(substr))
                    if temp_substr in s:
                        del list2, temp_substr, possible_substrings
                        return temp_count
            return 0
          
###############  Time Limit Exceeded on input "wslznzfxojzd"
