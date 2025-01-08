class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def isPrefix(k,l):
           
            if (k==l[:len(k)]) and l[-len(k):]==k:
                    return True
            
        c=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if(isPrefix(words[i],words[j])):
                    c+=1
        return c
