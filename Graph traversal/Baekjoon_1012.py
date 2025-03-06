#백준 1012번 유기농 배추
#그래프 내에서 인접(상 하 좌 우)해 있는 배추들끼리 그룹으로 묶어, 그룹의 수를 구해야 한다
#비슷한 문제를 이전에 풀어보았으나, 세부적인 로직은 기억이 나지 않는다다


import sys
sys.setrecursionlimit(10**6)


#TestCase 수
TestCase = int(input())

#배추밭 배열
Field = []
temp = []
answer = 0

M, N, K = 0, 0, 0

#배추 탐색 시작 위치를 얻었을 때에, 인근(상 하 좌 우)의 위치에 배추들이 있는지 확인 후 변환
def DFS(x, y):

    #좌표 범위를 벗어나면 바로 return 해서 연산 중단시키기
    if x < 0 or y < 0 or x >= M or y >= N:
        return

    #배추가 위치하지 않은 위치라면 연산하지 않기
    if Field[y][x] == 0:
        return
    
    Field[y][x] = 0 #위의 return을 거치지 않았다면, 배추가 위치한 것이기에 1을 0으로 변경
    
    
    DFS(x + 1, y) #우측으로 이동
    DFS(x - 1, y) #좌측으로 이동
    DFS(x, y + 1) #아래로 이동
    DFS(x, y - 1) #위로 이동


    pass


for i in range(TestCase):

    #배추밭의 가로, 세로, 배추 수 입력
    M, N, K = map(int, input().split())

    #가로 길이 M, 세로 길이 N에 맞추어서 배열 초기화화
    Field = [[0] * M for _ in range(N)] 
    temp = [] #배추 위치 배열 초기화
    answer = 0 #정답 초기화화

    #배추 위치 입력 처리
    for j in range(K):
        x, y = map(int, sys.stdin.readline().split())
        Field[y][x] = 1 #y축이 첫 인덱스로 가는 것을 주의
        temp.append(([x, y])) #[x, y]의 형태로 배추 위치들 저장장


    #배추밭 묶음 개수 출력
    for node in temp:

        nodeX, nodeY = node[0], node[1]

        #배추가 위치할 것으로 예상되는 위치가, 이미 DFS로 인해 0으로 처리된 상태면
        #로직 처리하지 않고 continue로 스킵
        if Field[nodeY][nodeX] == 0:
            continue
        
        #DFS로 현재 타겟 위치 근처에 위치한 배추들 묶음 처리해서 0으로 바꾸기
        DFS(nodeX, nodeY)
        answer += 1 #DFS로 묶음 처리 완료되면, 묶음 개수 1 증가



    print(answer)


 


#로직을 생각해보자. DFS, BFS 어느 쪽을 사용하던지 간에 무관하게,
# (0, 0)에서 시작한다고 할 때에, MN 이상의 시간복잡도로만 해결할 수 밖에 없나?
# 기본적으로 각 배추가 위치한 자리에 대한 데이터를 가지고 있으니, 전체 배추밭 배열 루프 돌리는 것이 아니라
#배추가 위치한 자리들에 대해서만 반복문을 돌게 한다면?
#그렇다면, 이미 처리해서 0으로 바꾼 배추를 배추가 위치한 자리를 보관하는 배열에서 제거해야 하는데,
# 배열 제거 및 재정립은 시간이 걸리니, 그냥 그 좌표에 배추가 위치하지 않으면 스킵하는 방식으로?