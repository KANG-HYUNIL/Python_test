#백준 11724번 연결 요소의 개수

from collections import deque
import sys
sys.setrecursionlimit(10**6)

#N, M Input
N, M = map(int, sys.stdin.readline().split()) 
answer = 0
#Graph Input
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())

    #방향이 없는 무방향 그래프이기에 양쪽에 모두 추가
    graph[u].append(v) 
    graph[v].append(u)
    
visited = [False] * (N+1) #방문 여부를 체크하기 위한 배열 

def BFS(i):
    deq = deque([i]) #BFS를 위한 deque

    while deq:
        node = deq.popleft() #deque에서 노드를 꺼내옴

        #해당 노드와 연결된 인근 노드들에 대한 반복
        for neighbor in graph[node]:
            if not visited[neighbor]: #방문하지 않은 노드라면
                visited[neighbor] = True #방문 처리
                deq.append(neighbor) #deque에 추가
            

    #print('BFS 완료')
    return 1



for i in range(1, N+1):

    if not visited[i]:
        answer += BFS(i)


print(answer)