'''
1114 
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        li_nums1 = nums1[:m]
        li_nums2 = nums2[:n]
        print("li_nums1: ",li_nums1)
        print("li_nums2: ",li_nums2)
        
        i = 0 # nums1 
        j = 0 # nums2 
        check_index = 0
        while i < m and j < n:
            if check_index < m + n and li_nums1[i] <= li_nums2[j]:
                nums1[check_index] = li_nums1[i]
                check_index += 1
                i += 1
            elif check_index < m + n and li_nums1[i] > li_nums2[j]:
                nums1[check_index] = li_nums2[j]
                check_index += 1
                j += 1
                
        if i < m:
            while i<m:
                nums1[check_index] = li_nums1[i]
                check_index += 1
                i += 1
        if j < n:
            while j<n:
                nums1[check_index] = li_nums2[j]
                check_index += 1
                j += 1
        

