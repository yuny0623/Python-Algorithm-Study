'''
0610 ~ 

코멘트: 
모르겠네. 헷갈리는 문제. 감은 잡히는데 좀 애매함. 
왤케 어렵죠. 
'''

'''
오답 솔루션: 
'''
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # 재밌는 문제다. 외계인 단어 .. ㅋㅋ 
        for i in range(1, len(words)):
            flag = True
            for c1, c2 in zip(words[i - 1], words[i]): # leetcode, hello 
                print(c1, c2)
                if order.index(c1) > order.index(c2):
                    flag = False
                    break
            if flag == False:
                return False 
            if len(words[i - 1]) > len(words[i]):
                return False 
                
        return True 

'''
정답 솔루션: 

Runtime: 71 ms, faster than 14.01% of Python3 online submissions for Verifying an Alien Dictionary.
Memory Usage: 14.1 MB, less than 38.00% of Python3 online submissions for Verifying an Alien Dictionary.

너무 어거지로 풀었음. 깔끔한 로직을 알아서 푼게 아니라 
예외를 하나씩 잡아가면서 풀었음. 그래서 코드가 길어지고 조건문이 많아짐. 
'''
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # 재밌는 문제다. 외계인 단어 .. ㅋㅋ 
        # 생각보다 안풀리네... 어떻게 풀까용. 
        if len(words) == 1:
            return True
        
        for i in range(1, len(words)):
            is_ordered = False  
            if words[i - 1] == words[i]: # 같은 단어는 정렬이 필요없음. 
                is_ordered = True 
                continue
            count = 0 
            for c1, c2 in zip(words[i - 1], words[i]):
                count += 1 
                print(c1, c2)
                if order.index(c1) < order.index(c2): # 정상적으로 정렬되어있다면 
                    is_ordered = True
                    break 
                elif order.index(c1) == order.index(c2):
                    is_ordered = True
                    continue 
                else:
                    is_ordered = False
                    break
            print("count:{0}".format(count))
            print("is_ordered:{0}".format(is_ordered))
            if is_ordered and len(words[i - 1]) > len(words[i]) and words[i -1][:count] == words[i][:count]:
                return False 

            if is_ordered == False:
                return False
        
        return True 
                
                 
                    
                