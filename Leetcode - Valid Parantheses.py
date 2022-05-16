# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':')', '[':']', '{':'}'}
        temp_stack = []
        for temp_val in s:
            if temp_val in '[{(':
                temp_stack.append(temp_val)
            elif len(temp_stack) == 0 or temp_val != brackets[temp_stack.pop()]:
                return 0
        return len(temp_stack) == 0
      
# Runtime: 50 ms, faster than 32.45% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 13.9 MB, less than 24.60% of Python3 online submissions for Valid Parentheses.
