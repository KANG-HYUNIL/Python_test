#백준 14503번 로봇 청소기

import sys

input = sys.stdin.readline

#주의, 가장 왼쪽 위는 (0, 0)이고, 가장 오른쪽 아래는 (N - 1, M - 1) 이다

#북, 동, 남, 서 방향 표시 숫자들
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

MOVE_TO_RIGHT = (0, 1) #동쪽, 오른쪽으로 이동
MOVE_TO_LEFT = (0, -1) # 서쪽, 왼쪽으로 이동
MOVE_TO_UP = (-1, 0) #북쪽, 위로 이동
MOVE_TO_DOWN = (1, 0) #남쪽, 아래로 이동

#전진 용 이동 좌표
MOVE_TO_FRONT = [MOVE_TO_UP, MOVE_TO_RIGHT, MOVE_TO_DOWN, MOVE_TO_LEFT] #북, 동, 남, 서 방향으로 이동하는 좌표들

#후진 용 이동 좌표
MOVE_TO_BACK = [MOVE_TO_DOWN, MOVE_TO_LEFT, MOVE_TO_UP, MOVE_TO_RIGHT] #남, 서, 북, 동 방향으로 이동하는 좌표들

N, M = map(int, input().split()) #행, 열
cur_row, cur_col, cur_dir = map(int, input().split()) #현재 위치와 방향 


board = [list(map(int, input().split())) for _ in range(N)] #맵
visited = [[0] * M for _ in range(N)] #방문 여부 체크 리스트, 필요한가? 맵에서 청소 완료 구역을 -1 등으로 따로 표시하면 안되나?

answer = 0 #청소한 구역 수
# board[cur_row][cur_col] = -1 #현재 위치 청소 완료 표시


while True:

    #1번 행동, 현재 칸의 청소 여부 체크 및 청소 시도
    if (board[cur_row][cur_col] == 0):
        board[cur_row][cur_col] = -1 #청소 완료 표시
        answer += 1 #청소한 구역 수 증가
    
    has_cleanable_area = False #청소 가능한 구역이 있는지 체크하는 변수

    #2, 3번 분기 위한 체크, 주변 4칸(상하좌우 의미하는 듯) 중 청소되지 않은 빈 칸이 있는지 검증
    for dir in MOVE_TO_FRONT:
        next_row = cur_row + dir[0]
        next_col = cur_col + dir[1]

        #범위 여부 체크
        if next_row < 0 or next_row >= N or next_col < 0 or next_col >= M:
            continue
        
        #상하좌우 중에 청소 가능한 구역이 있으면
        if board[next_row][next_col] == 0 :
            has_cleanable_area = True #체크
            break #탈출, 4 방향 중 하나라도 존재하면 조건 만족함
    
    #2번 행동
    if not has_cleanable_area:

        #바라보는 방향 유지하며 한 칸 후진
        next_row = cur_row + MOVE_TO_BACK[cur_dir][0]
        next_col = cur_col + MOVE_TO_BACK[cur_dir][1]

        #범위 여부 체크
        if next_row < 0 or next_row >= N or next_col < 0 or next_col >= M:
            break

        #벽 충돌 체크
        if board[next_row][next_col] == 1:
            break
        
        #한 칸 후진한 좌표로 갱신
        cur_row = next_row
        cur_col = next_col

        continue #다시 1번으로
    
    #3번 행동
    else:

        #반시계 방향 90도 회전 실행
        cur_dir = (cur_dir - 1) % 4 #방향 회전

        #바라보는 방향 기준, 앞 칸이 청소되지 않은 빈 칸인지 검증
        next_row = cur_row + MOVE_TO_FRONT[cur_dir][0]
        next_col = cur_col + MOVE_TO_FRONT[cur_dir][1]

        if board[next_row][next_col] == 0:
            #청소되지 않은 빈 칸이면 그 칸으로 이동
            cur_row = next_row
            cur_col = next_col
        
        continue


print(answer)
# print(board)

# 11 10
# 7 4 0

# 1 1 1 1 1 1 1 1 1 1
# 1 2 2 2 2 2 2 2 2 1
# 1 2 2 2 1 1 1 1 2 1
# 1 2 2 1 1 2 2 2 2 1
# 1 2 1 1 2 2 2 2 0 1
# 1 2 2 2 2 2 2 2 2 1
# 1 2 2 2 2 2 0 1 2 1
# 1 2 2 2 2 2 1 1 2 1
# 1 2 2 2 2 2 1 1 2 1
# 1 2 2 2 2 2 2 2 2 1
# 1 1 1 1 1 1 1 1 1 1
