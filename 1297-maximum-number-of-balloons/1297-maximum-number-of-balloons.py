class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        s="balloon"
        s_arr=[i for i in s]
        s_arr_set=set(s_arr)
        d={}
        for i in text:
            if i in s_arr_set:
                if i in d:
                    d[i]+=1
                else:
                    d[i]=1
        ar=[]
        for ch in s_arr_set:
            if ch == "l" or ch == "o":
                ar.append(d.get(ch, 0) // 2)  
            else:
                ar.append(d.get(ch, 0))
        
        return min(ar) if ar else 0