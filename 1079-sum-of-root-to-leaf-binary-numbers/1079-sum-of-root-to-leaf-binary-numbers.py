# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root,nums=""):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        if root is None:
            return 0
        nums+=str(root.val)
        if root.left is None and root.right is None:
            return int(nums,2)
       
            
        l=self.sumRootToLeaf(root.left,nums)
        r=self.sumRootToLeaf(root.right,nums)
        return l+r
    
        

        