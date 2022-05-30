# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:
# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8







from itertools import permutations as p
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        temp_str = ""
        temp_list = []
        temp_permutations = []
        for x in range(n):
            temp_str+="()"
        temp_permutations = list(set(p(temp_str,n*2)))
        print(len(temp_permutations))
        print(temp_permutations)
        for x in temp_permutations:
            temp_str = "".join(x)
            brackets = {'(':')', '[':']', '{':'}'}
            temp_stack = []
            for temp_val in temp_str:
                if temp_val in '[{(':
                    temp_stack.append(temp_val)
                elif len(temp_stack) == 0 or temp_val != brackets[temp_stack.pop()]:
                    continue
            if len(temp_stack) == 0 and temp_str not in temp_list:
                temp_list.append(temp_str)
            else:
                continue
        return temp_list
      
      
      
      
      
      # 5/8 test cases passed
