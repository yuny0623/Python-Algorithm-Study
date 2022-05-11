'''
0406 ~ 0439 

Runtime: 67 ms, faster than 12.87% of Python3 online submissions for Reverse String II.
Memory Usage: 14.5 MB, less than 5.29% of Python3 online submissions for Reverse String II.

예외 때문에 조금 까다로운 문제 
'''

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # 생각보다 안풀리네 
        # 반쪽짜리 슬라이딩 윈도우로 살살 전진하면 될라나
        if len(s) < k :
            return s[::-1]
        if len(s) < 2*k and len(s) >= k:
            return s[:k][::-1] + s[k:]
        # 100 39 
        result = [] 
        start = 0 
        end = k # 39 
        reverse_flag = True
        while end < len(s):
            print(result)
            print("start:{0}".format(start))
            print("end:{0}".format(end))
            if reverse_flag:
                result.append(s[start:end][::-1])
                start += k
                end += k
                reverse_flag = not reverse_flag
            else:
                result.append(s[start:end])
                start += k
                end += k
                reverse_flag = not reverse_flag 
        print(result)
        if start <= len(s) - 1:
            if reverse_flag:
                result.append(s[start:][::-1])
            else:
                result.append(s[start:])
        
        return ''.join(result)
                
                