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
        list1 = list(s)
        list2 = list(set(list1))
        temp_list = []
        final_val = 0
        if len(list2)==len(s):
            return len(s)
        elif len(list2)==0:
            return 0
        else:
            for xx in range(len(s)):
                for yy in range(xx):
                    if yy+xx>len(s):
                        break
                    else:
                        temp_val = s[yy:yy+xx]
                        #temp_list.append(len(temp_val))
                        if len(temp_val)==len(list(set(list(s[yy:yy+xx])))):
                            #print(len(temp_val))
                            if len(temp_val)>final_val:
                                final_val = len(temp_val)
        return final_val
                            #print(len(temp_val))
                        #for a in list2:
                            #temp_dict[a]=temp_val.count(a)
                            #print(temp_val, temp_dict)
                            #print(list(temp_dict.values()))
