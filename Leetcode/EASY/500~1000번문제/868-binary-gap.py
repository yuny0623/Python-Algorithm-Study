'''
0504 ~ 0524 

Runtime: 43 ms, faster than 48.33% of Python3 online submissions for Binary Gap.
Memory Usage: 13.8 MB, less than 55.23% of Python3 online submissions for Binary Gap.

코멘트: 
방법이 여러개 있는 문제임. 0카운트하면서 전진해도 되고 
1일때만 조건 수행하면서 기억하는 position 초기화해도됨. 
쉬운문제임.
근데 아래 문자로 다루고 있는데 정수로 다루면 좀 더 빠르지 않을까. 
'''
class Solution:
    def binaryGap(self, n: int) -> int:
        li = list(bin(n))[2:]
        if li.count('1') == 1 or li.count('1') == 0:
            return 0 
        longest_dist = 0 
        start_idx = li.index('1')  # 처음 등장하는 1인덱스  # 0 
        for i in range(start_idx + 1, len(li)):
            if li[i] == '1':
                if i - start_idx >= longest_dist:
                    longest_dist = i - start_idx 
                start_idx = i

        return longest_dist 


'''
문자대신 정수로 취급할 경우: 
Runtime: 40 ms, faster than 60.80% of Python3 online submissions for Binary Gap.
Memory Usage: 13.8 MB, less than 55.23% of Python3 online submissions for Binary Gap.

살짝 빨라졌네. 
'''
class Solution:
    def binaryGap(self, n: int) -> int:
        li = list(map(int, bin(n)[2:]))
        if li.count(1) == 1 or li.count(1) == 0:
            return 0 
        print(li)
        longest_dist = 0 
        start_idx = li.index(1)  # 처음 등장하는 1인덱스  # 0 
        for i in range(start_idx + 1, len(li)):
            if li[i] == 1:
                if i - start_idx >= longest_dist:
                    longest_dist = i - start_idx 
                start_idx = i

        return longest_dist 

