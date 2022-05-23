### Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

### The algorithm for myAtoi(string s) is as follows:

### Read in and ignore any leading whitespace.
### Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either.
### This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
### Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
### Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
### If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range.
### Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
### Return the integer as the final result.
                                                                                             
### Note:
### Only the space character ' ' is considered a whitespace character.
### Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
 

### Example 1:
### Input: s = "42"
### Output: 42
### Explanation: The underlined characters are what is read in, the caret is the current reader position.
### Step 1: "42" (no characters read because there is no leading whitespace)
###          ^
### Step 2: "42" (no characters read because there is neither a '-' nor '+')
###          ^
### Step 3: "42" ("42" is read in)
###            ^
### The parsed integer is 42.
### Since 42 is in the range [-231, 231 - 1], the final result is 42.

### Example 2:
### Input: s = "   -42"
### Output: -42
### Explanation:
### Step 1: "   -42" (leading whitespace is read and ignored)
###             ^
### Step 2: "   -42" ('-' is read, so the result should be negative)
###              ^
### Step 3: "   -42" ("42" is read in)
###                ^
### The parsed integer is -42.
### Since -42 is in the range [-231, 231 - 1], the final result is -42.

### Example 3:
### Input: s = "4193 with words"
### Output: 4193
### Explanation:
### Step 1: "4193 with words" (no characters read because there is no leading whitespace)
###          ^
### Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
###          ^
### Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
###              ^
### The parsed integer is 4193.
### Since 4193 is in the range [-231, 231 - 1], the final result is 4193.
 
### Constraints:
### 0 <= s.length <= 200
### s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.



class Solution:
    def myAtoi(self, s: str) -> int:
        temp_val = temp_val1 = ""
        is_num = 0
        is_plus_minus = 0
        for x in s:
            if x in ["1","2","3","4","5","6","7","8","9","0"]:
                temp_val += x
                is_num = 1
            elif x == " " and is_num == 0 and is_plus_minus == 0:
                temp_val+=x
            elif (x == "+" or x == "-") and is_plus_minus==0:
                temp_val += x
                is_plus_minus =1
            else:
                break
        if len(s) == 0:
            return 0
        elif not any(x in ["1","2","3","4","5","6","7","8","9","0"] for x in list(set(temp_val))):
            return 0
        else:
            temp_val = temp_val.replace(" ","")
            #print(temp_val)
            if temp_val[0]=="+" or temp_val[0]=="-":
                if int(temp_val) > 2147483647:
                    return 2147483647
                elif int(temp_val) < -2147483648:
                    return -2147483648
                else:
                    return int(temp_val)
            elif temp_val[0] == ".":
                return 0
            else:
                for x in temp_val:
                    if x in ["+","-","."]:
                        break
                    else:
                        temp_val1 += x
                temp_val = temp_val1
                del temp_val1
                print(int(temp_val))
                if int(temp_val) > 2147483647:
                    return 2147483647
                elif int(temp_val) < -2147483648:
                    return -2147483648
                else:
                    return int(temp_val)
                  
                  
# Runtime: 47 ms, faster than 53.83% of Python3 online submissions for String to Integer (atoi).
# Memory Usage: 14.1 MB, less than 30.41% of Python3 online submissions for String to Integer (atoi).
