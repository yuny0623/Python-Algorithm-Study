'''
0822 ~ <답지보고 풀음>

코멘트: 
처음에 접근법이 잘못됬음. Time Limit 뜬다. 
'''
'''
오답 솔루션: 
'''
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = abs(sum(aliceSizes) - sum(bobSizes)) // 2
        print(diff)
        for i in range(len(aliceSizes)):
            for j in range(len(bobSizes)):
                if abs(aliceSizes[i] - bobSizes[j]) == diff:
                    return [aliceSizes[i], bobSizes[j]]
    

'''
오답 솔루션 2:
이렇게 for 문으로 돌았을때 지금 계속 Time limit 이 뜨는걸 보니 아예 접근법이 틀린것 같다. 
수학적으로 접근해야할것 같다.  
'''
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum_a = sum(aliceSizes)
        sum_b = sum(bobSizes)
        result = []
        for i in range(len(aliceSizes)):
            for j in range(len(bobSizes)):
                if (sum_a - aliceSizes[i] + bobSizes[j]) == (sum_b + aliceSizes[i] - bobSizes[j]):
                    result.append(aliceSizes[i])
                    result.append(bobSizes[j])
                    return result 
            

'''
정답 솔루션: 

Runtime: 822 ms, faster than 27.14% of Python3 online submissions for Fair Candy Swap.
Memory Usage: 16.9 MB, less than 6.75% of Python3 online submissions for Fair Candy Swap.
'''
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum_a = sum(aliceSizes)
        sum_b = sum(bobSizes)
        middle = int((sum_b - sum_a)/2)
        aliceSizes = set(aliceSizes)
        bobSizes = set(bobSizes)
        for a in aliceSizes:
            if (a+middle) in bobSizes:
                return [a, a+middle]
            

