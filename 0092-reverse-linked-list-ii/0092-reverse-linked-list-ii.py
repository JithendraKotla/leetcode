# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        c=0
        cur=head
        arr=[]
        while(cur):
            arr.append(cur.val)
            cur=cur.next
        temp=arr[left-1:right]
        sol=temp[::-1]
        arr_m=arr[:left-1]+sol+arr[right:]
        dummy=ListNode(0)
        cur=dummy
        for i in arr_m:
            cur.next=ListNode(i)
            cur=cur.next
        return dummy.next
            
            
            

            
        