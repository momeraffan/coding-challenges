### Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

### Example 1:
### Input: head = [1,1,2]
### Output: [1,2]

### Example 2:
### Input: head = [1,1,2,3,3]
### Output: [1,2,3]
 

### Constraints:
### The number of nodes in the list is in the range [0, 300].
### -100 <= Node.val <= 100
### The list is guaranteed to be sorted in ascending order.





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        len_check = str(head).count("next")
        if len_check == 0:
            ln = ListNode()
            ln.val = ""
            return ln
        else:
            head_code="head"
            next_node_code=".next"
            next_val_code=".val"
            temp_val = head.next
            temp_list = [head.val]

            while temp_val!=None:
                head_code+=next_node_code
                temp_val = eval(head_code+".next")
                temp_list.append(eval(head_code+next_val_code))
            temp_list=list(set(temp_list))
            temp_list.sort()
            head_code="head"
            next_node_code=".next"
            next_val_code=""
            new_linked_list_node = ListNode()
            for x in range(len(temp_list)):
                exec("new_linked_list_node" + next_val_code + ".val = " + str(temp_list[x]))
                if x==len(temp_list)-1:
                    break
                else:
                    exec("new_linked_list_node" + next_val_code + ".next = ListNode()")
                next_val_code += next_node_code
            return new_linked_list_node
            
            
            
# Runtime: 3239 ms, faster than 5.05% of Python3 online submissions for Remove Duplicates from Sorted List.
# Memory Usage: 14.6 MB, less than 28.85% of Python3 online submissions for Remove Duplicates from Sorted List.
