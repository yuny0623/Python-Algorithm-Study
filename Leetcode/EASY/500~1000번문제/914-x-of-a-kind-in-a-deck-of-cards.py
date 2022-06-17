'''
1119 ~ 
'''

'''
오답 솔루션: 
예외 케이스를 확인하고 나서야 이렇게 접근하는것이 아님을 확인함. 
아예 로직이 틀림. 
'''
from collections import defaultdict
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) == 1:
            return False 
        
        d = defaultdict(int)
        for card in deck:
            d[card] += 1
        print(d)
        
        first_value = 0
        first_flag = False
        for k, v in d.items():
            print(first_value, v, first_flag)
            if first_flag == False:
                first_value = v 
                first_flag = True
                continue
            if v != first_value:
                print("exit v, first_value :{0},{1}".format(v, first_value))
                return False
        return True 
    
'''
정답 솔루션: 
Runtime: 328 ms, faster than 5.20% of Python3 online submissions for X of a Kind in a Deck of Cards.
Memory Usage: 14.5 MB, less than 8.26% of Python3 online submissions for X of a Kind in a Deck of Cards.

전체 deck 의 빈도수의 최대공약수를 찾아서 그룹으로 나눌 수 있는지를 체크하는 방식으로 풀었다.
위의 오답 솔루션과는 전혀 다른 접근법을 취했다. 그런데 좀 불필요한 코드가 많은것 같다. 
'''
from collections import defaultdict
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        # 최소 공약수로 나눠지는지에 대한 문제다. 
        if len(deck) == 1:
            return False 
        
        d = defaultdict(int)
        for card in deck:
            d[card] += 1
        print("d:{0}".format(d))
        min_val = min(d.values())
        max_val = max(d.values())
        print("min_val:{0}".format(min_val))

        if min_val < 2:
            return False 
        
        common_divisor = 0
        while True:
            count = 0 
            for val in d.values():
                if val% max_val != 0:
                    break 
                count += 1
            if count == len(d.values()):
                common_divisor = max_val
                break 
            max_val -= 1
        if common_divisor < 2:
            return False 
        print("common_divisor:{0}".format(common_divisor))
        for val in d.values():
            if val%common_divisor == 0:
                continue
            else:
                return False 
        return True 
            
        
                


