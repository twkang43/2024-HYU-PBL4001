# [HSAT 3회 정기 코딩 인증평가 기출] 플레이페어 암호
import sys

key_matrix = [['' for _ in range(5)] for _ in range(5)]

# LL -> LX LO
# XX -> XQ XY
# 마지막 글자 -> 마지막 글자 + X
# X (마지막) -> XX
# HELLOWORLD -> HE LX LO WO RL DX
# XXYYY -> XQ XY YX YX
def parse_message(message):
    parsed = []
    
    i = 0
    while i < len(message):
        if i == len(message)-1: # 마지막 한 문자가 남은 경우
            parsed.append([message[i], 'X'])
            break
        else:
            if message[i] == message[i+1]: # 같은 두 문자가 연속된 경우
                parsed.append([message[i], 'Q' if message[i] == 'X' else 'X'])
                i += 1
            else: # 서로 다른 두 문자가 연속된 경우
                parsed.append([message[i], message[i+1]])
                i += 2
    
    return parsed

# 두 문자가 같은 열 -> 각 문자 오른쪽으로 한 칸 이동
# 두 문자가 같은 행 -> 각 문자 아래로 한 칸 이동
# 두 문자 다른 열 & 행 -> 칸의 열이 서로 교환된 위치에 적힌 글자로 암호화
def find_location(char, key_matrix):
    for i in range(5):
        for j in range(5):
            if key_matrix[i][j] == char:
                return i, j
    
def encrypt_message(parsed, key_matrix):
    result = []
    
    for pair in parsed:
        first, second = pair
        first_x, first_y = find_location(first, key_matrix)
        second_x, second_y = find_location(second, key_matrix)
        
        first_encrypt, second_encrypt = '', ''
        if first_x == second_x: # 두 문자가 같은 행
            first_encrypt = key_matrix[first_x][(first_y+1)%5]
            second_encrypt = key_matrix[second_x][(second_y+1)%5]
        elif first_y == second_y: # 두 문자가 같은 열
            first_encrypt = key_matrix[(first_x+1)%5][first_y]
            second_encrypt = key_matrix[(second_x+1)%5][second_y]
        else: # 두 문자 다른 열 & 행
            first_encrypt = key_matrix[first_x][second_y]
            second_encrypt = key_matrix[second_x][first_y]
    
        result.append(first_encrypt)
        result.append(second_encrypt)
    
    return result

# main
message = input()
keys = list(set(input()))

# 입력받은 keys를 바탕으로 key matrix 구성
for i in range(ord('A'), ord('Z')+1):
    char = chr(i)
    if char not in keys and char != 'J':
        keys.append(char)

for i in range(25):
    key_matrix[i//5][i%5] = keys[i]

# parse the message
parsed = parse_message(message)

# encrypt the message
result = encrypt_message(parsed, key_matrix)
print(''.join(result))