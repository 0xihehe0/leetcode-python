class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ''.join(char.lower() for char in s if char.isalnum())
        frist = 0
        last = len(result) - 1
        
        while frist < last:
            if(result[frist] != result[last]):
                return False
            frist += 1
            last -= 1
        return True

so = Solution()
s = " "
result = so.isPalindrome(s)
print(result)