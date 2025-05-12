# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        arr=[]
        temp=head
        while temp:
            arr.append(temp.val)
            temp=temp.next
        l=0
        r=len(arr)-1
        temp1=head
        while l<r:
            temp1.val=arr[l]
            temp1=temp1.next
            temp1.val=arr[r]
            temp1=temp1.next
            l+=1
            r-=1
        if l==r and temp1:
            temp1.val=arr[l]

        return head
