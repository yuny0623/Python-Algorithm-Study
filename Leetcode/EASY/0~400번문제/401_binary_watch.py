'''
0140 ~ <0617 다시풀기> 0501 ~ 

<답지보고 풀음 >

'''
def readBinaryWatch(self, num):
    return ['%d:%02d' % (h, m)
            for h in range(12) for m in range(60)
            if (bin(h) + bin(m)).count('1') == num]

'''
직접 푼 솔루션 :
Runtime: 40 ms, faster than 75.07% of Python3 online submissions for Binary Watch.
Memory Usage: 13.8 MB, less than 98.36% of Python3 online submissions for Binary Watch.

그냥 풀려면 꽤나 헤맬것같은 문제. 파이썬 언어 차원에서 제공하는걸 활용하면 빠르게 풀 수 있음. 
'''
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        return ['%d:%02d' % (h, m)
               for h in range(12) for m in range(60)
               if (bin(h) + bin(m)).count('1') == turnedOn]
    


