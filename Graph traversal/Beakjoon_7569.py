#백준 7569번 토마토
from collections import deque
import sys
import copy

#3차원 행렬 이용해야 함

#가로, 세로, 높이인 M, N, H 
M, N, H = map(int, input().split())

#입력 받기
Field = []
deq = deque() #큐 초기화 [x좌표, y좌표, z좌표] 의 형식으로 저장장


Filed_Count = M * N * H #전체 공간의 개수(우선은 전체 개수로 초기화)
Tomato_Count = 0 #익은 토마토 개수
Blank_Count = 0 #비어 있는 공간의 개수(-1 입력)

time = 0 #시간 초기화

#각각 dx, dy, dz 방향 이동 의미미
Direction = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]  

#z축 루프프
for z in range(H):
    Temp_Field = [] #임시 행렬 초기화

    #y축 루프프
    for y in range(N):
        row = list(map(int, sys.stdin.readline().split())) #입력 받기(2차원)
        Temp_Field.append(row) #입력 받은 행렬을 임시 행렬에 추가

        #x축 루프프
        for x in range(M):
            if row[x] == 1:
                Tomato_Count += 1
                deq.append([x, y, z]) #익은 토마토의 좌표를 큐에 추가

            elif row[x] == -1:
                Blank_Count += 1



    Field.append(Temp_Field) #입력 받은 행렬을 전체 행렬에 추가(3차원)


def BFS():

    global Tomato_Count
    global time
    global deq

    #BFS 전에 이미 모든 토마토가 익어 있다면 아래 로직을 수행할 필요가 없음음
    if Tomato_Count == Filed_Count - Blank_Count:
        return

    while True:

        Temp_deq = deque() #임시 큐 초기화

        #deq의 모든 루프를 순회하고 나면, 그것은 하루가 지났다는 의미다다
        while len(deq) > 0 :

            #다음 이동할 좌표 및 이동 횟수를 deq에서 꺼내기
            next_node = deq.popleft()
            node_x = next_node[0] #x
            node_y = next_node[1] #y
            node_z = next_node[2] #z

            #방향 루프
            for dir in Direction:
                next_x = node_x + dir[0]
                next_y = node_y + dir[1]
                next_z = node_z + dir[2]

                #범위 초과 처리리
                if next_x < 0 or next_x >= M or next_y < 0 or next_y >= N or next_z < 0 or next_z >= H:
                    continue
                
                #인근의 토마토가 익지 않은 것이라면 익은 토마토로 변경
                if Field[next_z][next_y][next_x] == 0:
                    Field[next_z][next_y][next_x] = 1 #익은 토마토로 변경
                    Tomato_Count += 1 #익은 토마토 개수 증가
                    Temp_deq.append([next_x, next_y, next_z]) #큐에 추가

        #Temp_deq가 비어있다면, 더 이상 익힐 수 있는 토마토가 없다는 의미미
        if len(Temp_deq) == 0:
            break

        time += 1 #하루가 지났다는 의미

        #Temp_deq를 deq로 변경
        deq = copy.deepcopy(Temp_deq) 
    
    #모든 처리를 하였어도 익지 않은 토마토가 존재한다면, -1
    if Tomato_Count + Blank_Count < Filed_Count:
        time = -1


BFS()
print(time)





