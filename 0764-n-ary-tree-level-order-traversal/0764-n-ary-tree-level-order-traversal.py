"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        res=[]
        if root is None:
            return

        queue=deque([root])
        

        while queue:
            out=[]
            level_size=len(queue)
            for i in range(level_size):
                node=queue.popleft()
                out.append(node.val)

                if node.children:
                    for j in node.children:
                        queue.append(j)
            res.append(out)
            
            
            

           

        return res


        