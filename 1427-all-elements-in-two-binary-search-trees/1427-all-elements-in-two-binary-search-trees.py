# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        arr=[]
        arr1=[]
        def post(node):
            
            if node:
                post(node.left)
                
                arr.append(node.val)
                post(node.right)
            return arr
        def post1(node):
            
            if node:
                post(node.left)
                
                arr1.append(node.val)
                post(node.right)
            return arr1
        j=post(root1)
        k=post1(root2)
        return sorted(j+k)
        