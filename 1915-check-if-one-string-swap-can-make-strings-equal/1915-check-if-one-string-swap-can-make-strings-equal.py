class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1)!=len(s2):
            return False
        else:
            arr=[]
            c=0
            for  i in range(len(s2)):
                if s1[i]!=s2[i]:
                    c+=1
                    arr.append(i)
            if c==0:
                return True
            if len(arr) == 2:
                i, j = arr
                return s1[i] == s2[j] and s1[j] == s2[i]

            return False
                
        