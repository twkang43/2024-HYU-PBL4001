# [21년 재직자 대회 본선] 트럭
import sys
input = sys.stdin.readline

# main
N = int(input())
offer = [] # [[size, payment, buyer_id]]

for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(tmp[0]):
        offer.append([tmp[2*j+1], tmp[2*j+2], i+1])
        
M = int(input())
scenario = [] # [[target_revenue, target_id]]

tmp = list(map(int, input().split()))
for i in range(M):
    scenario.append([tmp[i], i+1])

offer.sort() # 이중 리스트의 각 리스트의 맨 앞 값 (size)를 바탕으로 sort
scenario.sort() # 이중 리스트의 각 리스트의 맨 앞 값 (target_revenue)를 바탕으로 sort

revenue = 0
scenario_index = 0
buyer_payment = [0 for _ in range(N+1)] # buyer가 현재 지불하고자 하는 금액
for i in range(len(offer)):
    size, payment, buyer_id = offer[i][0], offer[i][1], offer[i][2] # size 기준으로 정렬됨
    
    if buyer_payment[buyer_id] < payment: # buyer가 원래 지불하고자 한 금액보다 현재 payment가 더 큰 경우
        revenue += (payment - buyer_payment[buyer_id]) # 차액만큼 revenue update
        buyer_payment[buyer_id] = payment
        
    while((scenario_index < M) and (scenario[scenario_index][0] <= revenue)): # 현재의 size로 각 target을 만족시키는 경우
        scenario[scenario_index].append(size) # [target_revenue, target_id] -> [target_revenue, target_id, size]
        scenario_index += 1

while(scenario_index < M): # target_revenue를 만족시키지 못한 경우, -1 출력
    scenario[scenario_index].append(-1)
    scenario_index += 1        
        
scenario.sort(key= lambda x:x[1]) # 각 리스트에서 1번쨰 값 (target_id)를 가지고 sort       

for i in range(M):
    print(scenario[i][2], end=" ")
print()