#백준 14890번 경사로

#문제가 조금은 이해가 되지 않기도 한데..

#모든 칸(가로 혹은 세로)의 높이가 동일하거나, 높이가 낮은 칸에는 경사로가 놓여져 잇어야만 길로 취급.
#그럼 궁금한 건, 높이가 1 2 3 이렇게 순차적으로 있을 때에 연속적으로 경사로를 놓으면, 길로 취급된다는 건가?
#문제의 예시를 보았을 때에는, 순차적 높이 시에 경사로 블럭의 길이만 맞으면, 연속적으로 경사로 블럭을 배치해도 되는 것으로 보인다

#자, 순차적인 높이에서 연속적으로 경사로를 쌓는 것은 문제가 없다는걸 확인했다.
#그럼 이제 다른 방향의 생각. 한 방향의 경로 상에 놓는 경사로 블럭 때문에,
#따른 방향의 경사로가 막혀서, 지나갈 수 있는 길의 경우의 수에 영향을 주는 것은 어떻게 처리해야 하나?
# 문제 상에서, "최대" 라는 말이 없고, 단순히 지나갈 수 있는 길의 개수를 구하라 했다.
# 예제들을 보았을 때에, 경사로를 놓아 한 번에 만들 수 있는 길의 최대 수를 구하는 것이 아니다.
# 각 방향의 경로에 대하여, 따로 따로 처리하는 것이다.
# 한 방향의 길에 놓은 경사로는, 이후 다른 방향의 길을 연산할 때에 전혀 고려 대상이 되지 않는다.
# 이러면 문제가 매우 매우 쉬워짐.

#한 쪽 끝에서 다른 쪽 끝으로 차례차례 점검한다고 했을 때에,
#오르막길 구분은 되게 쉬울거다. 이동하면서 보아온 길이가 있으니까
# 그럼 내리막길은 어떻게?

# 일단은 코드가 보기 어려워도, 로직 수행의 분기를 확실히 분리하기 위해서 길게 작성

import sys

input = sys.stdin.readline


N, L = map(int, input().split()) #N*N 지도, 경사로 길이 L
board = [list(map(int, input().split())) for _ in range(N)] #지도

# 반복의 횟수는 2N 번.
answer = 2 * N

#행 단위 길 체크 한 번, 열 단위 길 체크 한 번.

# board[i][j] = 높이 이며, i는 행, j는 열

# 행 단위
for i in range(N):

    cur_height = board[i][0] #현재 높이
    cur_length = 1 #현재 길이 

    #3중 반복문으로 하는 것도 고려해보았으나, 시간복잡도 늘어나는거 싫어서, 멤버 변수 좀 추가해서라도 2중으로 끝내기

    get_down = False # 높이가 낮아지는,내려가는 경사로 배치를 연산 중인지 여부 체크


    #해당 방향 길의 다음 칸들 점검
    for j in range(1, N):

        # 7) 내리막길 경사로 배치 연산 시작
        if get_down :

            # 8) 경사로의 바닥면이 될 블럭들의 길이가 L과 같다면, 바로 경사로 배치
            if cur_length == L: 
                get_down = False #내려가는 경사로 배치 완료

            # 9) 경사로의 바닥면이 될 블럭들의 길이가 L보다 작다면, 다음 블럭들의 높이를 계속 봐야 함
            elif cur_length < L : 

                #10) 다음 블럭들의 높이가 현재 높이의 위치와 같지 않으면, 경사로 배치 불가, 길 X
                if cur_height != board[i][j]: 
                    answer -= 1
                    # print ("(i, j) =")
                    # print(i, j)
                    break # 현재 보고 있는 길을 그만 보고, 다음 길로 이동

                # 11) 다음 위치의 높이가 현재 위치의 높이와 같다면, 경사로 길이 증가
                cur_length += 1 #길이 증가

                if j == N - 1 and not cur_length == L:
                    answer -= 1
                    break

                continue #continue로 다음 위치로 이동
            
            # 12) 경사로 배치 후에, 현재 위치의 다음 위치 높이를 봐야 함
            # 경사로 배치 후에 다음 위치의 높이의 차이가 2 이상 나거나, 더 높으면 통행 불가
            if not get_down :

                # 13) 경사로 배치를 막 끝냈는데 다음 위치의 높이가 현재 보다 높다면, 통행 불가능, 길 x
                if cur_height < board[i][j]:
                    #현재 위치의 높이가 다음 위치의 높이보다 낮다면, 경사로 배치 불가
                    answer -= 1
                    # print ("(i, j) =")
                    # print(i, j)
                    break
                
                # 14) 다음 위치의 높이가 현재 위치 높이보다 1 보다 더 낮다면, 경사로 배치 불가, 길 X
                if cur_height - 1 > board[i][j] : 
                    answer -= 1
                    # print ("(i, j) =")
                    # print(i, j)
                    break # 현재 보고 있는 길을 그만 보고, 다음 길로 이동

                # 15) 다음 위치의 높이가 현재 위치 높이와 동일하다면, 그냥 연산하면 됨
                if cur_height == board[i][j]:
                    cur_length = 1 #현재 길이 초기화
                
                # 16) 경사로 배치를 끝냈는데, 다음 위치의 높이가 현재 위치보다 1만큼 낮아서 또 바로 경사로 연산을 해야 한다면
                if cur_height - 1 == board[i][j] :
                    cur_height = board[i][j] # 현재 높이도 다음 블럭의 높이로 갱신
                    cur_length = 1 # 현재 길이 초기화
                    get_down = True

                    if j == N - 1 and not cur_length == L: #
                        answer -= 1
                        break

            pass
        
        # 1) 다음 블럭이 현재와 높이가 같으니, 길이 증가
        elif cur_height == board[i][j]: # 같을 때는 현재 보고 있는 높이의 길이 증가
            cur_length += 1 #길이 증가
             
        
        # 2) 다음 블럭의 높이가 현재 높이의 + 1 이니, 경사로 배치 여부 분석 시작
        elif cur_height + 1 == board[i][j] :

            # 3) 오르막길 경사로 배치, 이전에 보았던 길이가 L 이상이여야 한다
            if cur_length >= L:
                # 현재 높이와 동일한 높이의 블럭이 L개 이상 배치되어 있다면,
                # 현재 높이와 동일한 높이의 블럭을 경사로로 놓을 수 있음
                cur_length = 1
                cur_height = board[i][j] # 현재 높이도 다음 블럭의 높이로 갱신
                # print ("(i, j) =")
                # print(i, j)

            # 4) 이전에 보았던 길이가 L 미만이면, 경사로 배치 불가, 길 X 
            else :
                answer -= 1
                # print ("(i, j) =")
                # print(i, j)
                break

        # 5) 다음 블럭의 높이가 현재 높이의 -1이니, 내리막길 경사로 배치 여부 분석 시작
        elif cur_height - 1 == board[i][j] : 
            cur_height = board[i][j] # 현재 높이도 다음 블럭의 높이로 갱신
            cur_length = 1 # 현재 길이 초기화
            get_down = True #내리막길 경사로 배치 시작d

            if j == N - 1 and not cur_length == L:
                    answer -= 1
                    break


        # 6) 다음 위치의 높이가 현재 위치보다  2 이상 차이나면, 애초에 경사로 배치 불가, 길 X
        else :
            answer -= 1 # 가능한 길의 수 차감
            # print ("(i, j) =")
            # print(i, j)
            break # break로 현재 보고 있는 길을 이제 그만 보고, 다음 길로 이동

    # # 17) 모든 칸을 보았는데, 아직 내리막길 경사로 배치 연산 중이라면
    # if get_down :

    #     # 18) 경사로 바닥면의 칸들의 길이가 L과 같지 않다면, 경사로 배치 불가, 길 X
    #     if not cur_length == L: 
    #         print(i)
    #         print(cur_length)
    #         answer -=1 

# 열 단위
for j in range(N):

    cur_height = board[0][j] #현재 높이
    cur_length = 1 #현재 길이 

    #3중 반복문으로 하는 것도 고려해보았으나, 시간복잡도 늘어나는거 싫어서, 멤버 변수 좀 추가해서라도 2중으로 끝내기

    get_down = False # 높이가 낮아지는,내려가는 경사로 배치를 연산 중인지 여부 체크


    #해당 방향 길의 다음 칸들 점검
    for i in range(1, N):

        # 7) 내리막길 경사로 배치 연산 시작
        if get_down :

            # 8) 경사로의 바닥면이 될 블럭들의 길이가 L과 같다면, 바로 경사로 배치
            if cur_length == L: 
                get_down = False #내려가는 경사로 배치 완료

            # 9) 경사로의 바닥면이 될 블럭들의 길이가 L보다 작다면, 다음 블럭들의 높이를 계속 봐야 함
            elif cur_length < L : 

                #10) 다음 블럭들의 높이가 현재 높이의 위치와 같지 않으면, 경사로 배치 불가, 길 X
                if cur_height != board[i][j]: 
                    answer -= 1
                    # print ("(i, j) =")
                    # print(i, j)
                    break # 현재 보고 있는 길을 그만 보고, 다음 길로 이동

                # 11) 다음 위치의 높이가 현재 위치의 높이와 같다면, 경사로 길이 증가
                cur_length += 1 #길이 증가

                if i == N - 1 and not cur_length == L:
                    answer -= 1
                    break

                continue #continue로 다음 위치로 이동
            
            # 12) 경사로 배치 후에, 현재 위치의 다음 위치 높이를 봐야 함
            # 경사로 배치 후에 다음 위치의 높이의 차이가 2 이상 나거나, 더 높으면 통행 불가
            if not get_down :

                # 13) 경사로 배치를 막 끝냈는데 다음 위치의 높이가 현재 보다 높다면, 통행 불가능, 길 x
                if cur_height < board[i][j]:
                    #현재 위치의 높이가 다음 위치의 높이보다 낮다면, 경사로 배치 불가
                    answer -= 1
                    # print ("(i, j) =")
                    # print(i, j)
                    break
                
                # 14) 다음 위치의 높이가 현재 위치 높이보다 1 보다 더 낮다면, 경사로 배치 불가, 길 X
                if cur_height - 1 > board[i][j] : 
                    answer -= 1
                    # print ("(i, j) =")
                    # print(i, j)
                    break # 현재 보고 있는 길을 그만 보고, 다음 길로 이동

                # 15) 다음 위치의 높이가 현재 위치 높이와 동일하다면, 그냥 연산하면 됨
                if cur_height == board[i][j]:
                    cur_length = 1 #현재 길이 초기화
                
                # 16) 경사로 배치를 끝냈는데, 다음 위치의 높이가 현재 위치보다 1만큼 낮아서 또 바로 경사로 연산을 해야 한다면
                if cur_height - 1 == board[i][j] :
                    cur_height = board[i][j] # 현재 높이도 다음 블럭의 높이로 갱신
                    cur_length = 1 # 현재 길이 초기화
                    get_down = True

                    if i == N - 1 and not cur_length == L: #
                        answer -= 1
                        break


            pass
        
        # 1) 다음 블럭이 현재와 높이가 같으니, 길이 증가
        elif cur_height == board[i][j]: # 같을 때는 현재 보고 있는 높이의 길이 증가
            cur_length += 1 #길이 증가
             
        
        # 2) 다음 블럭의 높이가 현재 높이의 + 1 이니, 경사로 배치 여부 분석 시작
        elif cur_height + 1 == board[i][j] :

            # 3) 오르막길 경사로 배치, 이전에 보았던 길이가 L 이상이여야 한다
            if cur_length >= L:
                # 현재 높이와 동일한 높이의 블럭이 L개 이상 배치되어 있다면,
                # 현재 높이와 동일한 높이의 블럭을 경사로로 놓을 수 있음
                cur_length = 1
                cur_height = board[i][j] # 현재 높이도 다음 블럭의 높이로 갱신
                # print ("(i, j) =")
                # print(i, j)

            # 4) 이전에 보았던 길이가 L 미만이면, 경사로 배치 불가, 길 X 
            else :
                answer -= 1
                # print ("(i, j) =")
                # print(i, j)
                break

        # 5) 다음 블럭의 높이가 현재 높이의 -1이니, 내리막길 경사로 배치 여부 분석 시작
        elif cur_height - 1 == board[i][j] : 
            cur_height = board[i][j] # 현재 높이도 다음 블럭의 높이로 갱신
            cur_length = 1 # 현재 길이 초기화
            get_down = True #내리막길 경사로 배치 시작

            if i == N - 1 and not cur_length == L:
                    answer -= 1
                    break


        # 6) 다음 위치의 높이가 현재 위치보다  2 이상 차이나면, 애초에 경사로 배치 불가, 길 X
        else :
            answer -= 1 # 가능한 길의 수 차감
            # print ("(i, j) =")
            # print(i, j)
            break # break로 현재 보고 있는 길을 이제 그만 보고, 다음 길로 이동

    # 17) 모든 칸을 보았는데, 아직 내리막길 경사로 배치 연산 중이라면
    # if get_down :

    #     # 18) 경사로 바닥면의 칸들의 길이가 L과 같지 않다면, 경사로 배치 불가, 길 X
    #     if not cur_length == L: 
    #         # print(j)
    #         # print(cur_length)
    #         answer -=1 


print(answer)

#(3, 2)
#(3, 3)
# (3)