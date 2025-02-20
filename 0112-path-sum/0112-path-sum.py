# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        def check(node,targetsum,cur):
            if not node:
                return False
            cur+=node.val
            if (targetsum==cur) and (node.left is None and node.right is None) :
                return True
            
            
            
            
            
            l=check(node.left,targetsum,cur)
            r=check(node.right,targetsum,cur)

            return l or r
        cur=0
        k=check(root,targetSum,cur)
        return k
            

        