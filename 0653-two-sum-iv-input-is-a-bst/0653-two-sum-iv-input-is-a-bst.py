# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        arr=[]
        def ino(node):
            if node:
                ino(node.left)
                arr.append(node.val)
                ino(node.right)
        ino(root)
        if len(arr)==1:
            return False

        for i in arr:
            if k-i in arr and k-i!=i:
                return True
        return False
        