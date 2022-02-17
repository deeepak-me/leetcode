Two pointer method:


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i= 0
        j=0
    
        while i<len(s) and j<len(t):
        
            if s[i] ==t[j]:
                i+=1
            j+=1
        
        if(i==len(s)):
            return (True)
        else:
            return False
            
            
Method 2


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        p=0
        
        for char in t:
            if(p==len(s)):
                break
                
            if(s[p]==char):
                p+=1
        
        return p == len(s)
