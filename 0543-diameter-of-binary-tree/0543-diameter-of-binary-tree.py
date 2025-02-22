# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recdia(self,n,res):

        if n is None:
            return 0
        
        l=self.recdia(n.left,res)
        r=self.recdia(n.right,res)
        
        res[0]=max(res[0],l+r)

        return 1+max(l,r)

    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res=[0]

        j=self.recdia(root,res)
        return res[0]

        