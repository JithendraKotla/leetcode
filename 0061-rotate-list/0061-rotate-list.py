# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        arr=[]
        cur=head
        while cur:
            arr.append(cur.val)
            cur=cur.next
        if k<0:
            return head
        if len(arr)==0:
            return None
        
        k=k%len(arr)
        res=arr[len(arr)-k:]+arr[:len(arr)-k]
        dummy=ListNode(0)
        c=dummy
        for i in res:
            c.next=ListNode(i)
            c=c.next
        return dummy.next
        