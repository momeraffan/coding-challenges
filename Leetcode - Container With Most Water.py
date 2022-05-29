### You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

### Find two lines that together with the x-axis form a container, such that the container contains the most water.

### Return the maximum amount of water a container can store.
### Notice that you may not slant the container.

 

### Example 1:
### Input: height = [1,8,6,2,5,4,8,3,7]
### Output: 49
### Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
### In this case, the max area of water (blue section) the container can contain is 49.

### Example 2:
### Input: height = [1,1]
### Output: 1
 

### Constraints:

### n == height.length
### 2 <= n <= 105
### 0 <= height[i] <= 104


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_pointer = 0
        right_pointer = len(height) - 1
        max_area = -1
        
        while left_pointer < right_pointer:
            if height[left_pointer]<height[right_pointer]:
                temp_height = height[left_pointer]
            else:
                temp_height = height[right_pointer]
            temp_width = right_pointer - left_pointer
            if max_area < temp_height * temp_width:
                max_area = temp_height * temp_width
            
            if height[left_pointer] > height[right_pointer]:
                right_pointer -= 1
            else:
                left_pointer += 1
        
        return max_area

# Runtime: 1001 ms, faster than 43.25% of Python3 online submissions for Container With Most Water.
# Memory Usage: 27.5 MB, less than 57.21% of Python3 online submissions for Container With Most Water.
