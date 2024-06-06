
#7576 토마토(백준) 그래프 탐색 문제

import sys
from collections import deque

#시간복잡도 O(mn) 으로 풀기?

#입력 받기, m은 가로 칸의 수, n은 세로 칸의 수
m, n = list(map(int, sys.stdin.readline().split(sep=" ")))

zero_count = 0 #0, 익지 않은 토마토의 수를 저장할 변수

time_count = 0 #토마토가 전부 익는데 필요한 시간 수를 저장할 변수

Map = [] #토마토 보관 상자 저장할 list

deq = deque() #익어 있는 토마토의 좌표를 저장할 deque

movement = [[1, 0], [-1, 0], [0, 1], [0, -1]] #하, 상, 우, 좌 이동을 표현

#토마토 보관 상자 저장 및 초기 0의 개수 계산
for i in range(n):

    #배열 한 줄 입력 받기
    tomato = list(map(int, sys.stdin.readline().split(sep=" ")))

    for j in range(m):

        if tomato[j] == 0: #익지 않은 토마토 수 계산
            zero_count += 1

        elif tomato[j] == 1: #익은 토마토의 좌표 deque에 저장
            deq.append([i, j])

    Map.append(tomato) #토마토 보관 상자 저장


while True:

    #모든 토마토가 익어 있다면, break
    if zero_count == 0:
        print(time_count)
        break

    Check = False #그 날에 익은 토마토가 있는지 확인하는 bool 변수

    ary = [] #매 상하좌우 이동 후 만나는 익지 않은 토마토의 좌표를 저장할 list

    while len(deq) != 0:

        y_tmt, x_tmt = deq.popleft() #익은 토마토의 좌표 하나 빼오기
        
        Map[y_tmt][x_tmt] = 2 #이미 방문한 익은 토마토를 "2"로 표현

        for i in range(4): #상하좌우 이동 표현

            y_moved = y_tmt + movement[i][0] #이동 후의 y좌표
            x_moved = x_tmt + movement[i][1] #이동 후의 x좌표

            #상자 범위를 초과해서 움직이면, pass
            if x_moved < 0 or y_moved < 0 or x_moved >= m or y_moved >= n:
                pass
                
            #이미 방문한 익은 토마토거나, 토마토가 들어있지 않은 칸이면 pass
            elif Map[y_moved][x_moved] == 2 or Map[y_moved][x_moved] == -1:
                pass
            
            #이동 후 익지 않은 토마토를 만나면
            elif Map[y_moved][x_moved] == 0:

                Map[y_moved][x_moved] = 1 #그 토마토를 익은 토마토로 바꾸기
                ary.append([y_moved, x_moved]) #익은 토마토의 좌표 저장

                zero_count -= 1 #익지 않은 토마토의 개수 -1 
                Check = True #익은 토마토가 있으니 True
        
    #익은 토마토가 있으면, ary에 익은 토마토의 좌표가 존재
    if Check == True:
        
        #deq에 익은 토마토의 좌표 append 하기
        for yx in ary:
            deq.append(yx)

        time_count += 1
    
    #이 루프에 익은 토마토가 없다면, 이미 모든 토마토가 익었거나, 
    #모든 토마토가 익지는 못하는 상황인 것
    elif Check == False:
        
        if zero_count == 0: #모든 토마토가 익었다면, 최소 날짜 출력
            print(time_count)
            break
        
        elif zero_count != 0: #모든 토마토가 익지 못하는 상황이면, -1 출력
            print(-1)
            break

