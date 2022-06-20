'''
0351 ~ 
'''

'''
오답 솔루션: Time limit Exeede  
이 솔루션이 Time Limit이 뜬다. n^2로 잡아서 그런건데 굳이 N^2로 하지 않고도 
풀 수 있는 방법이 있다. 
'''
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counter = 0
        for i in range(len(dominoes)):
            for j in range(i + 1, len(dominoes)):
                if dominoes[i] == dominoes[j] or dominoes[i] == dominoes[j][::-1]:
                    counter += 1
        return counter

'''
정답 솔루션: 
'''



