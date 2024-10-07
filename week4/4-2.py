# 트럭

N = int(input())
suggestion = []

for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(tmp[0]):
        suggestion.append([tmp[2*j+1], tmp[2*j+2], i+1]) # [size, payment, buyer]

M = int(input())
tmp = list(map(int, input().split()))
scenario = []
for i in range(M):
    scenario.append([tmp[i], i+1]) # [target_revenue, target. size]
    
suggestion.sort()
scenario.sort()

revenue = 0
buyer_payment = [0] * (N+1)
scenario_index = 0

for i in range(len(suggestion)):
    size, payment, buyer = suggestion[i]
    
    if buyer_payment[buyer] < payment:
        revenue += (payment - buyer_payment[buyer])
        buyer_payment[buyer] = payment
    
    while (scenario_index < M) and (scenario[scenario_index][0] <= revenue):
        scenario[scenario_index].append(size)
        scenario_index += 1
        
while(scenario_index < M):
    scenario[scenario_index].append(-1)
    scenario_index += 1
        
scenario.sort(key= lambda x:x[1])
for i in range(len(scenario)):
    print(f"{scenario[i][2]} ", end="")
print()