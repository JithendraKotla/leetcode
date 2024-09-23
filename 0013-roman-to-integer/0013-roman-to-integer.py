class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numeral_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M": 1000}
        decimal=0
        for i in range(len(s)):
            if(i>0 and numeral_map[s[i]]>numeral_map[s[i-1]]):
                decimal+=numeral_map[s[i]]-2*numeral_map[s[i-1]]
            else:
                decimal+=numeral_map[s[i]]
        return decimal