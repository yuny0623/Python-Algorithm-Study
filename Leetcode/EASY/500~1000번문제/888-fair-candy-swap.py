'''
0822 ~ <답지보고 풀음>

코멘트: 
처음에 접근법이 잘못됬음. Time Limit 뜬다. 
'''

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = abs(sum(aliceSizes) - sum(bobSizes)) // 2
        print(diff)
        for i in range(len(aliceSizes)):
            for j in range(len(bobSizes)):
                if abs(aliceSizes[i] - bobSizes[j]) == diff:
                    return [aliceSizes[i], bobSizes[j]]
        