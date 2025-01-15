class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """


        left =0
        right=len(height)-1

        res=0

        while left<right:

            cu_area=min(height[left],height[right])*(right-left)

            res=max(res,cu_area)

            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return res
        