
### Write a function to find the longest common prefix string amongst an array of strings.
### If there is no common prefix, return an empty string "".

 

### Example 1:
### Input: strs = ["flower","flow","flight"]
### Output: "fl"

### Example 2:
### Input: strs = ["dog","racecar","car"]
### Output: ""
### Explanation: There is no common prefix among the input strings.
 

### Constraints:
### 1 <= strs.length <= 200
### 0 <= strs[i].length <= 200
### strs[i] consists of only lower-case English letters.



class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        number_of_strs = len(strs)
        minimum_str_len = len(strs[0])
        temp_list = []
        prefix = {}
        for x in range(number_of_strs):
            if len(strs[x])<minimum_str_len:
                minimum_str_len =  len(strs[x])
        for x in strs:
            temp_list.append(x[0:minimum_str_len])
        first_word =list(strs[0][0:minimum_str_len])
        #for x in range(number_of_strs+1):
        for z in range(minimum_str_len):
            for y in temp_list:
                if y[z]==first_word[z] and y[z] not in prefix:
                    prefix[z]=y[z]
                    #print(y[z],first_word[z], prefix)    
                elif y[z] != first_word[z]:
                    prefix.popitem()
                    return "".join(prefix.values())
                else:
                    if len(prefix) == 0:
                        return ""
                        
        return "".join(prefix.values())
      
# Runtime: 40 ms, faster than 72.66% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 14.1 MB, less than 11.98% of Python3 online submissions for Longest Common Prefix.
