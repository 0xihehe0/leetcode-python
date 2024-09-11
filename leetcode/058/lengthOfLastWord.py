# "First of all, we decide to iterate through 
# the input string from the end. If the current character is a space, we skip it. 
# If it's not a space, we set a Boolean flag to True. 
# As long as the Boolean flag is True, 
# we increment the index value in each iteration until we encounter the next space. 
# Finally, we calculate the total index and return it."

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        foundWord = False
        index = 0
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                foundWord = True
                index += 1
            elif foundWord:
                return index
        
        return index

     
s = "   fly me   to   the moon  "
so = Solution()
result = so.lengthOfLastWord(s)
print(result)