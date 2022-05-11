'''
0841 ~ 0914 

좋은문제네. 근데 어려웡 

팁1:
문제 설명 그대로 전부다 구현하면 되는 문제임.
함정없고 그냥 구현만 하면 끝. 다만 키패드 위치와 관련해서는 조금 생각해볼 필요 있음. 
'''
def solution(numbers, hand):
    left_push = [1, 4, 7] # 무조건 왼손 push 
    right_push = [3, 6, 9] # 무조건 오른손 push 
    
    middle_push = [2 ,5, 8, 0] # 중간 패드 
    middle_dict = {2:0, 5:1, 8:2, 0:3}
    
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    left_pos = [3, 0] # 첫 왼손 위치
    right_pos = [3, 2] # 첫 오른손 위치 
    
    result = [] 
    for n in numbers:
        left_dist = 0
        right_dist = 0 
        if n in left_push:
            left_pos[0] = left_push.index(n)
            left_pos[1] = 0
            result.append('L')
            continue
        if n in right_push:
            right_pos[0] = right_push.index(n)
            right_pos[1] = 2 
            result.append('R')
            continue
        if n in middle_push: # 중간 키패드 누를 경우 
            left_dist = abs(left_pos[0] - middle_dict[n]) + abs(left_pos[1] - 1) # 왼손 수직거리 + 수평거리 
            right_dist = abs(right_pos[0] - middle_dict[n]) + abs(right_pos[1] - 1) # 오른손 수직거리 + 수평거리 
            if left_dist>right_dist:
                right_pos[0] = middle_dict[n]
                right_pos[1] = 1
                result.append('R')
            elif left_dist < right_dist:
                left_pos[0] = middle_dict[n]
                left_pos[1] = 1
                result.append('L')
            else:    # 거리가 같다면 
                if hand == 'left':
                    left_pos[0] = middle_dict[n]
                    left_pos[1] = 1
                    result.append('L')
                else:
                    right_pos[0] = middle_dict[n]
                    right_pos[1] = 1
                    result.append('R')
                
    return ''.join(result) 