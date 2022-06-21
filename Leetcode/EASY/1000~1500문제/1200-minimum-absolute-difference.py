'''
1248 ~ <답지보고풀음>

코멘트:
Time limit exceeded 발생함. 어려운 문제가 아닌데 그냥 헤맸다. 문제가 잘 안풀리는듯 
해답은 정렬에 있다. 
'''

'''
Time limit 발생한 오답 솔루션: 
'''
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        minimum_diff = 1e9 
        
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i == j:
                    continue
                minimum_diff = min(minimum_diff, abs(arr[i] - arr[j]))
        
        diff_pairs = [] 
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if abs(arr[i] - arr[j]) == minimum_diff:
                    diff_pairs.append([arr[i], arr[j]])
        
        return diff_pairs
    

'''
정답 솔루션: 
Runtime: 373 ms, faster than 88.35% of Python3 online submissions for Minimum Absolute Difference.
Memory Usage: 28.6 MB, less than 85.13% of Python3 online submissions for Minimum Absolute Difference.

위 코드처럼 굳이 for 문으로 전부 돌면서 가장 작은 차이를 구할 필요 없다.
그냥 정렬하면 된다. 정렬하면 가장 가까운애들끼리 정렬되니 인접한 애들끼리의 차가 가장 작은 diff 이다. 

'''
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        minimum_diff =  1e9 
        diff_pairs = []
        for i in range(1,len(arr)):
            if abs(arr[i - 1] - arr[i]) < minimum_diff:
                minimum_diff = abs(arr[i - 1] - arr[i])
        for i in range(1, len(arr)):
            if abs(arr[i -1] - arr[i]) == minimum_diff:
                diff_pairs.append([arr[i - 1], arr[i]])
        
        return diff_pairs



