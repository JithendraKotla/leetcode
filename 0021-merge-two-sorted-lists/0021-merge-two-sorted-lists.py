# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp1=list1
        arr=[]
        while (temp1):
            arr.append(temp1.val)
            temp1=temp1.next
        temp2=list2
        while (temp2):
            arr.append(temp2.val)
            temp2=temp2.next
        arr=sorted(arr)
        dummy=ListNode(0)
        cur=dummy
        for i in arr:
            cur.next=ListNode(i)
            cur=cur.next
        return dummy.next
        
       