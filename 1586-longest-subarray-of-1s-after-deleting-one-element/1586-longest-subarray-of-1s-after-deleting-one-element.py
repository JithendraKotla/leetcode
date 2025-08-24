class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i=0
        j=0
        n=len(nums)
        cntzero=0
        maxi=0

        while i<n:
            if nums[i]==0:
                cntzero+=1
            while cntzero>1:
                
                if nums[j]==0:
                    cntzero-=1
                j+=1
            maxi=max(maxi,i-j+1)
            i+=1
        return maxi-1
                


        