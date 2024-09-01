'''
Author: yaojinxi 864554492@qq.com
Date: 2024-09-01 17:37:53
LastEditors: yaojinxi 864554492@qq.com
LastEditTime: 2024-09-01 19:22:20
FilePath: \leetcode\169\majorityElement.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# Initialize hash table
from typing import List  # Import Optional from the typing module
hmap: dict = {}

# Add operation
# Add key-value pair (key, value) to the hash table
hmap[12836] = "Xiao Ha"
hmap[15937] = "Xiao Luo"
hmap[16750] = "Xiao Suan"
hmap[13276] = "Xiao Fa"
hmap[10583] = "Xiao Ya"

# Query operation
# Input key into hash table, get value
name: str = hmap[15937]

# Delete operation
# Delete key-value pair (key, value) from hash table
# print(hmap.pop(10543))

# Traverse hash table
# Traverse key-value pairs key->value
# for key, value in hmap.items():
#     print(key, "->", value)
# # Traverse keys only
# for key in hmap.keys():
#     print(key)
# # Traverse values only
# for value in hmap.values():
#     print(value)
    
nums = [3,2,3]



class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majorMap: dict = {}
        count = 1
        for value in nums:
            if value in majorMap:
                majorMap[value] += 1
            else:
                majorMap[value] = count

        max_value = max(majorMap.values())
        for key, val in majorMap.items():
            if val == max_value:
                return key
    
so = Solution()

print(so.majorityElement(nums))