# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes=0
        temp=head
        while temp:
            temp=temp.next
            nodes+=1
        middle = nodes//2
        temp=head
        if nodes==1:
            return None
        if nodes==2:
            head.next=None
            return head
        for i in range(middle-1):
            temp=temp.next
        temp.next=temp.next.next
        return head


        