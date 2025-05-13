# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def createbst(arr):
            if not arr:
                return None
            mid = len(arr)//2
            root=TreeNode(arr[mid])
            root.left=createbst(arr[:mid])
            root.right=createbst(arr[mid+1:])
            return root
        return createbst(nums)

       

