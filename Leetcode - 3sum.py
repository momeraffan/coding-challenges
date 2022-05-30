### Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

### Notice that the solution set must not contain duplicate triplets.

 

### Example 1:
### Input: nums = [-1,0,1,2,-1,-4]
### Output: [[-1,-1,2],[-1,0,1]]

### Example 2:
### Input: nums = []
### Output: []
  
### Example 3:
### Input: nums = [0]
### Output: []
 

### Constraints:
### 0 <= nums.length <= 3000
### -105 <= nums[i] <= 105





from itertools import groupby
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<0 or len(nums)>=3000:
            return
        else:
            list_of_lists = []
            temp_nums = nums
            temp_nums.reverse()
            for y in range(len(nums)):
                left_pointer = y
                right_pointer = len(nums)-1
                
                while left_pointer<right_pointer:
                    for x in range(left_pointer+1,right_pointer):
                        temp_list = []
                        if nums[left_pointer]+nums[right_pointer]+nums[x] == 0:
                            temp_list.append(nums[left_pointer])
                            temp_list.append(nums[right_pointer])
                            temp_list.append(nums[x])
                        else:
                            continue
                        list_of_lists.append(temp_list)
                    #left_pointer+=1
                    right_pointer-=1
            
            for x in list_of_lists:
                x.sort()
            list_of_lists.sort()
            list_of_lists = list(list_of_lists for list_of_lists,_ in groupby(list_of_lists))
            return list_of_lists

# 315 / 318 test cases passed.
