#24444번 너비 우선 탐색 1(백준)


#recursionerror 발생으로 인해,recursionlimit 값을 설정해주기
#기본값은 10**3, 1000번이며 그 이상의 재귀는 값을 설정해주어야 한다
import sys
sys.setrecursionlimit(10**6)



#그래프를 어떻게 구현하지?
#정점은 그냥 받기
#간선 = 정점의 관계 = 그래프
#간선을 인접 리스트로 구현해서 자원을 절약하며 그래프의 형태 받기


#문제의 예시 알고리즘대로 풀어보기 위해 deque 사용
from collections import deque

deq = deque()

#정점, 간선, 시작 정점
n, m, r = list(map(int, sys.stdin.readline().split(sep=" ")))


#방문 순서를 표시할 배열
answer = [0. for _ in range(n + 1)]

#방문 여부를 확인할 배열, 0이면 안갔고, 1이면 갔음
visited = [0. for _ in range(n + 1)]

#간선의 정보 u, v 를 담을 배열
m_set = [[] for _ in range(n + 1)]


for i in range(m):

    #간선의 정보를 a로 받기
    a = (list(map(int, sys.stdin.readline().split(sep=" "))))

    #인접 리스트 구현, m_set[u]에 v의 값을 넣어서, u에서 갈 수 있는 v들을 관리
    #방향 그래프가 아니기에, v > u 로 갈 수 있는 경로도 넣어주기
    m_set[a[0]].append(a[1])
    m_set[a[1]].append(a[0])


global sequence
sequence = 1



def Bfs(r):

    global sequence

    #방문 여부 
    visited[r] = 1

    #방문 순서
    answer[r] = sequence
    sequence += 1
    
    #deque에 r 넣어주기
    deq.append(r)

    
    while len(deq) != 0:

        #큐의 가장 앞 원소를 제거
        a = deq.popleft()

        #a와 간선으로 연결된 인접 정점들을 오름차순으로 탐색
        for x in sorted(m_set[a]):

            if visited[x] == 0:
                #방문 여부
                visited[x] = 1


                answer[x] = sequence
                sequence += 1

                deq.append(x)


 
Bfs(r)


 
for i in range(1, n + 1):
    sys.stdout.write(str(answer[i]) + "\n")
    # print(answer[i])


