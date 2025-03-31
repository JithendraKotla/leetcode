class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        l=0
        r=len(s)-1
        res=[i for i in s]

        while l<r:
            if ord(s[l])<ord(s[r]):
                res[l]=s[l]
                res[r]=s[l]
            elif ord(s[l])>ord(s[r]):
                res[l]=s[r]
                res[r]=s[r]
            l+=1
            r-=1
        return "".join(res)

    

        