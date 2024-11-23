# [HSAT 6회 정기 코딩 인증평가 기출] 출퇴근길
import sys
sys.setrecursionlimit(10**6) # recursion 제한 풀기

def dfs(current_node, current_adj, visit):
    if visit[current_node] == True:
        return

    visit[current_node] = True
    for node in current_adj[current_node]:
        dfs(node, current_adj, visit)

# main
n,m = map(int, input().split())
adj = [[] for _ in range(n+1)] # index: 1-n
adj_reverse = [[] for _ in range(n+1)] # 방향이 바뀐 그래프

for _ in range(m):
    x,y = map(int, input().split())
    adj[x].append(y)
    adj_reverse[y].append(x)
s,t = map(int, input().split())

from_s = [False]*(n+1)
from_s[t] = True # from: 목적지에 도달하면 더 탐색하지 않도록 목적지 노드를 미리 방문 처리
dfs(s, adj, from_s) # s에서 나가는 엣지들에 대한 dfs

from_t = [False]*(n+1)
from_t[s] = True 
dfs(t, adj, from_t) # t에서 나가는 엣지들에 대한 dfs

to_s = [False]*(n+1)
dfs(s, adj_reverse, to_s) # s로 들어오는 엣지들에 대한 dfs

to_t = [False]*(n+1)
dfs(t, adj_reverse, to_t) # t로 들어오는 엣지들에 대한 dfs

answer = 0
for i in range(1,n+1):
    if from_s[i] and from_t[i] and to_s[i] and to_t[i]:
        answer += 1
answer -= 2 # answer: s와 t도 방문 가능한 노드로 카운트 -> 해당 노드들은 빼주기
print(answer)