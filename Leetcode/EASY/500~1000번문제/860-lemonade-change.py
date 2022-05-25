'''
0420 ~ <답지보고풀음> 0445 

Runtime: 1139 ms, faster than 38.48% of Python3 online submissions for Lemonade Change.
Memory Usage: 17.8 MB, less than 87.79% of Python3 online submissions for Lemonade Change.

코멘트: 
너무 어렵게 풀었다. 생각보다 쉬운 문제였음. 시간 너무 소모함.  
처음에 heapq 로 풀려고 했는데 완전히 틀린 접근이었음. 거스름돈처럼 
빼서 합계나 갯수 등등 풀어내는거 변수 사용해서 푸는 쪽이 좀더 맞는듯. 
'''
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for b in bills:
            if b == 5:
                five += 1
            elif b == 10:
                five -= 1
                ten += 1
            elif ten > 0:
                ten -= 1
                five -= 1
            else:
                five -= 3
            if five < 0:
                return False
        return True
    
        
                
                
        



