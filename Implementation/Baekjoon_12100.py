#백준 12100번 2048(Easy) 


#자주 풀던 그래프, dp, 자료구조와는 관계 없는 구현 및 백트래킹 문제
#문제 자체는 직관적이다, 새 블럭 추가가 없는 2048 게임에서, 최댓값 구하는 문제
#이동은 상하좌우로만 가능하다.
#또한 최대 5번만 이동 한정해서 값을 구하는 것이니, 구하는 경우의 수가 그렇게 많지 않다
#단순하게 모든 경우의 수를 시도하는 브루트 포스 통해서도 접근 가능할 듯.
#다만 보드의 크기가 최대 20인 것이 걸린다
#또한, 동일한 수를 만났을 때에 합치는 것 까지는 쉬우나,
#이미 한 번 합쳐져 만들어진 수를 그 이동 대에서는 다시 안합쳐지게 처리하는 것 도 꽤나 귀찮아보인다.

import sys
import copy
input = sys.stdin.readline

N = list(map(int, input().split()))[0] #보드의 크기

MAX_MOVE = 5 #최대 이동 횟수
ZERO = 0 #0은 빈칸을 의미

graph = []

answer = 0

#게임판 입력 받기
for _ in range(N):

    row = list(map(int, input().split())) #행 입력
    answer = max(answer, max(row)) #초기값 설정
    graph.append(row)

#각각 우, 좌, 하, 상 이동 의미
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] 


#기초 작업은 끝났다. 또한 단순 상하좌우 이동은 이제 될거다.
#그럼 여기서 문제. 한 번 합쳐져 만들어진 수를 그 이동대에서는 어떻게 다시 안 합쳐지게 할 것인가?
#합치려고 할 때에, 마치 방문 여부 배열을 사용하듯, 이미 합쳐진 수가 위치하는 곳을 표시한다면?
#이동 방향 쪽의 블록이 먼저 합쳐진다고 하였으니, 이동 방향 쪽에 가장 가까운 행(열) 부터 이동 로직을 수행하고,
#다른 블럭과 부딪혔을 때에 숫자가 동일하며, 그 자리에 있는 블럭이 그 이동에서 합쳐진 블럭이 아니라면, 합쳐진 블럭으로 표시한다.

def move(board, move_count, max_value, dir):

    move_count += 1 #이동 횟수 증가

    #최대 이동 횟수 초과 시에 바로 반환
    if move_count > MAX_MOVE:

        return max_value

    sum_check = [[False] * N for _ in range(N)] #합쳐진 블럭 표시

    # print(str(move_count) + " : 원본 ------------------")
    # print(board)
    # print(" ------------------")


    #우 이동
    if dir == directions[0]:

        for j in range(N):

            for i in range(N):

                cur_i = i #현재 행
                cur_j = N - 1 - j #현재 열

                board = calculate(cur_i=cur_i, cur_j=cur_j, dir=dir, board=board, sum_check=sum_check) #이동 연산

    #좌 이동
    if dir == directions[1]:

        for j in range(N):

            for i in range(N):

                cur_i = i #현재 행
                cur_j = j #현재 열

                board = calculate(cur_i=cur_i, cur_j=cur_j, dir=dir, board=board, sum_check=sum_check) #이동 연산

    #하 이동
    if dir == directions[2]:

        #가장 위의 행부터, 행으로 먼저 접근
        for i in range(N):

            #열을 먼저 접근
            for j in range(N):

                cur_i = N - 1 - i #현재 행
                cur_j = j #현재 열

                board = calculate(cur_i=cur_i, cur_j=cur_j, dir=dir, board=board, sum_check=sum_check) #이동 연산

    #상 이동
    if dir == directions[3]:

        #가장 위의 행부터, 행으로 먼저 접근
        for i in range(N):

            #열을 먼저 접근
            for j in range(N):

                cur_i = i #현재 행
                cur_j = j #현재 열

                board = calculate(cur_i=cur_i, cur_j=cur_j, dir=dir, board=board, sum_check=sum_check) #이동 연산
    

    # print(dir)
    # print(str(move_count) + " : 후 ------------------")
    # print(board)
    # print(" ------------------")

    #최댓값 구하기
    temp_max = max(max(row) for row in board)
    temp_max = max(max_value, temp_max)

    right_move = move(copy.deepcopy(board), move_count, temp_max, directions[0]) #우 이동
    left_move = move(copy.deepcopy(board), move_count, temp_max, directions[1]) #좌 이동
    top_move = move(copy.deepcopy(board), move_count, temp_max, directions[2]) #상 이동
    bottom_move = move(copy.deepcopy(board), move_count, temp_max, directions[3]) #하 이동

    max_value = max(temp_max, right_move, left_move, top_move, bottom_move) #최댓값 갱신

    return max_value


#실 이동 및 합산 연산
def calculate(cur_i, cur_j, dir, board, sum_check):

    #현재 위치가 0이면, 이동 수행 필요가 없음. 바로 return
    if board[cur_i][cur_j] == ZERO:
        return board

    while True:

        #다음 이동 위치
        next_i = cur_i + dir[0]
        next_j = cur_j + dir[1]

        #일단 외곽 처리 먼저 하자
        if next_i < 0 or next_i >= N or next_j < 0 or next_j >= N:
            break

        #다음 이동 위치가 0이라면, 0과 현재 위치의 숫자를 교체해야 한다(이동 효과)
        if board[next_i][next_j] == ZERO:

            board[next_i][next_j] = board[cur_i][cur_j]
            board[cur_i][cur_j] = ZERO

            #현재 행, 열 위치 바꿔서 이동 효과 내기
            cur_i = next_i
            cur_j = next_j

            continue #다음 루프로

        #다음 이동 위치의 수가 현재 수와 같으며
        if board[next_i][next_j] == board[cur_i][cur_j]:

            #다른 이동 연산에 의해 이미 합쳐진 블록의 위치라면 
            #이 블록은 합쳐지지 않고, 더 이상 이동하지 않을 것이다
            if sum_check[next_i][next_j]:
                break

            #아직 합쳐진 적이 없는 블록이라면, 합치고 표시하기
            board[next_i][next_j] *= 2 #판에 들어있는 것은 2배수 들이니, *2로 처리해도 됨
            board[cur_i][cur_j] = ZERO #현재 위치는 빈칸으로 처리
            sum_check[next_i][next_j] = True #합쳐진 블록 표시

            #블럭 합산 연산을 했다는 건, 더 이상 이동의 필요가 없는 건가?
            break
        
        #다음 이동 숫자가 0도 아니고, 자신과 같은 숫자도 아니면, 더 이상 이동 못하므로 break
        else :
            break

    return board


answer = max(max(row) for row in graph) # 이동 전의 최댓값 미리 구하기
move_count = 0 #이동 횟수

#좌, 우, 상, 하 이동에 대한 최댓값 구하기
for i in range(4):

    answer = max(answer, move(copy.deepcopy(graph), move_count, answer, directions[i]))

print(answer)

