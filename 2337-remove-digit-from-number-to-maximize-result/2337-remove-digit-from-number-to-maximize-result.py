class Solution(object):
    def removeDigit(self, number, digit):
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
       

        arr=[]
        for i,j in enumerate(number):
            if j==digit:
                arr.append(i)
        arr1=[]

        for i in range(len(arr)):
            new_s = number[:arr[i]] + number[arr[i] + 1:]
            arr1.append(new_s)
        arr1=[int(i) for i in arr1]
        return str(max(arr1))
        

            