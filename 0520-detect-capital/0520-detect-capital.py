class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        c=0
        for i in range(len(word)):
            if word[0].isupper():
                k=0
                for i in range(1,len(word)):
                    if word[i].islower():
                        k+=1
                if k==len(word)-1:
                    return True
        for i in range(len(word)):
            if word[i].isupper():
                c+=1
        if c==len(word):
            return True
        c1=0
        for i in range(len(word)):
            if word[i].islower():
                c1+=1
        if c1==len(word):
            return True
        return False
            

        
        
                    

        