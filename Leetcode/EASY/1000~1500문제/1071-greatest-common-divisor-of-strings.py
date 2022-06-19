'''
1229 ~ 0105 
'''
'''
오답 솔루션: 
'''
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        li = []
        for i in range(1, len(str1) + 1):
            if str1[:i] in str2:
                temp2 = str1[:i]
                temp1 = str2[:i]
                if temp1 != temp2:
                    return ""
                j = 1
                while j < len(str1) and len(temp1) < len(str1):
                    if temp1*j == str1:
                        temp1 = temp1*j 
                        j += 1
                        continue
                    j += 1
                    
                j = 1
                while j < len(str1) and len(temp2) < len(str2):
                    if temp2*j == str2:
                        temp2 = temp2*j 
                        j += 1
                        continue
                    j += 1
                if temp1 == temp2:
                    li.append(temp1)
        print(li)
        return max(li, key= len)


'''
정답 솔루션: 

성능개선 가능할듯? 
'''

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        divisor_li = [] 
        for i in range(1, len(str1) + 1):
            divisor_of_str1 = str1[:i]
            print(divisor_of_str1)
            if len(str1)%len(divisor_of_str1) != 0 or len(str2)%len(divisor_of_str1):
                continue 
            if divisor_of_str1 != str2[:i]:
                return ""
            times_of_str1 = len(str1)//len(divisor_of_str1)
            times_of_str2 = len(str2)//len(divisor_of_str1)
            print(times_of_str1)
            print(times_of_str2)
            if divisor_of_str1*times_of_str1 == str1: # str1의 약수라면
                if divisor_of_str1*times_of_str2 == str2:
                    divisor_li.append(divisor_of_str1)
        
        if len(divisor_li) == 0:
            return ""
        return max(divisor_li, key = len)

'''
개선 솔루션: 
Runtime: 34 ms, faster than 89.06% of Python3 online submissions for Greatest Common Divisor of Strings.
Memory Usage: 14 MB, less than 30.85% of Python3 online submissions for Greatest Common Divisor of Strings.
'''
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        divisors = [] 
        str1_len = len(str1)
        str2_len = len(str2)
        for i in range(1, len(str1) + 1):
            divisor_of_str1 = str1[:i]
            if str1_len%i != 0 or str2_len%i:
                continue 
            if divisor_of_str1 != str2[:i]:
                return ""
            times_of_str1 = str1_len//i
            times_of_str2 = str2_len//i
            if divisor_of_str1*times_of_str1 == str1: # str1의 약수라면
                if divisor_of_str1*times_of_str2 == str2:
                    divisors.append(divisor_of_str1)
        
        return "" if len(divisors) == 0 else max(divisors, key = len)




