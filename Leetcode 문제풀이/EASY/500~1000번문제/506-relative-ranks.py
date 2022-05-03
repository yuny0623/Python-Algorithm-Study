'''
0443 ~ 0539 

Runtime: 403 ms, faster than 25.43% of Python3 online submissions for Relative Ranks.
Memory Usage: 14.9 MB, less than 87.99% of Python3 online submissions for Relative Ranks.

코멘트:
근데 이거 너무 길게 짰다. 분명 이것보다 짧게 짤 수 있을텐데... 
'''

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        if len(score) <= 3:
            medal = ["Gold Medal", "Silver Medal", "Bronze Medal"]
            result = [0] * len(score)
            li = sorted(score, reverse = True)
            for i in range(len(score)):
                result[i] = medal[li.index(score[i])]
            return result 
        
        li = sorted(score, reverse=True)
        result = [0] * len(score) 
        g = li[0]
        s = li[1]
        b = li[2]
        for i in range(len(score)):
            if score[i] == g:
                result[i] = "Gold Medal"
            elif score[i] == s:
                result[i] = "Silver Medal"
            elif score[i] == b:
                result[i] = "Bronze Medal"
            else:
                result[i] = str(li.index(score[i]) + 1)
        
        return result 