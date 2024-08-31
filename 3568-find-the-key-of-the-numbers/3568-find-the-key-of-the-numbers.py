class Solution(object):
    def generateKey(self, num1, num2, num3):
        """
        :type num1: int
        :type num2: int
        :type num3: int
        :rtype: int
        """
        arr=[]
       
        num1s=str(num1)
        num2s=str(num2)
        num3s=str(num3)
        num1p=num1s.zfill(4)
        num2p=num2s.zfill(4)
        num3p=num3s.zfill(4)
        key=""

        for i in range(4):
            key+=str(min(int(num1p[i]),int(num2p[i]),int(num3p[i])))
        return int(key)

        

