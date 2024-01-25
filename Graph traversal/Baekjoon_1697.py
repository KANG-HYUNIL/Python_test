#1697번 숨바꼭질(백준) 그래프 탐색
import sys
from collections import deque

#방문 지점 체크를 이용해야 한다

#시작점 n과 도착점 k 입력
n, k = list(map(int, sys.stdin.readline().split(sep=" ")))

global answer 
answer = 0

#지점 방문 가능 여부를 확인할 배열
visit_ary = [1] * 100001

#이동은 1초에 걸쳐 좌, 우(+-1) 혹은 2배(*2) 이동이 있다.

#BFS를 이용해, n에서 k로 도달하는 데에 필요한 최단 시간을 계산하는 함수
#미로 문제와는 다르게 한계점이 없기 때문에, DFS는 안된다
def BFS(n, k):

    #만약 n과 k가 같다면, 바로 함수 return 
    if n == k:
        return

    global answer

    Check = False #k 도착 여부를 확인할 bool 변수

    deq = deque() #이동 후의 점들을 모아둘 deque

    deq.append(n)

    visit_ary[n] = 0

    while True:

       # points = []
        s = set() #이동 후의 점들의 중복 제거를 위해 set을 활용

        while len(deq) != 0: #이동 후의 점들이 존재할 동안

            startPoint = deq.popleft()

            #좌우 이동 및 *2 이동 계산
            for i in range(3):

                if i == 0 :
                    
                    movePoint = startPoint + 1 #+1 이동

                    #범위를 초과하거나, 이미 방문했던 지점이라면
                    if movePoint < 0 or movePoint > 100000 or visit_ary[movePoint] == 0:
                        pass

                    elif movePoint == k: #k 도착 시 Check 표시 후 break
                        Check =True
                        break
                    
                    else:
                        visit_ary[movePoint] = 0
                        s.add(movePoint)
                    

                  

                elif i == 1:
                    
                    movePoint = startPoint - 1 # -1 이동

                    #범위를 초과하거나, 이미 방문했던 지점이라면
                    if movePoint < 0 or movePoint > 100000 or visit_ary[movePoint] == 0:
                        pass

                    elif movePoint == k: #k 도착 시 Check 표시 후 break
                        Check =True
                        break
                    
                    else:
                        visit_ary[movePoint] = 0
                        s.add(movePoint)

                  

                elif i == 2:

                    movePoint = startPoint * 2 # *2 이동

                    #범위를 초과하거나, 이미 방문했던 지점이라면
                    if movePoint < 0 or movePoint > 100000 or visit_ary[movePoint] == 0:
                        pass

                    elif movePoint == k: #k 도착 시 Check 표시 후 break
                        Check =True
                        break
                    
                    else:
                        visit_ary[movePoint] = 0
                        s.add(movePoint)


        #이동 시간에 1초 추가
        answer += 1

        #만약 목표 지점인 k에 도착했다면, break
        if Check == True:
            break

        l_s = list(s)

        for i in l_s:
            deq.append(i)


BFS(n, k) #최단 시간 계산

print(answer) #정답 출력

