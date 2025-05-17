# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        nums=[]
        def ino(node):
            if node:
                ino(node.left)
                nums.append(node.val)
                ino(node.right)
        ino(root)
        nums.sort()
        global i
        i=0
        
        def replace(node):
            global i
            if node:
                replace(node.left)
                node.val=nums[i]
                i+=1
                replace(node.right)
        replace(root)
        
        