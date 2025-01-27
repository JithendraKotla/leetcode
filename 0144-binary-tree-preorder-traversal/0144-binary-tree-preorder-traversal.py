# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        arr=[]
        def n(node):
            
            if node:
                arr.append(node.val)
                n(node.left)
                n(node.right)
            return arr
        j=n(root)
        return j
        