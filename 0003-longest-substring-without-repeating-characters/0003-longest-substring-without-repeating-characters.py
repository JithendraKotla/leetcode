class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:  
        mpp=[-1]*256
        left=0
        right=0

        n=len(s)
        maxLen=0
        while right<n:
            if mpp[ord(s[right])]!=-1:
                if left<=mpp[ord(s[right])]:
                    left=mpp[ord(s[right])]+1
            mpp[ord(s[right])]=right

            maxLen=max(maxLen,right-left+1)
            right+=1
        return maxLen        