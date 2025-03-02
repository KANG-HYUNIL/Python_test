#백준 3190번 뱀 자료구조 문제
#머리가 꺾은 뒤에, 몸은 꺾은 위치에 도달하기 전까지는 기존 이동을 유지해야 한다
#기존 방향의 이동을 유지하다가, 머리가 꺾은 지점에 도달해서야 꼬리도 꺾게 될 것이다다



from os import error
import sys
import copy
from collections import deque #deque 쓰기 위해

RIGHT = [1, 0]
LEFT = [-1, 0]
UP = [0, 1]
DOWN = [0, -1]

START_POINT = [0, 0]
cur_head = [0, 0]
cur_tail = [0, 0]
cur_direction = [1, 0] # 현재 이동 방향, + 면 우측 혹은 상단 - 면 좌측 혹은 하단단


time = 0

N = int(input()) #보드의 크기
K = int(input()) #사과의 개수

apple_list = [] #사과의 위치를 저장할 리스트
movement_list = [] #뱀의 방향 변환 정보를 저장할 리스트
corner_list = [] #뱀의 꺾인 지점을 저장할 리스트, 어느 지점에서, 어느 방향으로, 어느 시간에 회전을 시도하는지 차례로 기록되어 있음음

for i in range(K) :

    X, Y = map(int, input().split()) #사과의 위치
    apple_list.append([X - 1, Y - 1]) #사과의 위치를 리스트에 저장

L = int(input()) #뱀의 방향 변환 횟수

for i in range(L):

    X, C = input().split() #뱀의 방향 변환 정보
    movement_list.append([int(X), C]) #뱀의 방향 변환 정보를 리스트에 저장

    cur_head[0] += cur_direction[0] * int(X)
    cur_head[1] += cur_direction[1] * int(X)

    corner_list.append([copy.deepcopy(cur_head), copy.deepcopy(cur_direction), int(X)]) #뱀의 꺾인 지점을 리스트에 저장

    if C == 'L' :
        if cur_direction == RIGHT :
            cur_direction = copy.deepcopy(DOWN)
        elif cur_direction == LEFT :
            cur_direction = copy.deepcopy(UP)
        elif cur_direction == UP :
            cur_direction = copy.deepcopy(RIGHT)
        elif cur_direction == DOWN :
            cur_direction = copy.deepcopy(LEFT)

    if C == 'D' :
        if cur_direction == RIGHT :
            cur_direction = copy.deepcopy(UP)
        elif cur_direction == LEFT :
            cur_direction = copy.deepcopy(DOWN)
        elif cur_direction == UP :
            cur_direction = copy.deepcopy(LEFT)
        elif cur_direction == DOWN :
            cur_direction = copy.deepcopy(RIGHT)

cur_head = [0, 0]
cur_tail = [0, 0]
cur_direction = [1, 0] # 현재 이동 방향, + 면 우측 혹은 상단 - 면 좌측 혹은 하단단
time = 0
tail_direction = [1, 0]
#실 소요 시간 연산 로직    

while True :
    error = False
    time += 1

    #머리 먼저 이동
    cur_head[0] += cur_direction[0]
    cur_head[1] += cur_direction[1]

    #머리가 보드 밖으로 나가면 게임 종료
    if cur_head[0] < 0 or cur_head[0] >= N or cur_head[1] < 0 or cur_head[1] >= N :
        error = True
        break

    #머리가 몸과 부딪혔는지 검증하는 로직직
    #꼬리에서 시작하여서, 현재 시간과 비교하여 꺾임 지점 포인트와 포인트의 사이(몸통이겠지)
    #사이 안에 머리가 위치하는지를 검증해야 함. 만약에 위치하면 게임 종료
    for i in range(len(corner_list)) :

        #꺾인 지점의 시간이 현재 시간보다 크면 검증할 필요가 없음
        if time < corner_list[i][2] :
            break

        #꺾는 시간과 현재 시간이 같다면, 이동 방향을 변경
        if time == corner_list[i][2] :
            cur_direction = corner_list[i][1]

        #현재 시간이 꺾는 시간보다 더 지났다면, 위치 비교를 통해 충돌 여부 검증증
        if time > corner_list[i][2]:


            pass

     #꺾인 지점의 시간이 현재 시간보다 작다면, 충돌 검증을 진행해야 함

    apple = False

    #사과와 머리의 충돌 판정, 충돌 시에 사과를 제거하고 꼬리는 이동을 시키지 말아야 함
    for i in range(len(apple_list)) :

        if cur_head == apple_list[i] :
            apple_list.pop(i)
            apple = True
            break

    #사과가 없다면 꼬리 이동
    if apple == False :
        #꼬리의 이동 방향은, 현재 time과 꺾는 방향 리스트를 대조하여 얻어내야 함
        #또한 꼬리의 이동 방향을 변경하는 로직을 리스트와 비교하여 얻어내야 함
        #마지막으로 꼬리가 이동 후 꺾는 지점에 도달하였다면, 꼬리 이동 방향 변경 및 꺾는 포인트 제거 필요


        pass

    #에러 검증 시에 게임 종료
    if(error):
        break



print(time) #게임이 종료되는 시간 출력    






