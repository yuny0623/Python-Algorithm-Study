'''
0553 ~ 0608 
재밌는 문제임. 

마지막 return 에서 왜 duration 더해줄까요? 
가장 마지막 공격타임 이후에도 계속 중독상태가 duration 동안 유지될거니까 
더해줘야 제대로된 값이 나옴. 

개선: 다른사람거보다 좀 많이 느린것 같은데 뭘 바꿔볼까. 

'''
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        li = sorted(timeSeries)
        total = 0 
        for i in range(0, len(li) - 1):
            if li[i + 1] - li[i] >= duration:
                total += duration
            else:
                total += li[i + 1] - li[i]
                
        return total + duration  
        
        




