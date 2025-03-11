class Solution(object):
    def findValidPair(self, s):
        """
        :type s: str
        :rtype: str
        """
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        for i in range(len(s)-1):
            first=s[i]
            second=s[i+1]

            if int(first)==d[first] and int(second)==d[second] and int(first)!=int(second):
                return s[i]+s[i+1]
        return ""
        