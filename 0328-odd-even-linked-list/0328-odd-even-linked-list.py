# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur=head
        arr=[]
        while cur:
            arr.append(cur.val)
            cur=cur.next
        n=len(arr)
        dummy=ListNode(0)
        c=dummy
        for i in range(0,n,2):
            c.next=ListNode(arr[i])
            c=c.next
        for i in range(1,n,2):
            c.next=ListNode(arr[i])
            c=c.next
        return dummy.next


        