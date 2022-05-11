'''
1030 ~ 1039 

1번 솔루션 조금 느리네. 
'''
# 1번 솔루션 
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        s3 = s1&s2
        result = []
        for n in s3:
            result.extend([n] * (min(nums1.count(n), nums2.count(n))))
            
        return result

'''
좀더 최적화 못하나? 
'''


