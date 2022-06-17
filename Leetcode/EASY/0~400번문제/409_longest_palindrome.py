'''
1129 ~ <0614> 0401 ~ 0418 

테스트케이스에서 걸리네. 

https://www.youtube.com/watch?v=a_3XDW9P47E
https://leetcode.com/problems/longest-palindrome/
'''

'''
Runtime: 48 ms, faster than 49.76% of Python3 online submissions for Longest Palindrome.
Memory Usage: 14 MB, less than 20.16% of Python3 online submissions for Longest Palindrome.

정답 솔루션: 
가장 긴 palindrome? 이 어떻게 형성될지에 대해 생각해보면 된다. 그걸 떠올리지 못하면
문제를 풀기가 꽤 까다로움. 참고로 핵심은 홀수번 등장하는 character에 있음. 가장 큰 빈도수인 문자를
더해주고, 이후 나머지 홀수번 등장하는 애들은 -1 만큼한 짝수만큼만 등장하면 되겠지.
'''
from collections import defaultdict 
class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = defaultdict(int)
        #s = list(s)
        for c in s:
            d[c] += 1
        print(d)
        length = 0

        odd_li = [] 
        for k, v in d.items():
            print(length)
            if v%2 == 0:
                length += v
            else:
                odd_li.append(v)
                
        if len(odd_li) == 0:
            return length
        if len(odd_li) == 1:
            return length + odd_li[0]

        odd_li = sorted(odd_li, reverse = True)
        length += odd_li[0]
        for i in range(1, len(odd_li)):
            if odd_li[i] > 0:
                length += (odd_li[i] - 1)
                
        return length 





