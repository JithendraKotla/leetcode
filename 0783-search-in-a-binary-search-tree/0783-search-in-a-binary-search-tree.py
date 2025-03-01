# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def ini(node):
            if node is None:
                return None
            if node.val==val:
                return node
            if node.val>val:
                return ini(node.left)
            return ini(node.right)
        j=ini(root)
        return j
        