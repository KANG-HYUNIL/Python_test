#백준 2206번 벽 부수고 이동하기

#M * N 의 행렬, 0은 이동 가능, 1은 이동 불가


import sys
from collections import deque
sys.setrecursionlimit(10**6)

#N은 세로, M은 가로로
N, M = map(int, input().split())

End_node = [N - 1, M - 1]

Field = [] #배열 초기화
answer = -1 #정답 초기화
Temp_Field = []
Direction = [[1, 0], [-1, 0], [0, 1], [0, -1]] #우, 좌, 상, 하


#배열 입력력
for _ in range(N):
    line = input().strip()  # 한 줄 입력받기
    Temp_Field.append([int(char) for char in line])  # 각 문자를 정수로 변환하여 리스트에 추가

    
#단순 최단 거리는 DFS든 BFS든 상관 없이 처리할 수 있다 
#그런데 중간에 단 하나의 벽을 부수고 이동할 수 있다고? 
#동시에 벽을 부수지 않고 이동하는 경우가 더 최단거리일 수도 있잖아
#그냥 단순하게 모든 벽이 위치한 좌표에 대해 반복문을 돌려서, 그 벽만이 없어졌을 떄의
#최단 경로 연산을 해서 비교해야 하나? 근데 이러면 시간초과 안되려나? 항상 M*N에 추가로 DFS 재귀까지 들어가는데.

#브루트 포스로 벽을 하나 하나 부순 경우는 시간 초과다
#BFS내에서 모든 것을 한 번에 해결해야 함
#또한, 너무 단순하게 BFS를 생각하였다. 
#방문 여부를 문제에서 주어진 행렬 내에 동시에 처리하려고 하였는데, 그러면 문제가 생김
#이전의 경로가 이미 방문한 곳이라고 해서, 다른 경로가 방문하지 못하게 되면 연산에 오류가 생김
#문제 제공 행렬은 진짜 지도로만 사용하고, 방문 여부 및 현재까지의 이동거리는 따로 방문 여부 배열을 통해 관리리
def BFS():

    #[0] * 2 인 이유는, 벽을 부순 경우와 부수지 않은 경우를 구분하기 위함임
    #2차원 배열은 원소로 [0, 0]의 형태를 저장하게 될텐데, 여기서 첫 번째 원소는 벽을 부수지 않았을 때의 최단거리
    #두 번째 원소는 벽을 부쉇을 경우의 최단거리 저장장
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

    deq = deque()
    deq.append((0, 0, 0)) #x, y좌표, 벽 부숨 여부부

    #visited 배열은 3차원 배열로, x, y좌표와 벽 부숨 여부를 기준으로 방문 여부 및 이동 거리를 관리한다
    #초기에 값을 1로 하는 이유는, 시작 지점에서의 이동 거리를 1로 설정하기 위함
    #방문 후에는 단순히 0 혹은 1로 방문 여부를 검증하는 것이 아니라, 그 지점까지 이동하기 위해 필요한 최소한의 이동거리를 기록하게 된다다
    visited[0][0][0] = 1 #각각 x, y 좌표에서 벽 부숨 여부에 따른 이동 거리 계산산


    while len(deq) > 0 :

        #다음 이동할 좌표 및 이동 횟수를 deq에서 꺼내기
        next_node = deq.popleft()
        node_x = next_node[0] #x
        node_y = next_node[1] #y
        is_broken = next_node[2] #벽 부숨 여부

        #최종 지점 도착 여부
        if node_x == M - 1 and node_y == N - 1:
            global answer

            answer = visited[node_y][node_x][is_broken]
            return

        #이동 로직 수행
        for movement in Direction:

            #다음 좌표 계산
            next_x = node_x + movement[0]
            next_y = node_y + movement[1]

            #범위 충돌 검증
            if next_x < 0 or next_y < 0 or next_x >= M or next_y >= N:
                continue
            
            #이동 가능한 곳이라면, 그리고 방문하지 않았다면
            #visited 배열은 그 지점까지의 최소 이동거리를 저장하기에, 그 값이 0이라면 아직 기록되지 않음 즉 방문하지 않음음
            if Temp_Field[next_y][next_x] == 0 and visited[next_y][next_x][is_broken] == 0:
                visited[next_y][next_x][is_broken] = visited[node_y][node_x][is_broken] + 1 #이동거리 연산해서 기록
                deq.append((next_x, next_y, is_broken)) #새로운 지점 deq에 추가
               
            #벽이 있는 곳인데, 아직 벽을 부숴본 적이 없다면면
            elif Temp_Field[next_y][next_x] == 1 and is_broken == 0:
                visited[next_y][next_x][1] = visited[node_y][node_x][is_broken] + 1 #이동거리 연산
                deq.append((next_x, next_y, 1)) #is_broken에 +1 해서, 다른 축으로 연산을 관리하게 함

                
    pass


BFS()
print(answer)