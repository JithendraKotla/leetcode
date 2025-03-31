# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l=1
        r=1
        temp=head

        while l<k and temp:
            temp=temp.next
            l+=1
        val1=temp.val
        temp2=head
        c=1
        while temp2:
            temp2=temp2.next
            c+=1
        right=c-k
        temp3=head
        while r<right and temp3:
            temp3=temp3.next
            r+=1
        temp.val,temp3.val=temp3.val,temp.val
        return head
        

        