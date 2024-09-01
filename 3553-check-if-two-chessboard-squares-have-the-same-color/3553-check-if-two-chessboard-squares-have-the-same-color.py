class Solution(object):
    def checkTwoChessboards(self, coordinate1, coordinate2):
        """
        :type coordinate1: str
        :type coordinate2: str
        :rtype: bool
        """
        arr1=["a","c","e","g"]
        arr2=["b","d","f","h"]
        
        def word(co):
            if co[0] in  arr1:
                if int(co[1])%2!=0:
                    return "black"
            if co[0] in arr2:
                if int(co[1])%2==0:
                    return "black"
            return "white"
        i=word(coordinate1)
        j=word(coordinate2)
        if i==j:
            return True
        return False
