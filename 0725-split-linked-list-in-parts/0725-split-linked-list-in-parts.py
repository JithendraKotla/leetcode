# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        arr=[None]*k
        size=0
        cur=head
        while cur:
            size+=1
            cur=cur.next
        split_size=size//k
        rem=size%k
        cur=head
        for i in range(k):
            arr[i]=cur
            if (rem>0):
                cur_size=(split_size+1)
            else:
                cur_size=split_size
            rem-=1
            for _ in range(cur_size-1):
                if cur:
                    cur=cur.next
            if cur:
                next_par=cur.next
                cur.next=None
                cur=next_par
        return arr


        