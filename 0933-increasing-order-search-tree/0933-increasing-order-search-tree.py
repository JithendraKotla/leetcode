# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        arr=[]
        def post(node):
            
            if node:
                post(node.left)
                
                arr.append(node.val)
                post(node.right)
            return arr
        array=post(root)
        array=sorted(arr)
        dummy=TreeNode(0)
        cur=dummy
        for i in array:
            cur.right=TreeNode(i)
            cur=cur.right
        return dummy.right

        
        
        

        