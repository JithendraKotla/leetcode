# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        res=[]
        if not root:
            return res
        q=deque()
        q.append(root)
        while q:
            sub=[]
            len_q=len(q)
            for i in range(len_q):
                node=q.popleft()
                if node:
                    sub.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right) 
            res.append(sub)
        return res       