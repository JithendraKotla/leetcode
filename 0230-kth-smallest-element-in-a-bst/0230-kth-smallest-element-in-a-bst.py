# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr=[]
        def ino(node):
            if node:
                ino(node.left)
                arr.append(node.val)
                ino(node.right)
        ino(root)
        return arr[k-1]
                

        