'''
0723 ~ <답지보고 풀음> ~ 0905 

코멘트: 
흠... 
투포인터...? 슬라이딩 윈도우...? 뭐로 풀까? <- 둘다 아님. 
'''

'''
오답 솔루션: 
투포인터로 풀려고 했지만 실패  
느낌상 슬라이딩 윈도우가 더 쉬울것 같음. 사이즈가 가변적인 슬라이딩 윈도우 ... 
'''
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        # 처음 보는 유형이다. 문제 자체가 되게 신박하다. 근데 느낌에 투포인터 응용같은데
        # 투 포인터가 아니라 쓰리포인터를 써야할까? ->  투포인터로 그냥 풀어도 될듯. 
        for i in range(1, len(arr) - 2):
            first_sum = sum(arr[:i])
            middle_sum = 0 
            j = i + 1 
            while j < len(arr) - 1:
                middle_sum = sum(arr[i:j])
                if middle_sum == first_sum:
                    break
                j += 1
            middle_sum = sum(arr[i:j])
            last_sum = sum(arr[j:])
            print(first_sum, middle_sum, last_sum)
            if first_sum == middle_sum == last_sum:
                return True
            else:
                continue 
            
        return False 
                
        
'''
슬라이딩 윈도우 오답  솔루션: 
'''
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        for i in range(1, len(arr) - 2): # 슬라이딩 윈도우 사이즈 
            for j in range(1, len(arr) - 1 - i):
                first_sum = sum(arr[:j])
                window = sum(arr[j:j + i])
                last_sum = sum(arr[j + i:])
                if first_sum == window == last_sum:
                    return True
        return False 
                 
'''
슬라이딩 윈도우 오답 솔루션2: 
'''                  
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
    
        for i in range(1, len(arr) - 1): # 슬라이딩 윈도우 사이즈 
            print("window_size: {0}".format(i))
            for j in range(1, len(arr) - 1 - i):
                print(i, j)
                first_sum = sum(arr[:j])
                window = sum(arr[j:j + i])
                last_sum = sum(arr[j + i:])
                print("sums: {0},{1},{2}".format(first_sum, window, last_sum))
                if first_sum == window == last_sum:
                    return True
        return False 
                 

'''
정답 솔루션: 

Runtime: 549 ms, faster than 23.14% of Python3 online submissions for Partition Array Into Three Parts With Equal Sum.
Memory Usage: 21.1 MB, less than 37.19% of Python3 online submissions for Partition Array Into Three Parts With Equal Sum.

코멘트: 
지금 count == 2 로 체크하고 있는게 살짝 가독성에 좋아보이진 않음. <- 이거 수정해보자. 
'''     
        
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        if sum(arr) % 3 != 0:
            return False 
        target = sum(arr)//3 
        
        count = 0 
        accum = 0 
        for num in arr:
            if count == 2:
                return True 
            
            accum += num
            if accum == target:
                count += 1
                accum = 0
        return False 
            
'''
개선한 솔루션: 
Runtime: 574 ms, faster than 18.67% of Python3 online submissions for Partition Array Into Three Parts With Equal Sum.
Memory Usage: 21 MB, less than 81.32% of Python3 online submissions for Partition Array Into Three Parts With Equal Sum.

많은거 바꿔줄 필요없음. 그냥 count 검사하는 if guard만 아래쪽으로 내려버리면 해결됨. 
3으로 count 체크하는걸로 바꿀 수 있음. 
'''
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        if sum(arr) % 3 != 0:
            return False 
        target = sum(arr)//3 
        
        count = 0 
        accum = 0 
        for num in arr:
            accum += num
            if accum == target:
                count += 1
                accum = 0
            if count == 3:
                return True 
        return False 
            
                
        
                
        