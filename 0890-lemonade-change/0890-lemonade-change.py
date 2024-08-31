class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five_c= 0
        ten_c = 0
        for i in bills:
            if i == 5:
                five_c+=1
            elif i==10:
                
                if five_c>0:
                    five_c-=1
                else:
                    return False
                ten_c+=1
            elif i==20:
                if five_c > 0 and ten_c>0:
                    five_c-=1
                    ten_c-=1
                elif five_c >= 3:
                    five_c -= 3
                else:
                    return False

        return True
            


