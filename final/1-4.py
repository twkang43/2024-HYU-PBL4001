# [21년 재직자 대회 예선] 회의실 예약
import sys

# main
N,M = map(int, input().split())

rooms = dict()
for _ in range(N):
    room_name = input()
    rooms[room_name] = [i for i in range(9,19)] # 9시 - 18시 중 가능한 시간을 표시

for _ in range(M):
    name, start_time, end_time = input().split()
    start_time, end_time = int(start_time), int(end_time)
    
    for time in range(start_time, end_time): # 예약된 시간을 삭제 [시작시간:종료시간)
        rooms[name].remove(time)

sorted_room_keys = sorted(rooms.keys())
for room in sorted_room_keys:
    print(f"Room {room}:")
    list = rooms[room]
    
    if 0 < len(list) and list[-1] == 18: # 마지막에 남은 18 제거
        list.remove(18)
    
    if len(list) == 0:
        print("Not available")
    else:
        count = 1
        start_time = [list[0]]
        end_time = []
        for i in range(len(list)-1):
            if list[i+1] != list[i]+1:
                count += 1
                end_time.append(list[i]+1)
                start_time.append(list[i+1])
        end_time.append(list[-1]+1)
                
        print(f"{count} avaiable:")
        for i in range(len(end_time)):
            s = start_time[i] if start_time[i] != 9 else '09'
            print(f"{s}-{end_time[i]}")
            
    if room != sorted_room_keys[-1]:
        print("-----")