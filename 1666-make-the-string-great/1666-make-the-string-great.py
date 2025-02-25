class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        st=[]
        for i in range(len(s)):
            if st:
                if st[-1].islower() and s[i].isupper():
                    if st[-1]==s[i].lower():
                        st.pop()
                        continue
                elif st[-1].isupper() and s[i].islower():
                    if st[-1]==s[i].upper():
                        st.pop()
                        continue
            
            st.append(s[i])
        return "".join(st)
                

        