from collections import defaultdict



# 문제 정의는 다음과 같다.
# 2차원 평면에 N개의 점이 위치해있으며, 각 점의 좌표인 (x, y)는 모두 정수이다.
# 이 때 임의의 3개 점을 골라서 삼각형을 만들어야 한다만,

# 1. 삼각형의 한 변은 X축 평행 요구
# 2. 삼각형의 다른 한 변은 Y축 평행 요구

# 위의 조건을 만족하며 넓이가 가장 큰 삼각형의 넓이를 출력하여라.
# 넓이에 2를 곱해 정수의 형태로  출력하도록 하여라.


# 입력 조건은 다음과 같다.
# 첫 줄 : TC의 개수
# 그 이후 TC개의 테스트 케이스가 구분되어 주어짐.
# 각 TC는 맨 처음에는 정수 N이 주어지며, 3 <= N <= 100 이다.
# 그 이후 N개의 줄에 걸쳐서 점의 좌표인 X_i, Y_i가 주어진다. 모든 좌표값은 서로 다른 것이 보장되며, 절댓값이 10000 이하인 정수이다. 


# 1차 제출, 틀렸다. 왜 틀렸을까?

# ---- 풀이 코드-------

MIN = 0
MAX = 1

# TC 개수 받기
TC = int(input())

# TC에 대한 Loop
for i in range(TC):

    # 해당 TC의 점 개수 N개 받기
    N = int(input())
    
    # 해당 TC의 점들을 받을 List
    points = []

    # 정답 값
    answer = 0

    # 특정 x 좌표에 대해서 그 x좌표를 가진 y 값의 최대, 최소를 저장할 default dict
    x_min_dict = defaultdict(lambda : float('inf'))
    x_max_dict = defaultdict(lambda : float('-inf'))


    # 특정 y 좌표에 대해서 그 y좌표를 가진 x 값의 최대, 최소를 저장할 default dict
    y_min_dict = defaultdict(lambda : float('inf'))
    y_max_dict = defaultdict(lambda : float('-inf'))

    # 점 개수 N에 대한 Loop
    for j in range(N):
        x, y = map(int, input().split())
        points.append([x, y])

        # x_minMax_dict 값 갱신
        x_min_dict[x] = min(x_min_dict[x], y)
        x_max_dict[x] = max(x_max_dict[x], y)

        # y_minMax_dict 값 갱신
        y_min_dict[y] = min(y_min_dict[y], x)
        y_max_dict[y] = max(y_max_dict[y], x)


    # 점들이 있는 points에 대한 loop
    for p in points:
        main_x, main_y = p # 직각점이 될 점 획득

        #요기가 문제이@!

        if abs(main_y - x_min_dict[main_x]) > abs(main_y - x_max_dict[main_x]):
            top_y = x_min_dict[main_x]
        else : 
            top_y = x_max_dict[main_x]


        if abs(main_x - y_min_dict[main_y]) > abs(main_x - y_max_dict[main_y]):
            top_x =  y_min_dict[main_y]
        else : 
            top_x =  y_max_dict[main_y]

        value = abs(main_y  - top_y) * abs(main_x - top_x)

        answer = max(answer, value)
    
    print(answer)
