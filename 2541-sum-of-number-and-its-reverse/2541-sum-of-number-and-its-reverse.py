class Solution(object):
    def sumOfNumberAndReverse(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for i in range(num+1):
            if i+int(str(i)[::-1])==num:
                return True
        return False
        