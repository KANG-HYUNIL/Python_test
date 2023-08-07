#2606번 바이러스(백준)

#입출력 sys, 재귀 제한 설정
import sys
sys.setrecursionlimit(10**6)

#컴퓨터의 수 받기
n = int(sys.stdin.readline())

#간선의 수 받기
m = int(sys.stdin.readline())

#각 컴퓨터의 방문 여부를 확인할 배열 
visited = [0 for _ in range(n + 1)]

#인접한 정점을 받을 인접 리스트
m_set = [[] for _ in range(n + 1)]


#연결되어있는 간선의 정보 받기
for i in range(m):

    a = list(map(int, sys.stdin.readline().split(sep=" ")))


    #각 간선에 방향이 없기 때문에, 양 정점에 간선 정보 모두 기록
    m_set[a[0]].append(a[1])
    m_set[a[1]].append(a[0])


#시작 컴퓨터는 1로 고정
r = 1

#답을 담을 gloabal 변수
global answer

answer = 0


def DFS(r):

    global answer

    #방문 여부 표시
    visited[r] = 1


    #r과 연결된 정점들 확인
    for x in m_set[r]:

        #r과 연결된 정점들 중 하나, x에 방문한 적이 없다면
        if visited[x] == 0:

            #방문, 바이러스 감염 + 1
            answer += 1

            #x와 연결된 정점들을 찾기 위해 재귀함수
            DFS(x)


    pass


DFS(r)


# print(m_set)
# print(visited)
print(answer)








