#백준 15683번 감시

#각 카메라의 종료와 위치, 지도의 정보가 주어졌을 때에
# 발생하는 사각 지대의 최소 크기를 계산하는 문제
# 적당한 효율 지점을 찾는게 아닌 최소 크기이며, 카메라의 개수가 최대 8개로 고정되어 있고
# 지도의 크기도 최대 길이가 8이다. 연산 필요 영역이 넓지 않으므로 브루트포스로 단순하게 박치기 시도 해도 될 듯.
# 카메라는 카메라를 통과할 수 있으며, 이미 다른 카메라에 의해 감시된 영역을 추가로 감시한다고 의미가 있지는 않다.
# 그럼 여기서 질문.
# 한 카메라가 자신의 최대 감시 영역을 구해서 표시하였을 때에,
# 그것에 의해 다른 카메라의 최대 감시 영역이 바뀔 가능성이 있는가?
# 즉, 감시 영역의 설정 순서가 최대 감시 영역의 연산에 영향을 끼치는가?
# 왠지 그럴 것 같다. 카메라의 처리 순서가 총 감시 영역에 영향을 끼칠 수 있을 듯.
# 그렇다면, 카메라의 모든 경우의 수를 재귀적으로 전부 처리해야 한다.
# 시간복잡도와 공간복잡도가 다소 우려되는 선택이나, 지도의 크기와 카메라의 수가 제한되어있으니 괜찮을듯.

import sys
from collections import deque
import copy

input = sys.stdin.readline

N, M = map(int, input().split()) #N 세로, M 가로

MAX_LENGTH = max(N, M)

dir = [[0, 1], [1, 0], [0, -1], [-1, 0]] #동, 남, 서, 북 방향

class Camera:
    def __init__(self, row, col, c):
        self.row = row # 행 위치
        self.col = col # 열 위치
        self.c = c #카메라 종류

board =[] #지도

cams = [] #카메라 정보

#지도 정보 입력
for i in range(N):

    new_row = list(map(int, input().split())) #행 정보
    board.append(new_row) #지도에 추가

    for j in range(M):
        if new_row[j] != 0 and new_row[j] != 6: #벽이 아니고 빈 공간이 아니면 -> 즉 카메라일 경우에
            cams.append(Camera(i, j, new_row[j])) #카메라의 행, 열 위치와, 카메라 종류 기입

# camera == Camera 인스턴스
# board == 지도 정보
# check_type == 카메라의 감시 방향을 말한다. 0, 1, 2, 3가 들어갈 수 있다.
# 카메라 종류가 1일 때에는, 0, 1, 2, 3 입력을 통해 특정 방향의 감시 영역을 체크한다.
# 카메라 종류가 2일 때에는, 0, 1 입력을 통해 (좌, 우) 혹은 (상, 하) 의 감시 영역을 체크한다.
def watch(camera, board, check_type):
    #카메라의 위치와 종류를 받아서, 해당 카메라가 감시하는 영역을 체크하는 함수
    #감시 영역은 0으로 체크한다.

    cam = camera.c #카메라 종류
    row = camera.row #카메라 행 위치
    col = camera.col #카메라 열 위치

    if cam == 1: #종류 1인 카메라일 경우에
        
        for j in range(1, MAX_LENGTH): #각 방향으로 계속 진행
            nr = row + dir[check_type][0] * j #행 위치
            nc = col + dir[check_type][1] * j #열 위치

            if nr < 0 or nr >= N or nc < 0 or nc >= M: #범위 초과 시 종료
                break

            if board[nr][nc] == 6: #벽이 있는 경우 종료
                break
            
            if board[nr][nc] == 0: #빈 공간인 경우 감시 영역 체크
                board[nr][nc] = -1 #감시 영역 체크

    elif cam == 2 :

        n_1_hit_wall = False #벽에 부딪혔는지 체크
        n_2_hit_wall = False #벽에 부딪혔는지 체크

        for j in range(1, MAX_LENGTH):

            #2번 카메라는 상하, 좌우 쌍으로만 보면 된다. 그 이외의 요청에 대해서는 break로 무시
            if check_type == 2 or check_type == 3 :
                break

            nr_1 = row + dir[check_type][0] * j #행 위치
            nc_1 = col + dir[check_type][1] * j #열 위치

            nr_2 = row + dir[(check_type + 2) % 4][0] * j
            nc_2 = col + dir[(check_type + 2) % 4][1] * j

            n_1_check = nr_1 < 0 or nr_1 >= N or nc_1 < 0 or nc_1 >= M #범위 초과 시 종료
            n_2_check = nr_2 < 0 or nr_2 >= N or nc_2 < 0 or nc_2 >= M #범위 초과 시 종료

            #양 쪽 방향 모두 범위 초과 시에는 종료
            if n_1_check and n_2_check :
                break

            if n_1_hit_wall and n_2_hit_wall: #양 쪽 방향 모두 벽에 부딪힌 경우 종료
                break
            
            if not n_1_check:
                #한 쪽 방향이 벽 충돌 시 추가 연산 안하게
                if board[nr_1][nc_1] == 6:
                    n_1_hit_wall = True

            if not n_1_hit_wall and not n_1_check: #벽에 부딪히지 않았고, 범위 초과가 아니라면 감시 영역 체크
                if board[nr_1][nc_1] == 0: #빈 공간인 경우 감시 영역 체크
                    board[nr_1][nc_1] = -1 #감시 영역 체크

            if not n_2_check:
                #한 쪽 방향이 벽 충돌 시 추가 연산 안하게
                if board[nr_2][nc_2] == 6:
                    n_2_hit_wall = True
            
            if not n_2_hit_wall and not n_2_check :
                if board[nr_2][nc_2] == 0:
                    board[nr_2][nc_2] = -1

    elif cam == 3:
        n_1_hit_wall = False #벽에 부딪혔는지 체크
        n_2_hit_wall = False #벽에 부딪혔는지 체크

        for j in range(1, MAX_LENGTH):

            nr_1 = row + dir[check_type][0] * j #행 위치
            nc_1 = col + dir[check_type][1] * j #열 위치

            nr_2 = row + dir[(check_type + 1) % 4][0] * j #행 위치
            nc_2 = col + dir[(check_type + 1) % 4][1] * j #열 위치

            n_1_check = nr_1 < 0 or nr_1 >= N or nc_1 < 0 or nc_1 >= M #범위 초과 시 종료
            n_2_check = nr_2 < 0 or nr_2 >= N or nc_2 < 0 or nc_2 >= M #범위 초과 시 종료

            #양 쪽 방향 모두 범위 초과 시에는 종료
            if n_1_check and n_2_check :
                break

            if n_1_hit_wall and n_2_hit_wall: #양 쪽 방향 모두 벽에 부딪힌 경우 종료
                break
            
            if not n_1_check:
                #한 쪽 방향이 벽 충돌 시 추가 연산 안하게
                if board[nr_1][nc_1] == 6:
                    n_1_hit_wall = True

            if not n_1_hit_wall and not n_1_check: #벽에 부딪히지 않았고, 범위 초과가 아니라면 감시 영역 체크
                if board[nr_1][nc_1] == 0: #빈 공간인 경우 감시 영역 체크
                    board[nr_1][nc_1] = -1 #감시 영역 체크
            
            if not n_2_check:
                #한 쪽 방향이 벽 충돌 시 추가 연산 안하게
                if board[nr_2][nc_2] == 6:
                    n_2_hit_wall = True
            
            if not n_2_hit_wall and not n_2_check :
                if board[nr_2][nc_2] == 0:
                    board[nr_2][nc_2] = -1

    elif cam == 4:
        n_1_hit_wall = False #벽에 부딪혔는지 체크
        n_2_hit_wall = False
        n_3_hit_wall = False

        for j in range(1, MAX_LENGTH):

            nr_1 = row + dir[check_type][0] * j #행 위치
            nc_1 = col + dir[check_type][1] * j #열 위치

            nr_2 = row + dir[(check_type + 1) % 4][0] * j #행 위치
            nc_2 = col + dir[(check_type + 1) % 4][1] * j #열 위치

            nr_3 = row + dir[(check_type + 2) % 4][0] * j #행 위치
            nc_3 = col + dir[(check_type + 2) % 4][1] * j #열 위치

            n_1_check = nr_1 < 0 or nr_1 >= N or nc_1 < 0 or nc_1 >= M #범위 초과 시 종료
            n_2_check = nr_2 < 0 or nr_2 >= N or nc_2 < 0 or nc_2 >= M #범위 초과 시 종료
            n_3_check = nr_3 < 0 or nr_3 >= N or nc_3 < 0 or nc_3 >= M

            if n_1_check and n_2_check and n_3_check:
                break

            if n_1_hit_wall and n_2_hit_wall and n_3_hit_wall: #양 쪽 방향 모두 벽에 부딪힌 경우 종료
                break
            
            if not n_1_check:
                #한 쪽 방향이 벽 충돌 시 추가 연산 안하게
                if board[nr_1][nc_1] == 6:
                    n_1_hit_wall = True

            if not n_1_hit_wall and not n_1_check: #벽에 부딪히지 않았고, 범위 초과가 아니라면 감시 영역 체크
                if board[nr_1][nc_1] == 0: #빈 공간인 경우 감시 영역 체크
                    board[nr_1][nc_1] = -1 #감시 영역 체크

            if not n_2_check:
                #한 쪽 방향이 벽 충돌 시 추가 연산 안하게
                if board[nr_2][nc_2] == 6:
                    n_2_hit_wall = True
            
            if not n_2_hit_wall and not n_2_check :
                if board[nr_2][nc_2] == 0:
                    board[nr_2][nc_2] = -1

            if not n_3_check:
                if board[nr_3][nc_3] == 6:
                    n_3_hit_wall = True

            if not n_3_hit_wall and not n_3_check:
                if board[nr_3][nc_3] == 0:
                    board[nr_3][nc_3] = -1            

    elif cam == 5:

        n_1_hit_wall = False #벽에 부딪혔는지 체크
        n_2_hit_wall = False
        n_3_hit_wall = False
        n_4_hit_wall = False

        for j in range(1, MAX_LENGTH):

            if check_type != 0 :
                break

            nr_1 = row + dir[check_type][0] * j #행 위치
            nc_1 = col + dir[check_type][1] * j #열 위치

            nr_2 = row + dir[(check_type + 1) % 4][0] * j #행 위치
            nc_2 = col + dir[(check_type + 1) % 4][1] * j #열 위치

            nr_3 = row + dir[(check_type + 2) % 4][0] * j #행 위치
            nc_3 = col + dir[(check_type + 2) % 4][1] * j #열 위치

            nr_4 = row + dir[(check_type + 3) % 4][0] * j #행 위치
            nc_4 = col + dir[(check_type + 3) % 4][1] * j

            n_1_check = nr_1 < 0 or nr_1 >= N or nc_1 < 0 or nc_1 >= M #범위 초과 시 종료
            n_2_check = nr_2 < 0 or nr_2 >= N or nc_2 < 0 or nc_2 >= M #범위 초과 시 종료
            n_3_check = nr_3 < 0 or nr_3 >= N or nc_3 < 0 or nc_3 >= M
            n_4_check = nr_4 < 0 or nr_4 >= N or nc_4 < 0 or nc_4 >= M

            if n_1_check and n_2_check and n_3_check and n_4_check:
                break
            
            if n_1_hit_wall and n_2_hit_wall and n_3_hit_wall and n_4_hit_wall: #양 쪽 방향 모두 벽에 부딪힌 경우 종료
                break
            
            if not n_1_check:
                #한 쪽 방향이 벽 충돌 시 추가 연산 안하게
                if board[nr_1][nc_1] == 6:
                    n_1_hit_wall = True

            if not n_1_hit_wall and not n_1_check: #벽에 부딪히지 않았고, 범위 초과가 아니라면 감시 영역 체크
                if board[nr_1][nc_1] == 0: #빈 공간인 경우 감시 영역 체크
                    board[nr_1][nc_1] = -1 #감시 영역 체크

            if not n_2_check:
                #한 쪽 방향이 벽 충돌 시 추가 연산 안하게
                if board[nr_2][nc_2] == 6:
                    n_2_hit_wall = True
            
            if not n_2_hit_wall and not n_2_check :
                if board[nr_2][nc_2] == 0:
                    board[nr_2][nc_2] = -1

            if not n_3_check:
                if board[nr_3][nc_3] == 6:
                    n_3_hit_wall = True

            if not n_3_hit_wall and not n_3_check:
                if board[nr_3][nc_3] == 0:
                    board[nr_3][nc_3] = -1     

            if not n_4_check:
                if board[nr_4][nc_4] == 6:
                    n_4_hit_wall = True

            if not n_4_hit_wall and not n_4_check:
                if board[nr_4][nc_4] == 0:
                    board[nr_4][nc_4] = -1       


    return board


INT_MAX = sys.maxsize #최대 정수값
answer = sum(row.count(0) for row in board) #정답 초기화

temp_cams = deque() #
cams_que = deque(cams) #카메라 정보

def recursion(board):

    global answer #정답
    global cams_que #카메라 정보
    global temp_cams #카메라 정보

    if cams_que:
        camera = cams_que.popleft()
        temp_cams.append(camera) #카메라 정보 추가
        c = camera.c



        if c == 1:

            for i in range(4):
                copy_board = copy.deepcopy(board) #보드 복사
                new_copy_board = watch(camera, copy_board, i)
                
                if not cams_que: #모든 카메라를 처리한 경우
                    answer = min(answer, sum(row.count(0) for row in new_copy_board))
                else :
                    recursion(new_copy_board)

        elif c == 2:

            for i in range(2):
                copy_board = copy.deepcopy(board) #보드 복사
                new_copy_board = watch(camera, copy_board, i)
                
                if not cams_que: #모든 카메라를 처리한 경우
                    answer = min(answer, sum(row.count(0) for row in new_copy_board))
                else :
                    recursion(new_copy_board)



        elif c == 3:
                
            for i in range(4):
                copy_board = copy.deepcopy(board) #보드 복사
                new_copy_board = watch(camera, copy_board, i)
                
                if not cams_que: #모든 카메라를 처리한 경우
                    answer = min(answer, sum(row.count(0) for row in new_copy_board))
                else :
                    recursion(new_copy_board)

        elif c == 4:

                
            for i in range(4):
                copy_board = copy.deepcopy(board) #보드 복사
                new_copy_board = watch(camera, copy_board, i)
                
                if not cams_que: #모든 카메라를 처리한 경우
                    answer = min(answer, sum(row.count(0) for row in new_copy_board))
                else :
                    recursion(new_copy_board)
        
        elif c == 5:
            copy_board = copy.deepcopy(board) #보드 복사
            new_copy_board = watch(camera, copy_board, 0)
            
            if not cams_que: #모든 카메라를 처리한 경우
                answer = min(answer, sum(row.count(0) for row in new_copy_board))
            else :
                recursion(new_copy_board)

    if temp_cams:
        cams_que.appendleft(temp_cams.pop())

    return

recursion(board) #재귀 호출
print(answer)

