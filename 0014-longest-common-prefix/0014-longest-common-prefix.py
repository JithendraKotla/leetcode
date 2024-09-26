class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min=float('inf')
        for i in strs:
            if len(i)<min:
                min=len(i)
        k=0
        while k<min:
            for i in strs:
                if i[k]!=strs[0][k]:
                    return i[:k]
            k+=1

        return i[:k]
        
        