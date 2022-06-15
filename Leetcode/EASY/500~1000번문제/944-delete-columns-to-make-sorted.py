'''
0945 ~ 
Runtime: 385 ms, faster than 8.07% of Python3 online submissions for Delete Columns to Make Sorted.
Memory Usage: 14.6 MB, less than 61.83% of Python3 online submissions for Delete Columns to Make Sorted.

코멘트: 
간단한 구현 문제다. 지문 그대로만 코드로 옮기면 되는 문제. 
'''

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # 상당히 간단한 구현 문제임. 
        count = 0 
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if ord(strs[j - 1][i]) > ord(strs[j][i]):
                    count += 1
                    break 
        return count 


