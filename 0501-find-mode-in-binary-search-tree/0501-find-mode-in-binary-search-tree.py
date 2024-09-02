# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        arr=[]
        def post(node):
            if node:
                post(node.right)
                arr.append(node.val)
                post(node.left)
            return arr
        array=post(root)
        d={}
        for i in array:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        d_val=max(d.values())
        res=[]
        for i,j in d.items():
            if j==d_val:
                res.append(i)
        return res


        