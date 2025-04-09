#백준 15684번 사다리 조작

#순열이 아닌 조합으로 접근해야 할거다.
#최적해를 얻는 로직은 생각이 안난다, 그냥 모든 경우의 수 때려박고 해야 할 듯.
# 세로선, 가로선, 위치의 수가 그렇게 크지 않다. Brute Force.

# 문제의 목표는, 각 세로선의 시작 위치가 끝 위치와 동일한 구조가 되게끔.
# 이동 로직은 일반적인 사다리 게임과 동일하다, 그러기에 연속으로 가로선이 배치될 수는 없다
# 가로선의 위치를 관리할 배열을 백트래킹으로 재귀때려서 처리시켜야 할 듯.


import sys
input = sys.stdin.readline

MAX_CNT = 3 # 가로선의 최대 개수
N, M, H = map(int, input().split()) # 세로선, 가로선, 사다리 높이

# idx 접근 편하게 하기 위해서, 0번째 행, 열 은 사용하지 않기로. 1번부터 처리.
# ladder[row][col] = 1 이면, row 행의 col 열에서 col + 1 열로 가는 가로선이 존재한다는 의미.
ladder = [[0] * (N + 1) for _ in range(H + 1)] # 사다리의 상태를 저장할 배열

for i in range(M):

    a, b = map(int, input().split()) # a = 가로 위치, b = 세로 위치. b -> b + 1로 연결했다는 의미.
    ladder[a][b] = 1 # 가로선이 존재하는 위치에 1을 저장


answer = -1 # 정답을 저장할 변수, 초기값은 -1로 설정. 사다리 조작이 불가능한 경우를 처리하기 위함.

# 모든 세로의 시작위치가 도착 위치와 동일한지 연산 하는 메서드. 동일하면 true 뱉기. 하나라도 다르면 false 뱉기.
def calculate_ladder(target_ladder):

    #각 열에 대해 처리
    for col in range(1, N + 1):
        cur_col = col
        
        # 현재 처리하는 열을 행 한칸 씩 아래로 이동시키기
        for row in range(1, H + 1):

            #만약 내려가는데 우측에 가로선이 존재하면, 우측으로 이동
            if target_ladder[row][cur_col] == 1:   
                cur_col += 1 #1칸 우측 이동

            #만약 내려가는데 좌측이 범위를 벗어나지 않고, 좌측에 가로선 존재 시에 좌측으로 이동
            elif cur_col > 1 and target_ladder[row][cur_col - 1] == 1:
                cur_col -= 1 #1칸 좌측 이동

        # 행의 바닥까지 이동 완료 시에 최초 출발 열인 col와 현재 열인 cur_col이 다른지 분석
        if cur_col != col:
            return False
        
    return True # 모든 세로선의 시작 위치와 도착 위치가 동일함.



#ladder = 사다리 배열(깊은 복사 처리 필요), cur_row = 마지막 사다리 놓은 행, cur_col = 마지막 사다리 놓은 열, cnt = 현재까지 놓은 가로선의 개수
#순열이 아닌 조합으로 처리하기 위해서, 사다리 배치는 마지막 사다리 배치에서 우측, 아래로만 가능하게끔.
def recursion(ladder, cur_row, cur_col, cnt):

    global answer # 정답 전역 변수

    #이미 최소값인 0 찾았다면 추가 연산 불필요
    if answer == 0 :
        return

    # 현재 시도하는 사다리의 개수보다 이미 적은 걸로 가능한것을 알면, 연산 불필요
    if answer != -1 and answer <= cnt:
        return

    #현재 사다리의 가능 여부 분석
    if calculate_ladder(ladder):
        # 사다리의 시작 위치와 도착 위치가 동일한 경우, 정답을 갱신
        if answer == -1 or answer > cnt:
            answer = cnt

            if answer == 0 :
                return
    
    #이미 3개 깔았으면, 더 이상 볼 필요 없음
    if cnt == MAX_CNT:
        return

    #재귀 처리 진입

    #현재 진행한 row부터 하여서, 위쪽 row는 보지 않게끔
    for new_row in range(cur_row, H + 1):

        # 지금 보는 row가 현재 row 라면
        if new_row == cur_row:

            #현재 col부터 하여서, 이미 지난 왼쪽 col은 보지 않게끔
            for new_col in range(cur_col, N):
                
                #배치하려는 위치에 이미 가로줄이 있으면
                if ladder[new_row][new_col] == 1:
                    continue

                #배치하려는 위치의 좌측에 이미 가로줄이 있으면
                if new_col > 1:
                    if ladder[new_row][new_col - 1] == 1:
                        continue
                
                #배치하려는 위치의 우측에 이미 가로줄이 있으면
                if new_col < N:
                    if ladder[new_row][new_col + 1] == 1:
                        continue

                ladder[new_row][new_col] = 1 # 가로줄 배치
                recursion(ladder, new_row, new_col + 2, cnt + 1) # 재귀 발사 
                ladder[new_row][new_col] = 0 # 가로줄 배치 해제

                if answer == 0:
                    return


        else:
            # N이 최대 10이니, 그냥 모든 col에 대해 처리하게 하자
            for new_col in range(1, N):

                #배치하려는 위치에 이미 가로줄이 있으면
                if ladder[new_row][new_col] == 1:
                    continue

                #배치하려는 위치의 좌측에 이미 가로줄이 있으면
                if new_col > 1:
                    if ladder[new_row][new_col - 1] == 1:
                        continue
                
                #배치하려는 위치의 우측에 이미 가로줄이 있으면
                if new_col < N:
                    if ladder[new_row][new_col + 1] == 1:
                        continue

                ladder[new_row][new_col] = 1 # 가로줄 배치
                recursion(ladder, new_row, new_col + 2, cnt + 1) # 재귀 발사 
                ladder[new_row][new_col] = 0 # 가로줄 배치 해제

                if answer == 0:
                    return



recursion(ladder=ladder, cur_row=1, cur_col=1, cnt=0) # 재귀 발사

print(answer)

