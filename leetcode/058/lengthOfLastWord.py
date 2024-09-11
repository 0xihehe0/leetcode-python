class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        type = False
        index = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                type = True
                
            if s[i] == " " and index > 0:
                return index
            
            if type == True:
                index +=1
        
        return index
     
s = "   fly me   to   the moon  "
so = Solution()
result = so.lengthOfLastWord(s)
print(result)