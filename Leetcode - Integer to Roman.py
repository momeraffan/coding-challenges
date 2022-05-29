### Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

### Symbol       Value
### I             1
### V             5
### X             10
### L             50
### C             100
### D             500
### M             1000
### For example, 2 is written as II in Roman numeral, just two one's added together.
### 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

### Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV.
### Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX.
### There are six instances where subtraction is used:

### I can be placed before V (5) and X (10) to make 4 and 9. 
### X can be placed before L (50) and C (100) to make 40 and 90. 
### C can be placed before D (500) and M (1000) to make 400 and 900.
### Given an integer, convert it to a roman numeral.

 

### Example 1:
### Input: num = 3
### Output: "III"
### Explanation: 3 is represented as 3 ones.

### Example 2:
### Input: num = 58
### Output: "LVIII"
### Explanation: L = 50, V = 5, III = 3.

### Example 3:
### Input: num = 1994
### Output: "MCMXCIV"
### Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

### Constraints:

### 1 <= num <= 3999



class Solution:
    def intToRoman(self, num: int) -> str:
        if num <= 0 or num > 3999:
            return ''
        else:
            temp_str = list(str(num))
            temp_str.reverse()
            result = ""
            x = len(temp_str)-1
            while x!=-1:
                if x == 3:
                    for y in range(int(temp_str[x])):
                        result += "M"
                elif x == 2:
                    for y in range(int(temp_str[x])):
                        if temp_str[x] == "9":
                            result +="CM"
                            break
                        elif temp_str[x] == "8":
                            result +="DCCC"
                            break
                        elif temp_str[x] == "7":
                            result +="DCC"
                            break
                        elif temp_str[x] == "6":
                            result +="DC"
                            break
                        elif temp_str[x] == "5":
                            result += "D"
                            break
                        elif temp_str[x] == "4":
                            result += "CD"
                            break
                        else:
                            result += "C"
                elif x == 1:
                    for y in range(int(temp_str[x])):
                        if temp_str[x] == "9":
                            result +="XC"
                            break
                        elif temp_str[x] == "8":
                            result+="LXXX"
                            break
                        elif temp_str[x] == "7":
                            result+="LXX"
                            break
                        elif temp_str[x] == "6":
                            result+="LX"
                            break
                        elif temp_str[x] == "5":
                            result += "L"
                            break
                        elif temp_str[x] == "4":
                            result += "XL"
                            break
                        else:
                            result += "X"
                elif x == 0:
                    if temp_str[x] == "9":
                        result +="IX"
                    elif temp_str[x] == "8":
                        result += "VIII"
                    elif temp_str[x] == "7":
                        result += "VII"
                    elif temp_str[x] == "6":
                        result += "VI"
                    elif temp_str[x] == "5":
                        result += "V"
                    elif temp_str[x] == "4":
                        result += "IV"
                    elif temp_str[x] == "3":
                        result += "III"
                    elif temp_str[x] == "2":
                        result += "II"
                    elif temp_str[x] == "1":
                        result += "I"
                else:
                    return result
                x-=1
            return result
          
          
# Runtime: 66 ms, faster than 56.00% of Python3 online submissions for Integer to Roman.
# Memory Usage: 14 MB, less than 35.55% of Python3 online submissions for Integer to Roman.
