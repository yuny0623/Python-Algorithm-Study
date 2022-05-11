'''
1258 ~ 0105 

Runtime: 345 ms, faster than 52.29% of Python3 online submissions for Array Partition I.
Memory Usage: 17.3 MB, less than 18.22% of Python3 online submissions for Array Partition I.

팁:
어떻게 하면 최대값이 나올 수 있을까에 대한 대충의 짐작이 없으면 풀기가 힘듬.
방법은 오름차순으로 일단 정렬해주면 1 2 3 4 5 6 7 8 이 된다고 가정했을떄
여기서 pair의 최대값이 나오려면? 대충 큰 숫자가 있는쪽 5 6 7 8 이 숫자들을 낭비해선 안된다는 거임
1 7 이랑 min 해주면 1 이 나오는데 그러면 7이 통째로 낭비되는거나 마찬가지임.
그런데 7 8 min 해주면? 7을 쓸 수 있다. 여기서 8이 낭비되는거 아니냐 하지만 8은 7이랑 1차이밖에 안남
그리고 가장 큰수라 어차피 min 해도 못씀. 
 
'''
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        li = sorted(nums)
        total = 0 # 합 
        pairs = [] 
        
        i = 0
        l = len(li)
        while i < l:
            pairs.append((li[i], li[i + 1]))
            i += 2
        
        for a, b in pairs:
            total += min(a, b)
            
        return total 

