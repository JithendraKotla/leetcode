# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        arr=[]
        cur=head
        while cur:
            arr.append(cur.val)
            cur=cur.next
        arr=sorted(arr)
        dummy=ListNode(0)
        c=dummy
        for i in arr:
            c.next=ListNode(i)
            c=c.next
        return dummy.next
            

        