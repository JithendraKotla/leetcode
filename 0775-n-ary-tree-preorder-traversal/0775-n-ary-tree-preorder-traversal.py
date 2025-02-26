"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        output=[]
        if not root:
            return 

        stack=[root]

        while stack:
            node=stack.pop()

            output.append(node.val)

            for i in reversed(node.children):
                stack.append(i)
        
        return output



        