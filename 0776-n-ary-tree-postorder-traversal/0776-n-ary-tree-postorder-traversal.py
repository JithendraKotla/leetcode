"""
# Definition for a Node.
class Node(object):
	def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return 
        output=[]

        st=[root]

        while st:
            node=st.pop()

            output.append(node.val)

            for i in node.children:
                st.append(i)
        
        return output[::-1]