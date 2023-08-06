#24480번 깊이 우선 탐색 2 (백준)





#백준 24479번  깊이 우선 탐색 1

#recursionerror 발생으로 인해,recursionlimit 값을 설정해주기
#기본값은 10**3, 1000번이며 그 이상의 재귀는 값을 설정해주어야 한다
import sys
sys.setrecursionlimit(10**6)


#그래프를 어떻게 구현하지?
#정점은 그냥 받기
#간선 = 정점의 관계 = 그래프
#간선을 인접 리스트로 구현해서 자원을 절약하며 그래프의 형태 받기


#정점, 간선, 시작 정점
n, m, r = list(map(int, sys.stdin.readline().split(sep=" ")))

#모든 배열은 n + 1의 크기를 가지도록 해, 마지막 idx가 n이 되도록 함

#방문 순서를 표시할 배열
answer = [0 for _ in range(n + 1)]

#방문 여부를 확인할 배열, 0이면 안갔고, 1이면 갔음
visited = [0 for _ in range(n + 1)]

#간선의 정보 u, v 를 담을 배열
m_set = [[] for _ in range(n + 1)]

for i in range(m):

    #간선의 정보를 a로 받기
    a = (list(map(int, sys.stdin.readline().split(sep=" "))))

    #인접 리스트 구현, m_set[u]에 v의 값을 넣어서, u에서 갈 수 있는 v들을 관리
    #방향 그래프가 아니기에, v > u 로 갈 수 있는 경로도 넣어주기
    m_set[a[0]].append(a[1])
    m_set[a[1]].append(a[0])

#print(m_set)


global sequence
sequence = 1


def Dfs(r):

    global sequence

    #방문 여부와 방문 순서 표기, 순서는 표기 후 +1
    visited[r] = 1

    answer[r] = sequence

    sequence += 1

    a = sorted(m_set[r], reverse=True)

    #r과 연결되어 있는 정점들, 즉 간선의 정보가 담긴 인접 리스트 접근
    #인접 정점은 내림차순 접근한다고 한다
   
    for x in a:     

        #간선 u > v 에서, v에 방문한 적이 없으면 재귀로 방문
        if visited[x] == 0:

            Dfs(x)

Dfs(r)

# print(answer)

 
for i in range(1, n + 1):
    sys.stdout.write(str(answer[i]) + "\n")
    # print(answer[i])
























