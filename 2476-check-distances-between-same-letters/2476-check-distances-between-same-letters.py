class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: List[int]
        :rtype: bool
        """
        s_list=sorted(list(set(s)))

        d={}
        letter=97

        for i in distance:
            d[chr(letter)]=i
            letter+=1
        


     
        j=0
        for i in range(len(s_list)):
            fir=s.index(s_list[i])
           
            sec=s.index(s_list[i],fir+1)

            diff=sec-fir-1
            if diff!=d[s_list[i]]:
                return False
        return True


           
        