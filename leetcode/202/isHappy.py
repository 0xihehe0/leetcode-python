class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()  # This set will store the sums we have encountered
        
        while n != 1 and n not in seen:
            seen.add(n)  # Add the current number to the set
            n = self.sum_of_squares(n)  # Update n to the sum of the squares of its digits
        
        return n == 1
    
    def sum_of_squares(self, num: int) -> int:
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total
    
so =  Solution()
n = 46
print(so.isHappy(n))