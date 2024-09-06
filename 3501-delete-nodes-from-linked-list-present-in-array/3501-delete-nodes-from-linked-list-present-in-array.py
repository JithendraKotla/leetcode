# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        nums_list=set(nums)
        
        while head is not None and head.val in nums_list:
            head = head.next
        temp=head
        while( temp is not None and temp.next is not None ):
            if (temp.next.val in nums_list ):
                
                temp.next=temp.next.next
            else:
                temp=temp.next
        return head
       

        

        