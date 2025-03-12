class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """
        d={}
        items=items1+items2
        for  i in items:
            if i[0] in d:
                d[i[0]]+=i[1]
            else:
                d[i[0]]=i[1]
        
        

        res=[]

        for i in sorted(d):
            res.append([i,d[i]])

        return res
        