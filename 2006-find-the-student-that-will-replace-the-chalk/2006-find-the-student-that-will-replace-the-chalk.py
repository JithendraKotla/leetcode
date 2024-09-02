class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        i = 0
        k%=sum(chalk)
        while k >= 0:
            for i in range(len(chalk)):
                if k >= chalk[i]:
                    k -= chalk[i]
                else:
                    return i
        return -1

        