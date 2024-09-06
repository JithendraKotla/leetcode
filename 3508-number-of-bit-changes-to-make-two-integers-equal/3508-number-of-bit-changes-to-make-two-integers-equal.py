class Solution(object):
    def minChanges(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        n_bin=bin(n)[2:]
        k_bin=bin(k)[2:]
        c=0
        max_len = max(len(n_bin), len(k_bin))
        n_bin = n_bin.zfill(max_len) 
        k_bin = k_bin.zfill(max_len)  

        for i in range(len(n_bin)):
            if n_bin[i] == '1':  
                if k_bin[i] == '0': 
                    c+=1
            elif n_bin[i] == '0' and k_bin[i] == '1':
                
                return -1
        return c

        