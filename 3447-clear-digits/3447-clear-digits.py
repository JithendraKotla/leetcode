class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr=[]
        d={0,1,2,3,4,5,6,7,8,9}
        for i in range(len(s)):
            if s[i].isdigit():
                if arr:
                    arr.pop()
            if s[i].isalpha():
                arr.append(s[i])
        return "".join(arr)

        