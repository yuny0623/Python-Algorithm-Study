'''
0930 ~ 0935 
Runtime: 217 ms, faster than 66.78% of Python3 online submissions for Shift 2D Grid.
Memory Usage: 14.6 MB, less than 6.42% of Python3 online submissions for Shift 2D Grid.

코멘트: 
이 문제는 자료구조를 활용하지 않으면 삽질할 가능성이 있음. 
큐, 스택 -> 리스트로 쓰거나 해야함. 직접 이동시키려고 하면 시간이 오래걸릴듯 

근데 지금 코드 자체가 너무 장황한데 이걸 좀 간단하게 만들 수 있을까? 
'''

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # 0928 ~ 
        # 이 문제는 자료구조를 적극 활용해야 쉬울것 같은 문제다. 
        m = len(grid)
        n = len(grid[0])
        
        flat_grid = [] 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                flat_grid.append(grid[i][j])
        print(flat_grid)
        for i in range(k):
            val = flat_grid.pop()
            flat_grid.insert(0,val)
        print(flat_grid)
        result = [] 
        start = 0 
        end = n 
        for i in range(0, m):
            result.append(flat_grid[start:end])
            end += n
            start += n
        
        return result 
            

'''
조금 줄인 솔루션: 
'''
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # 0928 ~ 
        m = len(grid)
        n = len(grid[0])
        flat_grid = [x for li in grid for x in li] 
        for i in range(k):
            flat_grid.insert(0,flat_grid.pop())
            
        result = [] 
        start = 0 
        end = n 
        for i in range(0, m):
            result.append(flat_grid[start:end])
            end += n
            start += n
        return result 
            
        
        
            
        
            