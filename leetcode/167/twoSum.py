from typing import List
# Step 1:
# I will initialize two pointers, first and last.
# The first pointer will start at index 0, 
# and the last pointer will start at the last index of the array (array length minus 1).

# Step 2:
# Then, I will calculate the sum of the values at these two pointers. 
# If the sum is equal to the target value, 
# I will return the indices of these pointers, 
# each incremented by 1. If the sum is less than the target value, 
# I will move the first pointer to the right (increment by 1). If the sum is greater than the target value, 
# I will move the last pointer to the left (decrement by 1)."

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        last = len(numbers) - 1
        while first < last:
            if numbers[first] + numbers[last] < target:
                first +=1
            
            elif numbers[first] + numbers[last] > target:
                last -= 1
                
            elif numbers[first] + numbers[last] == target:
                return [first + 1, last + 1]

        return []
    
numbers = [2,7,11,15]
target = 9
so = Solution()
result = so.twoSum(numbers, target)

print(result)