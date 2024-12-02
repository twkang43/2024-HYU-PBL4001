# [21년 재직자 대회 예선] 로드 밸런서 트래픽 예측
import sys
from collections import deque
input = sys.stdin.readline

def topological_sort(dag):
    order = []
    queue = deque()
    
    in_degree = [0 for _ in range(N+1)] # 1 x (N+1)
    for i in range(1,N+1):
        for j in range(len(dag[i])):
            in_degree[dag[i][j]] += 1
    
    for i in range(1,N+1):
        if in_degree[i] == 0:
            queue.append(i)
            
    while queue:
        v = queue.popleft()
        order.append(v)
        
        for neighbor in dag[v]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return order

# main
N,K = map(int, input().split())

dag = [[0]] # 1 x (N+1)
for _ in range(N):
    input_list = list(map(int, input().split()))
    dag.append(input_list[1:]) # r 제외
    
order = topological_sort(dag) # topological sort로 노드 간 순서 정리

result = [0]*(N+1)
result[1] = K # 루트 로드 밸런서

for i in range(N):
    current_node = order[i]
    child_length = len(dag[current_node])

    if 0 < child_length: # 로드 밸런서
        quotient = result[current_node]//child_length
        remainder = result[current_node]%child_length
        
        for j in range(child_length): # 공통적인 방문 횟수
            result[dag[current_node][j]] += quotient
        
        for j in range(remainder): # 추가 방문 횟수
            result[dag[current_node][j]] += 1

for i in range(1,N+1):
    print(result[i], end=" ")
print()