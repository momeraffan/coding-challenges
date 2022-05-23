### The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

### P   A   H   N
### A P L S I I G
### Y   I   R
### And then read line by line: "PAHNAPLSIIGYIR"

### Write the code that will take a string and make this conversion given a number of rows:
### string convert(string s, int numRows);

### Example 1:
### Input: s = "PAYPALISHIRING", numRows = 3
### Output: "PAHNAPLSIIGYIR"

### Example 2:
### Input: s = "PAYPALISHIRING", numRows = 4
### Output: "PINALSIGYAHRPI"
### Explanation:
### P     I    N
### A   L S  I G
### Y A   H R
### P     I

### Example 3:
### Input: s = "A", numRows = 1
### Output: "A"

### Constraints:
### 1 <= s.length <= 1000
### s consists of English letters (lower-case and upper-case), ',' and '.'.
### 1 <= numRows <= 1000


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        temp_val1 = list(s)
        temp_val2 = ""
        marker = 0
        for x in range(numRows):
            counter = numRows-x-1
            while 0 in temp_val1:
                temp_val1.remove(0)
            #print(temp_val)
            #print(temp_val2.replace("0",""))
            marker = 0
            for y in range(len(temp_val1)):
                if marker < len(temp_val1):
                    if x == 0:
                        temp_val2+=str(temp_val1[marker])
                        temp_val1[marker] = 0
                        marker+=counter+counter
                    else:
                        temp_val2+=str(temp_val1[marker])
                        temp_val1[marker] = 0
                        if marker==0:
                            marker+=counter+counter
                        else:
                            if marker+1 < len(temp_val1):
                                temp_val2+=str(temp_val1[marker+1])
                                temp_val1[marker+1] = 0
                                marker+=counter+counter+1
                            else:
                                marker = 0
                else:
                    marker = 0
        for x in temp_val1:
            if x == 0:
                continue
            else:
                temp_val2+=x
        temp_val2 = temp_val2.replace("0","")
        return temp_val2
    
    
    
# Runtime: 2998 ms, faster than 5.01% of Python3 online submissions for Zigzag Conversion.
# Memory Usage: 14.6 MB, less than 7.93% of Python3 online submissions for Zigzag Conversion.
