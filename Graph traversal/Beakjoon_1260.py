#1260번 DFS와 BFS(백준)



#recursionerror 발생으로 인해,recursionlimit 값을 설정해주기
#기본값은 10**3, 1000번이며 그 이상의 재귀는 값을 설정해주어야 한다
import sys
sys.setrecursionlimit(10**6)



#그래프를 어떻게 구현하지?
#정점은 그냥 받기
#간선 = 정점의 관계 = 그래프
#간선을 인접 리스트로 구현해서 자원을 절약하며 그래프의 형태 받기


#BFS 구현 위해 deque 사용
from collections import deque

deq = deque()


#오름차순 방문

n, m, v = list(map(int, sys.stdin.readline().split(sep=" ")))

#방문한 점을 순서대로 담을 배열
answer = []

visited = [0 for _ in range(n + 1)]

m_set = [[]for _ in range(n + 1)]

#간선 정보 받기
for i in range(m):
    
    a = list(map(int, sys.stdin.readline().split(sep=" ")))

    m_set[a[0]].append(a[1])
    m_set[a[1]].append(a[0])

#오름차순 방문이기에, 미리 정렬
for i in m_set:

    i.sort()

# print(n, m, v)
# print(m_set)


def DFS(v) :

    #방문한 정점 넣기
    answer.append(v)

    #방문했다는 표시
    visited[v] = 1

    #v와 연결된 정점들 검사
    for a in m_set[v]:

        #방문하지 않은 정점이 있다면
        if visited[a] == 0:

            #재귀로 접근
            DFS(a)



def BFS(v) :

    answer.append(v)

    visited[v] = 1

    #deque에 v 넣어주기
    deq.append(v)


    while len(deq) > 0 :

        #deque의 왼쪽 원소 가져오기
        a = deq.popleft()

        for x in m_set[a] :

            if visited[x] == 0:
        
                visited[x] = 1
                answer.append(x)
                deq.append(x)

   
DFS(v)

print(" ".join(list(map(str, answer))))


answer = []

visited = [0 for _ in range(n + 1)]

BFS(v)

print(" ".join(list(map(str, answer))))

