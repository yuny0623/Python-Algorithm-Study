# 0149 
# for문에서 요소를 뽑아줄때 거기서 정렬을 시키고
# 그리고 난 다음에 i를 뽑아줘야 작은것부터 정렬시킬 수 있다. 
# 그런데 사실 defaultdict를 쓰지 않고 그냥 list를 사용해서
# 정렬하는 것도 좋은 방법이다. 
import sys
input = sys.stdin.readline # 이게 있는거랑 없는거랑 차이가 상당히 크다. 

N, M, V = map(int, input().split())
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
g = [[] for i in range(N + 1)] # 지금 값이 들어오는 범위는 1<= 이다. 즉 1부터 시작이므로 인덱스 1부터 쓰기 위해서는 +1 값으로 세팅해준다. 

for _ in range(M):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)
    # 그리고 반드시 양방향으로 해줘야 한다. 
    # 안그러면 틀림. 

for i in g:
    i.sort(reverse = True) # 왜 오름차순정렬해줄까? 이부분이 상당히 흥미롭다.   
                           # stack에 넣어주기 위해서 오름차순해주는건데, 
                        #    지금 DFS함수를 보면 stack += g[v1]라는 코드가 있다. 
                        #    즉 요소를 쫙 넣어주는데 스택은 마지막에 있는 요소부터 즉 스택 탑을 의미함. -> 거기서 결국엔 꺼내게 될거다.
                        #    근데 작은 요소부터 먼저 정렬하고 싶다고 했으므로
                        #    꺼냈을때 스택탑에 작은 요소가 있어야 한다.
                        #    그렇게 하려면? 여기서 reverse = True를 세팅해서 오름차순으로 잡아놔야하는거다. 

def DFS():
    d_visit = []
    stack = [V]
    d_check = [0 for i in range(N + 1)]
    while stack:
        v1 = stack.pop()
        if not d_check[v1]:
            d_check[v1] = 1
            d_visit.append(v1)
            stack += g[v1]  # 이부분 주의 
    return d_visit

def BFS():
    b_visit = []
    queue = [V]
    b_check = [0 for i in range(N + 1)]
    b_check[V] = 1
    while queue:
        v2 = queue.pop()
        b_visit.append(v2)
        for i in reversed(g[v2]): # 왜 reversed일까? 큐의 경우 앞에서부터 뺀다. 즉 앞에가 작은 수가 있어야 한다. 
                                  # 아까 위에서 오름차순 정렬했으므로 여기서는 뽑을때 작은 요소부터 뽑아야하므로 다시 reversed하면 된다. 
            if not b_check[i]:
                b_check[i] = 1
                queue = [i] + queue # 사실 재귀를 사용하지 않으니 append를 사용할 필요가 없다. 그냥 + 만 해줘도 재귀가 아니라서 문제 없다. 
                                    # 만약 재귀로 구현한다면 각 호출이 동일한 리스트를 써야하므로 +를 할 경우 독립적인 리스트가 될 수 있다. 그러니 지금은 문제 없다. 
    return b_visit

print(' '.join(map(str, DFS())))
print(' '.join(map(str, BFS())))


'''
꽤 재밌는 문제였다. defaultdict를 정렬해서 해결하려고 했는데, 
그냥 요소뽑을때 거기서 정렬해줘도 충분하다. 
그나저나 defaultdict는 왜 제대로 정렬이 안되지? 

--> 문제 최신화했음. 

'''