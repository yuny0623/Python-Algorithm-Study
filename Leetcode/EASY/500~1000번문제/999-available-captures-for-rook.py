'''
0155 ~ <잠시 카페서 놀기ㅋㅋ> ~ 0451 

Runtime: 43 ms, faster than 59.90% of Python3 online submissions for Available Captures for Rook.
Memory Usage: 13.9 MB, less than 82.03% of Python3 online submissions for Available Captures for Rook.

코멘트: 
꽤나 재밌었던 문제. 구현 자체는 어렵지 않음. 문제 제대로 안읽고 풀어서 
처음에 BFS인줄 알고 삽질했음. 문제 잘 읽어보면 BFS, DFS가 아니라 그냥 상하좌우 탐색 문제인걸
알 수 있음. 쉬움. 
'''
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]
        
        rook = None # rook 좌표 
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rook = [i, j]
                    break 
        count = 0
        # 이제 상하좌우에서 살펴보기. 
        for i in range(rook[0], -1, -1): # 상 
            if board[i][rook[1]] == 'p':
                count += 1
                break
            elif board[i][rook[1]] == 'B':
                break 
                
        for i in range(rook[0], 8): # 하
            if board[i][rook[1]] == 'p':
                count += 1
                break
            elif board[i][rook[1]] == 'B':
                break 
                
        for i in range(rook[1], 8): # 우
            if board[rook[0]][i] == 'p':
                count += 1
                break
            elif board[rook[0]][i] == 'B':
                break 
                
        for i in range(rook[1], -1, -1): # 좌 
            if board[rook[0]][i] == 'p':
                count += 1
                break
            elif board[rook[0]][i] == 'B':
                break 
                
        return count 
        
        











