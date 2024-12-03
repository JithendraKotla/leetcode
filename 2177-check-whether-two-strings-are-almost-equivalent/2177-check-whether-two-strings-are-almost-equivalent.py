class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        d1={}
        d2={}
        s1=set(word1)
        s2=set(word2)
        for i in word1:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1
        for i in word2:
            if i in d2:
                d2[i]+=1
            else:
                d2[i]=1
        c1=0
        for i in s1:
            if i in s2:
                if abs(d1[i]-d2[i])<=3:
                    c1+=1
            if i not in s2:
                if d1[i]<=3:
                    c1+=1
        c2=0
        for i in s2:
            if i in s1:
                if abs(d1[i]-d2[i])<=3:
                    c2+=1
            if i not in s1:
                if d2[i]<=3:
                    c2+=1
        if(c1==len(s1) and c2==len(s2)):
            return True
        else:
            return False
        
        
        