#백준 1987번 알파벳


import sys
input = sys.stdin.readline

#입력
R, C = map(int, input().split())
Board = [list(input().strip()) for _ in range(R)]

#상하좌우
Direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

answer = 1

Passed = [0] * 26 #알파벳을 방문했는지 체크하기 위한 배열

Passed[ord(Board[0][0]) - ord('A')] = 1 #시작점 방문 체크

def DFS(x, y, cnt):
    
    global answer
    answer = max(answer, cnt) #최대값을 찾기 위한 변수
    
    #알파벳이 26개라면 더 이상 탐색할 필요가 없음
    if answer == 26:
        return

    #상하좌우 탐색
    for dx, dy in Direction:
        nx, ny = x + dx, y + dy #다음 좌표

        #범위 내에 있고
        if not(0 <= nx < R) or not(0 <= ny < C):
            continue
            
        

        #방문하지 않은 알파벳이라면
        if Passed[ord(Board[nx][ny]) - ord('A')] == 0:

            Passed[ord(Board[nx][ny]) - ord('A')] = 1 #방문 체크
            DFS(nx, ny, cnt + 1) #다음 좌표로 이동
            Passed[ord(Board[nx][ny]) - ord('A')] = 0 #방문 해제

DFS(0, 0, 1) #시작점부터 탐색 시작

print(answer)




