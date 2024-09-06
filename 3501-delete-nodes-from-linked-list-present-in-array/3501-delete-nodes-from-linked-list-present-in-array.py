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
        ans=ListNode(0)
        ans.next=head
        prev,cur=ans,head
        
        if not head:
            return None
        while cur:
            if cur.val in nums_list:
                prev.next=cur.next
            else:
                prev=cur
            cur=cur.next
        return ans.next

        

        