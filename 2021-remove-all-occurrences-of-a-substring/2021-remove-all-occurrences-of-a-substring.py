class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        arr=[]
    
        for i in range(0,len(s)):
            arr.append(s[i])
            if len(arr) >= len(part) and "".join(arr[-len(part):]) == part:
                for j in range(len(part)):
                    arr.pop()
            
        return "".join(arr)
            

        
        

        