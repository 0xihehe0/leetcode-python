'''
Author: yaojinxi 864554492@qq.com
Date: 2024-09-06 19:52:57
LastEditors: yaojinxi 864554492@qq.com
LastEditTime: 2024-09-08 13:40:18
FilePath: \leetcode\015\threeSum.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# Step 1:
# We should sort the nums array to ensure that the input array is in non-decreasing order.

# Step 2:
# Start traversing the sorted nums array and initialize two pointers, j and k.
# The j pointer will point to the element next to the current element i, 
# and the k pointer will point to the last element of the array.

# Step 3:
# Create a while loop to use a two-pointer approach with pointers j and k to find triplets whose sum equals zero. 
# Calculate the total sum of the current triplet.

# Step 4:
# If the total is greater than 0, decrement k. 
# If the total is less than 0, increment j. If the total equals 0, 
# add the result to the res list.

# Step 5:
# The result seems to be finished, 
# but we should note that when j is incremented, if it equals the previous value, 
# the result might include duplicate elements. 
# So, we need to handle this situation by skipping over duplicates for both j and i pointers."
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortNums = sorted(nums)
       
        res = []
        for i in range(len(sortNums)):
            if i > 0 and sortNums[i] == sortNums[i-1]:
                continue
            print(i)
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                total = sortNums[i] + sortNums[j] + sortNums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    res.append([sortNums[i] , sortNums[j] , sortNums[k]])
                    j += 1
                    
                    while sortNums[j] == sortNums[j - 1] and j < k:
                        j += 1
        return res
    
nums = [-1,0,1,2,-1,-4]
so = Solution()
result = so.threeSum(nums)
print(result)