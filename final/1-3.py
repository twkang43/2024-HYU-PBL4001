# [21년 재직자 대회 예선] 좌석 관리
import sys
input = sys.stdin.readline

def get_nearest_distance(x,y):
    min_distance = sys.maxsize
    
    for location in id_location:
        distance = ((x-location[0])**2 + (y-location[1]**2))**(1/2)
        if(distance < min_distance):
            min_distance = distance
            
    return min_distance

def assign_seat(id):
    distance = 0
    x,y = 0,0
    
    for i in range(1,N+1):
        for j in range(1,M+1):
            if(cafeteria[i][j] or cafeteria[i-1][j] or cafeteria[i+1][j] or cafeteria[i][j-1] or cafeteria[i][j+1]): # 해당 좌석 혹은 상하좌우의 좌석이 이미 선점되었다면 넘어감
                continue
            
            current_distance = get_nearest_distance(i,j)
            if(distance < current_distance):
                distance = current_distance
                x,y = i,j
    
    if(distance == 0 and id_location):
        return False
    
    id_status[id] = 1 # 식사 중으로 표시
    cafeteria[x][y] = True # 자리 할당
    id_location[id] = [x,y] # 자리 할당
    return True

def leave_seat(id,x,y):
    id_status[id] = 2 # 식사 완료로 표시
    cafeteria[x][y] = False # 자리 비우기
    del(id_location[id]) # 자리 비우기

# main
N,M,Q = map(int, input().split())
cafeteria = [[False for _ in range(M+2)] for _ in range(N+2)] # NxM + 상하좌우 padding

id_status = dict() # key: id, value: status (0: 식사 X, 1: 식사 중, 2: 식사 완료)
id_location = dict() # key: id, value: [x,y] (현재 앉은 위치)

for _ in range(Q):
    task = input()
    
    if(task[:2] == "In"): # In
        id = task[3]
        
        if(id_status[id] == 1): # {id} already seated.
            print(f"{id} already seated.")
        elif(id_status[id] == 2): # {id} already ate lunch.
            print(f"{id} already ate lunch.")
        else:
            if(assign_seat() == True): # 배정 성공
                x,y = id_location[id]
                print(f"{id} gets the seat ({x}, {y}).")
            else: # 배정 실패
                print("There are no more seats.")
        
    else: # Out
        id = task[4]
        
        if(id_status[id] == 0): # {id} didn't eat lunch. -> not in 등으로 고치기
            print(f"{id} didn't eat lunch.")
        elif(id_status[id] == 2): # {id} already left seat.
            print(f"{id} already left seat.")
        else: # {id} leaves from the seat ({x},{y}).
            x,y = id_location[id]
            print(f"{id} leaves from the seat ({x}, {y}).")
            leave_seat(id,x,y)