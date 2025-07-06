class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def firsto(arr,n,target):
            low=0
            high=n-1
            first=-1

            while (low<=high):
                mid=(low+high)//2
                if (arr[mid]==target):
                    first=mid
                    high=mid-1
                elif arr[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
                    
            return first
        def lasto(arr,n,target):
            low=0
            high=n-1
            last=-1

            while (low<=high):
                mid=(low+high)//2
                if (arr[mid]==target):
                    last=mid
                    low=mid+1
                elif arr[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return last
        f=firsto(nums,len(nums),target)
        if f==-1:
            return [-1,-1]
        else:
            return [f,lasto(nums,len(nums),target)]
        
                


        

        

        