# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q=deque()
        q.append(root)
        res=[]
        while q:
            len_q=len(q)
            r=[]
            for i in range(len_q):
                node=q.popleft()
                if node:
                    r.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(r)
        return res[-1][0]

        