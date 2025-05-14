# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c=0
        temp=head
        while (temp):
            c+=1
            temp=temp.next
        index=c-n
        temp=head
        if index==0:
            return head.next
    
        for i in range(index-1):
            temp=temp.next
        temp.next=temp.next.next
        return head


        