class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res=[0]*(len(nums)-k+1)

        for j in range(len(nums)-k+1):
            sub=nums[j:j+k]
            re=0
            d={}
            for i in sub:
                if i in  d:
                    d[i]+=1
                else:
                    d[i]=1
            sorted_items = sorted(d.items(), key=lambda item: (-item[1], -item[0]))

     

            
            for  l in range(min(x,len(sorted_items))):
                re+=(sorted_items[l][0]*d[sorted_items[l][0]])
            res[j]=re
        return res

        