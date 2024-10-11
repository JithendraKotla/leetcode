# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        arr=[]
        cur=head
        while cur:
          
            arr.append(cur.val)
            cur=cur.next
        dummy=ListNode(0)

        c=dummy
        if not arr:
            return None
        for i in arr:
            if arr.count(i)==1:
                c.next=ListNode(i)
                c=c.next
        return dummy.next

        