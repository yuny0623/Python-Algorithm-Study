'''
0534 ~ 0541 
마지막 조건 체크해주세요. 
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # 연속된 1의 최대 길이를 구하세요. 
        count = 0
        max_count = 0 
        for i in range(len(nums)):
            print(nums[i])
            if nums[i] == 1:
                count += 1
                continue 
            elif nums[i] == 0:
                if count >= max_count: # 2 >= 0
                    max_count = count # max_count = 2
                    count = 0           # count = 0
                else:
                    count = 0  

        # 여기서 마지막 조건 체크해줘야함. 
        if count >= max_count:
            max_count = count 
        return max_count 
    
                
        
