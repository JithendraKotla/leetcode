# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dep(node):
            if node is None:
                return 0
            lefti=dep(node.left)
            righti=dep(node.right)
            return max(lefti,righti)+1
        j=dep(root)
        return j
        