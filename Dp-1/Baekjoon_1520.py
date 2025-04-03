#백준 1520번 내리막 길


import sys
from collections import deque
import heapq
sys.setrecursionlimit(10**7)
#그래프와 DP를 결합한 문제? 그냥 그래프 탐색 문제로만 보이는데.
#일반적인 직사각형 2차원 그래프에서, 벽 대신에 고저차를 가만해 이동해야 한다
#그런데 최단 경로가 아니라, 목표 지점에 도달할 수 있는 모든 경우의 수를 출력하는 것이니,
#각 지점에 도달(내리막 길로)할 수 있는 모든 경우의 수를 계산해 더하는 방식으로 문제를 접근하면 될듯


input = sys.stdin.readline

M, N = map(int, input().split()) #세로 M, 가로 N 입력 받기
dp = [[-1 for _ in range(N)] for _ in range(M)] #DP 테이블 초기화, 각 지점에 도달하는 경우의 수 저장
graph = [list(map(int, input().split())) for _ in range(M)] #지도 입력 받기

#상하좌우 이동을 위한 방향벡터
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)] # (x , y)

START_POINT = (0, 0) #시작 지점
END_POINT = (N - 1, M - 1) #목표 지점, 2차원 배열의 인덱스 접근 순서 고려해서, M - 1 = 세로다
 

# BFS로는 풀 수 없는 문제인건가??
# 최단 거리가 아니라, 모든 경우의 수 이므로 사실은 DFS가 더 적합하다고 할 수 있다.
# 억지로 BFS로 풀 거면, 우선순위 큐를 이용해 높이가 높은 부분부터 처리해야 최종 지점
# 중복 도달 시에 연산 오류를 줄일 수 있다 ! 매우 주요한 지점.
def BFS():
    dp[START_POINT[0]][START_POINT[1]] = 1 #시작 지점은 1로 초기화
    que = deque() #다음 이동 지점을 담을 deque 생성
    que.append(START_POINT) #시작 지점을 que에 추가

    while que:

        cur_x, cur_y = que.popleft() #다음 이동 지점을 que에서 꺼내기
        
        cur_height = graph[cur_y][cur_x] #현재 지점의 높이

        for next_dir in dir:

            next_x = cur_x + next_dir[0] #다음 이동 지점의 x좌표
            next_y = cur_y + next_dir[1] #다음 이동 지점의 y좌표

            #범위 초과  판단해서 continue 시키기
            if next_x < 0 or next_x >= N or next_y < 0 or next_y >=  M:
                continue

            #오르막 길 판단해서 continue 시키기
            if graph[next_y][next_x] >= cur_height:
                continue

            # #아직 도달 안한 곳이라면
            # if dp[next_y][next_x] == 0:
            #     dp[next_y][next_x] = dp[cur_y][cur_x] #현재 지점 경우의 수를 그대로 대입

            # elif dp[next_y][next_x]

            # # 다음 이동 지점 경우의 수가 현재 지점 경우의 수 보다 작으면 바로 대입,
            # if dp[next_y][next_x] <= dp[cur_y][cur_x]:
            #     dp[next_y][next_x] = dp[cur_y][cur_x] 
            # # 크면 더해주기?
            # else :
            #     dp[next_y][next_x] += 1

            #이미 목적지인 우측 하단에 도착한 경우에는 que에 넣을 필요가 없음.
            #사실 que에 넣어도 for 문 내에서 오르막 길 이동을 안하기에 로직적인 오류는 생기지 않겠다만,
            #불필요한 루프 하나 더 생기는 것이니 애초에 넣지 않게 처리하자
            if next_x == END_POINT[0] and next_y == END_POINT[1]:
                continue

            que.append((next_x, next_y)) #다음 이동 (x, y) 좌표 추가

#이 참에 DFS로 모든 경우의 수 따지게끔 한 번 풀어보자

#BFS에서는 (0, 0) 에서 특정 지점에 도달하는 경우의 수를 dp에 저장했다면,
# DFS에서는 특정 지점에서 목표 지점까지 도달하는 경우의 수를 dp에 저장해야 한다.
def DFS(cur_x, cur_y):

    #목표 지점에 도달하면, 경우의 수 하나 추가
    if cur_x == END_POINT[0] and cur_y == END_POINT[1]:
        return 1

    #이미 그 지점에 도달한 기록이 있다면, 그 경우의 수 값을 반환환
    if dp[cur_y][cur_x] != -1:
        return dp[cur_y][cur_x] #이미 도달한 경우의 수 반환

    cur_height = graph[cur_y][cur_x] #현재 지점의 높이

    answer = 0

    #방향 이동 시작 
    for next_dir in dir:

        next_x = cur_x + next_dir[0] #다음 이동 지점의 x좌표
        next_y = cur_y + next_dir[1] #다음 이동 지점의 y좌표

        #범위 초과  판단해서 continue 시키기
        if next_x < 0 or next_x >= N or next_y < 0 or next_y >=  M:
            continue

        #오르막 길 판단해서 continue 시키기
        if graph[next_y][next_x] >= cur_height:
            continue

        answer += DFS(next_x, next_y) #다음 이동 지점으로 이동하여 경우의 수 더하기
    
    dp[cur_y][cur_x] = answer #현재 지점의 경우의 수 저장
    return answer #현재 지점의 경우의 수 반환


ans = DFS(START_POINT[0], START_POINT[1]) #DFS 시작
print(ans)
