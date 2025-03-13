class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        c=0
        vowel=set("aeiou")
        for i in range(len(word)-5+1):
            for j in range(i+5,len(word)+1):
                if set(word[i:j])==vowel:
                    c+=1
        return c
        