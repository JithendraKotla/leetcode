# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        gcdi=[]
        temp=head
        arr=[]
        
        while(temp):
            arr.append(temp.val)
            temp=temp.next
        if (len(arr)==1):
            return head
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        for i in range(len(arr)-1):
            j=gcd(arr[i],arr[i+1])
            gcdi.append(j)
        res = []
       

        res = []
        for i in range(len(arr) - 1):
            res.append(arr[i])     
            res.append(gcdi[i]) 
        res.append(arr[-1])
        dummy=ListNode(0)
        cur=dummy
        for i in res:
            cur.next=ListNode(i)
            cur=cur.next
        return dummy.next
       
        

        

        