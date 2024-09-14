'''
Author: yaojinxi 864554492@qq.com
Date: 2024-03-06 19:19:30
LastEditors: yaojinxi 864554492@qq.com
LastEditTime: 2024-09-14 11:14:42
FilePath: \leetcode\075\sortColors.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
class Solution(object):
    def sortColors(self, nums):
        n = len(nums)
        ptr = 0
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1
        for i in range(ptr, n):
            if nums[i] == 1:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1
            
    def sortColors2(self,nums):
        p0, p1 = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[p0], nums[i] = nums[i], nums[p0]
                if p0 < p1:  # 当p0和p1不相等时，需要调整p1位置的元素
                    nums[p1], nums[i] = nums[i], nums[p1]
                p0 += 1
                p1 += 1
            elif nums[i] == 1:
                nums[p1], nums[i] = nums[i], nums[p1]
                p1 += 1
                
#     Step 1:
# I will create a dictionary to store the frequency of each color in the input nums array.

# Step 2:
# I will update the array by first getting the frequency of each color and initializing a variable called index.

# Step 3:
# Increment the index by the frequency to move to the next segment of the array for the next color.            
                
    def sortColors3(self,nums):
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
            
        index = 0
        for color in range(3):
            freq = count.get(color, 0)
            nums[index : index + freq] = [color] * freq
            index += freq
                    
    
    
nums = [2,1,1,0,1,2]
so = Solution()
# print(so.sortColors(nums))
# print(so.sortColors2(nums))
print(so.sortColors3(nums))