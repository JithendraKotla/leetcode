# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root:
            return 

        stack=[(root,root.val)]
       
        c=0

        while stack:
            node,max_so_far=stack.pop()

            if node.val>=max_so_far:
                c+=1
            
            if node.left:
                stack.append([node.left,max(node.val,max_so_far)])
            
            if node.right:
                stack.append([node.right,max(node.val,max_so_far)])
            
        return c