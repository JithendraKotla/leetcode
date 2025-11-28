class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        res=[]

        for i in arr:
            res.append(i)
            if i==0:
                res.append(i)
        sub_res=res[:len(arr)]

        for i in range(len(arr)):
            arr[i]=sub_res[i]
        
            
        