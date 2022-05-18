
### You are given the heads of two sorted linked lists list1 and list2.
### Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

### Example 1:
### Input: list1 = [1,2,4], list2 = [1,3,4]
### Output: [1,1,2,3,4,4]

### Example 2:
#### Input: list1 = [], list2 = []
### Output: []

### Example 3:
### Input: list1 = [], list2 = [0]
### Output: [0]
 

### Constraints:
### The number of nodes in both lists is in the range [0, 50].
### -100 <= Node.val <= 100
### Both list1 and list2 are sorted in non-decreasing order.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = []
        l2 = []
        dot_next=".next"
        next_val_code=""
        temp_val = 0
        result = ""
        
        len1 = str(list1).count("next")
        len2 = str(list2).count("next")
        
        if len1 == 0 and len2 == 0:
            ln = ListNode()
            ln.val = ""
            return ln
        
        for x in range(len1):
            l1.append(int(eval("list1"+next_val_code+".val")))
            next_val_code += dot_next
        next_val_code=""
        for x in range(len2):
            l2.append(int(eval("list2"+next_val_code+".val")))
            next_val_code += dot_next
        l3 = l1 + l2
        l3.sort()
        #print(l3)
        ln = ListNode()
        next_val_code=""
        

        for x in range(len(l3)):
            exec("ln" + next_val_code + ".val = " + str(l3[x]))
            if x==len(l3)-1:
                break
            else:
                exec("ln" + next_val_code + ".next = ListNode()")
            next_val_code += dot_next
        return ln
      
      
### Runtime: 381 ms, faster than 5.22% of Python3 online submissions for Merge Two Sorted Lists.
### Memory Usage: 14.1 MB, less than 32.80% of Python3 online submissions for Merge Two Sorted Lists.
