### Given two binary strings a and b, return their sum as a binary string.
 

### Example 1:
### Input: a = "11", b = "1"
### Output: "100"

### Example 2:
### Input: a = "1010", b = "1011"
### Output: "10101"

### Constraints:
### 1 <= a.length, b.length <= 104
### a and b consist only of '0' or '1' characters.
### Each string does not contain leading zeros except for the zero itself.



class Solution:
    def addBinary(self, a: str, b: str) -> str:
        stack = []
        carry = 0
        len_a = len(a)
        len_b = len(b)
        if len_a>=len_b:
            for x in range(len_a):
                if x>=len_b:
                    if int(a[len_a-x-1]) == 1 and carry == 1:
                        stack.append("0")
                        carry = 1
                        continue
                    elif int(a[len_a-x-1]) == 1 and carry == 0:
                        stack.append("1")
                        carry = 0
                        continue
                    elif int(a[len_a-x-1]) == 0 and carry == 1:
                        stack.append("1")
                        carry = 0
                        print(stack)
                        continue
                    else:
                        if carry == 0:
                            stack.append("0")
                        else:
                            stack.append("1")
                        carry = 0
                else:
                    if int(a[len_a-x-1]) == 1 and int(b[len_b-x-1]) == 1 and carry == 0:
                        carry = 1
                        stack.append("0")
                        continue
                    elif int(a[len_a-x-1]) == 0 and int(b[len_b-x-1]) == 1 and carry == 0:
                        carry = 0
                        stack.append("1")
                        continue
                    elif int(a[len_a-x-1]) == 1 and int(b[len_b-x-1]) == 0 and carry == 0:
                        carry = 0
                        stack.append("1")
                        continue
                    elif int(a[len_a-x-1]) == 1 and int(b[len_b-x-1]) == 1 and carry == 1:
                        carry = 1
                        stack.append("1")
                        continue
                    elif int(a[len_a-x-1]) == 0 and int(b[len_b-x-1]) == 1 and carry == 1:
                        carry = 1
                        stack.append("0")
                        continue
                    elif int(a[len_a-x-1]) == 1 and int(b[len_b-x-1]) == 0 and carry == 1:
                        carry = 1
                        stack.append("0")
                        continue
                    elif int(a[len_a-x-1]) == 0 and int(b[len_b-x-1]) == 0 and carry == 1:
                        carry = 0
                        stack.append("1")
                        continue
                    else:
                        carry = 0
                        stack.append("0")
                        continue
            if carry == 1:
                stack.append(str(carry))
        else:
            for x in range(len_b):
                if x>=len_a:
                    if carry == 1 and int(b[len_b-x-1]) == 1:
                        stack.append("0")
                        carry = 1
                        continue
                    elif carry == 0 and int(b[len_b-x-1]) == 1:
                        stack.append("1")
                        carry = 0
                        continue
                    elif carry == 1 and int(b[len_b-x-1]) == 0:
                        stack.append("1")
                        carry = 0
                        continue
                    else:
                        if carry == 0:
                            stack.append("0")
                        else:
                            stack.append("1")
                        carry = 0
                else:
                    if int(b[len_b-x-1]) == 1 and int(a[len_a-x-1]) == 1 and carry == 0:
                        carry = 1
                        stack.append("0")
                        continue
                    elif int(b[len_b-x-1]) == 0 and int(a[len_a-x-1]) == 1 and carry == 0:
                        carry = 0
                        stack.append("1")
                        continue
                    elif int(b[len_b-x-1]) == 1 and int(a[len_a-x-1]) == 0 and carry == 0:
                        carry = 0
                        stack.append("1")
                        continue
                    elif int(b[len_b-x-1]) == 1 and int(a[len_a-x-1]) == 1 and carry == 1:
                        carry = 1
                        stack.append("1")
                        continue
                    elif int(b[len_b-x-1]) == 0 and int(a[len_a-x-1]) == 1 and carry == 1:
                        carry = 1
                        stack.append("0")
                        continue
                    elif int(b[len_b-x-1]) == 1 and int(a[len_a-x-1]) == 0 and carry == 1:
                        carry = 1
                        stack.append("0")
                        continue
                    elif int(b[len_b-x-1]) == 0 and int(a[len_a-x-1]) == 0 and carry == 1:
                        carry = 0
                        stack.append("1")
                        continue
                    else:
                        carry = 0
                        stack.append("0")
                        continue
            if carry == 1:
                stack.append(str(carry))
        stack.reverse()
        return "".join(stack)
      
      
# Runtime: 41 ms, faster than 67.15% of Python3 online submissions for Add Binary.
# Memory Usage: 14.3 MB, less than 24.35% of Python3 online submissions for Add Binary.
