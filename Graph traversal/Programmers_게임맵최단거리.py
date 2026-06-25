def solution(maps):

    import copy

    answer = 1

    # 지도는 벽이 0, 길은 1로 구성되어져 있다.

    # BFS로 풀어보기

    N = len(maps)
    M = len(maps[0])
    
    # 동일한 크기의 방문 배열 구축해두기
    visited_matrix = [[False for j in range(M)] for i in range(N)]
    

    move_top = (0, -1)
    move_down = (0, 1)
    move_right = (1, 0)
    move_left = (-1, 0)

    # movement는 위, 아래, 우, 좌 순으로 이루어진다
    movement = [move_top, move_down, move_right, move_left]

    # 목표 찾음 여부 변수
    find_target = False

    # 외부 BFS Loop에서 탐색할 애들 보관할 리스트
    global_queue = []
    
    # 맨 처음 시작 지점 정보 주입
    global_queue.append((0,0))
    visited_matrix[0][0] = True

    # 목표를 찾을 때 까지 루프
    while not find_target:

        #  global_queue가 비어잇는데 목표가 없으면, 타겟을 찾지 못한것
        if len(global_queue) == 0:
            answer = -1
            break


        # 이번 루프에서 방문할 지점들을 우선 수집 및 조건 검증을 해야 할거다

        # 이후에 global_queue에 넣기 전에 보관할 다음 목적지 후보들의 리스트
        local_queue = []

        # global_queue 들에 대해 다 검검증
        while global_queue:

            #검증을 시작할 x, y 좌표 추출
            cur_x, cur_y = global_queue.pop()

            # 만약 이게 목표 지점이라면 정답이므로 break
            if cur_x ==N - 1 and cur_y == M - 1:
                find_target = True
                break

            # 상하좌우 방향에 대해 전부 다 접근 시도
            for move in movement:

                # 다음 목적지 좌표 설정
                next_x = cur_x + move[0]
                next_y = cur_y + move[1]

                # 미로의 범위 초과 여부 검증
                if next_x < 0 or next_x >= N or next_y < 0 or next_y >= M :
                    continue

                # 미로의 벽에 부딪혔을 때 검증
                if maps[next_x][next_y] == 0:
                    continue

                # 이미 방문한 곳 여부인지 검증
                if visited_matrix[next_x][next_y]:
                    continue
        
                # 범위초과 X && 미로 벽 부딪힘 X && 방문했던 곳 X 면, 방문을 해도 되는 곳
                local_queue.append((next_x, next_y))
                visited_matrix[next_x][next_y] = True

        if find_target:
            break

        # global_queue를 다 돌았으면, 한 루프를 달성한 것. 거리 1 증가.
        
        answer += 1

        #local_queue의 내용을 global-queue로 넘겨주기
        global_queue = local_queue
    return answer