class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five_count = 0
        ten_count = 0

        for i in bills:
            if i == 5:
                five_count += 1
            elif i == 10:
                if five_count == 0:
                    return False
                five_count -= 1
                ten_count += 1
            elif i == 20:
                if ten_count > 0 and five_count > 0:
                    ten_count -= 1
                    five_count -= 1
                elif five_count >= 3:
                    five_count -= 3
                else:
                    return False

        return True

