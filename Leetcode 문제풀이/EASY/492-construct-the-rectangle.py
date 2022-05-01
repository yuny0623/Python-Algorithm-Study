'''
0543 ~ 0552 

범위가 area // 2 가 아니라 sqrt 로 제곱근으로 잡아줘야함. 왜냐면
우리가 구하고자 하는건 가장 차가 작은 약수 2개 이기 때문임. 
'''
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        # L >= W
        # L-W 는 최소 
        
        # 공약수중에서 가장 차가 적은 쌍을 찾는 문제네요. 
        divide = 0 
        for i in range(1, int(math.sqrt(area)) + 1):
            if area % i == 0:
                divide = i
        
        li = [divide, area//divide]
        return sorted(li, reverse = True)
    
        
        
        
        
        




