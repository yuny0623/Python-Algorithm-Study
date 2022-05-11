'''
0611 ~ 0821 

너무느림. 
181 ms 걸림
코드 줄일 수 있을까. 
'''

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [] 
        for i in range(len(nums1)):
            if nums1[i] not in nums2:
                result.append(-1)
                continue
            else: 
                index = nums2.index(nums1[i])
                if index == len(nums2) - 1:
                    result.append(-1)
                elif index < len(nums2) - 1:    
                    s = nums2[index + 1:]
                    j = 0
                    while j < len(s):
                        if s[j] > nums1[i]:
                            result.append(s[j])
                            break 
                        j += 1
                    if j == len(s):
                        result.append(-1)
                else:
                    result.append(-1)
                    
        return result 


