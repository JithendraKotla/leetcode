class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d={}
        for i,char in enumerate(s):
            d[char]=i
        
        end=0
        start=0
        res=[]
        
        for i,char in enumerate(s):
            end=max(end,d[char])

            if i==end:
                res.append(end-start+1)
                start=i+1
        return res

        