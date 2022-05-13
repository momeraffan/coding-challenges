### You are given two non-empty linked lists representing two non-negative integers.
### The digits are stored in reverse order, and each of their nodes contains a single digit.
### Add the two numbers and return the sum as a linked list.

### You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

### Example 1:
### Input: l1 = [2,4,3], l2 = [5,6,4]
### Output: [7,0,8]
### Explanation: 342 + 465 = 807.

### Example 2:
### Input: l1 = [0], l2 = [0]
### Output: [0]

### Example 3:
### Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
### Output: [8,9,9,9,0,0,0,1]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1 = ""
        str2 = ""
        dot_next=".next"
        next_val_code=""
        temp_val = 0
        result = ""
        
        len1 = str(l1).count("next")
        len2 = str(l2).count("next")
        
        if len1>=len2:
            for x in range(len1):
                str1 += str(eval("l1"+next_val_code+".val"))
                next_val_code += dot_next
            next_val_code=""
            for x in range(len2):
                str2 += str(eval("l2"+next_val_code+".val"))
                next_val_code += dot_next

            result = int(str1) + int(str2)
            print(result)
            result = str(result)
            result = list(result)
            result = [int(i) for i in result]
            result.reverse()
            ln = ListNode()
            next_val_code=""

            for x in range(len(result)):
                exec("ln" + next_val_code + ".val = " + str(result[x]))
                if x==len(result)-1:
                    break
                else:
                    exec("ln" + next_val_code + ".next = ListNode()")
                next_val_code += dot_next

            del str1, str2, dot_next, next_val_code
            return ln
        else:
            for x in range(len1):
                str1 += str(eval("l1"+next_val_code+".val"))
                str2 += str(eval("l2"+next_val_code+".val"))
                temp_result = int(str1) + int(str2) + int(temp_val)
                temp_val = 0
                if len(str(temp_result))>1:
                    temp_result = str(temp_result)
                    result += temp_result[1]
                    temp_val = int(temp_result[0])
                else:
                    result += str(temp_result)
                next_val_code += dot_next
            if temp_value > 0:
                result += str(temp_val)

            print(result)
            result = list(result)
            result = [int(i) for i in result]
            result.reverse()
            ln = ListNode()
            next_val_code=""

            for x in range(len(result)):
                exec("ln" + next_val_code + ".val = " + str(result[x]))
                if x==len(result)-1:
                    break
                else:
                    exec("ln" + next_val_code + ".next = ListNode()")
                next_val_code += dot_next

            del str1, str2, dot_next, next_val_code
            return ln
