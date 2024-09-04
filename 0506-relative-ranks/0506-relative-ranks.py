class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        score_des=sorted(score,reverse=True)
        for i,j in enumerate(score):
            k=score_des.index(j)
            if k==0:
                score[i]="Gold Medal"
            elif k==1:
                score[i]="Silver Medal"
            elif k==2:
                score[i]="Bronze Medal"
            else:
                score[i]=str(k+1)
        return score


        