from typing import List

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