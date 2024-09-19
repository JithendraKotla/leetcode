# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def mini(node):
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return 1
            if node.left is None:
                return mini(node.right)+1
            if node.right is None:
                return mini(node.left)+1
            
            l=mini(node.left)
            f=mini(node.right)
            return min(l,f)+1
        j=mini(root)
        return j