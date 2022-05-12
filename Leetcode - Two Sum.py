### Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
### You may assume that each input would have exactly one solution, and you may not use the same element twice.
### You can return the answer in any order.

### Example 1:
### Input: nums = [2,7,11,15], target = 9
### Output: [0,1]
### Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

### Example 2:
### Input: nums = [3,2,4], target = 6
### Output: [1,2]
### Example 3:

### Input: nums = [3,3], target = 6
### Output: [0,1]
 

### Constraints:
### 2 <= nums.length <= 104
### -109 <= nums[i] <= 109
### -109 <= target <= 109
### Only one valid answer exists.



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp_list = []
        if len(nums)<2 or len(nums)>10000:
            pass
        else:
            if target>1000000000 or target<-1000000000:
                pass
            else:
                for x in range(len(nums)):
                    for y in range(len(nums)):
                        if nums[x]+nums[y]==target and x!=y:
                            return x,y
                        else:
                            continue
                            
###All test cases passed, but time limit exceeded using code above...
###################################################################################################

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp_list = []
        for x in range(len(nums)):
            if target-nums[x] in nums and x!=nums.index(target-nums[x]):
                return x, nums.index(target-nums[x])
            else:
                continue

### Success 
### Runtime: 1100 ms, faster than 32.00% of Python3 online submissions for Two Sum.
### Memory Usage: 14.9 MB, less than 76.45% of Python3 online submissions for Two Sum.
