# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        arr=[]
        def inorder(n):
            if n:
                inorder(n.left)
                arr.append(n.val)
                inorder(n.right)
        inorder(root)
        arr.sort()
        mini=float("inf")
        for i in range(len(arr)-1):
            diff=arr[i+1]-arr[i]
            mini=min(mini,diff)
        return mini

        