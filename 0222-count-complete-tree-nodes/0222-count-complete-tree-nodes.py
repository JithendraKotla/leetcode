# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        arr=[]
        def post(node):
            if node:
                post(node.left)
                arr.append(node.val)
                post(node.right)
            return arr
        j=post(root)
        return len(j)
        
        