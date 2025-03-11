class Solution(object):
    def vowelStrings(self, words, left, right):
        """
        :type words: List[str]
        :type left: int
        :type right: int
        :rtype: int
        """
        d={"a","e","i","o","u"}
        c=0
        for i in range(left,right+1):
            if words[i][0] in d and words[i][-1] in d:
                c+=1
        return c