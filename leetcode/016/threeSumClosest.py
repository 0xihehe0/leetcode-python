'''
Author: yaojinxi 864554492@qq.com
Date: 2024-09-12 14:15:14
LastEditors: yaojinxi 864554492@qq.com
LastEditTime: 2024-09-13 14:23:50
FilePath: \leetcode\016\threeSumClosest.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# "My approach is to use the two-pointer technique to solve the problem.

# Step 1: First of all, 
# we need to sort the input nums array to ensure it is in increasing order.

# Step 2: Start a loop from index 0 to len(nums) - 2. 
# Then, initialize two pointers: right is set to the last index of nums, 
# and left is set to i + 1.

# Step 3: Inside the loop, ensure left is less than right, 
# and calculate the total value as nums[i] + nums[left] + nums[right]. 
# If the total value equals the target, return the total.

# Step 4: In each iteration, update the closest value. 
# If the absolute difference between the target and the total is 
# less than the absolute difference between the target and 
# the current closest value, update the closest value to be the total."

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == target:
                    return total
                
                if abs(total - target) < abs(closest_sum - target):
                    closest_sum = total
                    
                if total < target:
                    left += 1
                
                else:
                    right -= 1                 
                
        return closest_sum
    
nums = [-4, -1, 1, 2, 3]
target = 1
so = Solution()
result = so.threeSumClosest(nums,target)
print(result)