class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        arr=date.split("-")
        str=""
        for i in arr:
            j=bin(int(i))
            str+=j[2:]
            str+="-"
        return str[:-1]