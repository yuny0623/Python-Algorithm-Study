from typing import List 
'''
0842 ~ 0905 
이문제는 뭘 요구하는거지? 
문제 자체는 안어려운듯. 
문제에서 표현하는 문장자체가 살짝 헷갈릴 여지가 있음. 걍 읽어보면 됨. 
'''

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        tmp = []
        if len(nums) == 0:
            return [] 
        for i in range(len(nums)):
            if len(tmp) == 0:
                tmp.append(nums[i])
            elif len(tmp) != 0:
                if nums[i] == (tmp[-1] + 1):
                    tmp.append(nums[i])
                else:
                    result.append(tmp)
                    tmp = []
                    tmp.append(nums[i])
        result.append(tmp)
        
        return_list = [] 
        for l in result:
            if len(l) == 1:
                return_list.append(str(l[0]))
            else:
                return_list.append(str(l[0]) + '->' + str(l[-1]))
        return return_list