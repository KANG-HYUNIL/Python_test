TC = 10

for i in range(1, TC + 1):

    # 건물  개수 N
    N = int(input())

    # 건물 높이 리스트 
    buildings = list(map(int, input().split()))

    answer = 0 # 기본 정답값은 0

    # 맨 왼쪽/오른쪽 2개는 건물이 없음.
    for j in range(2, N - 2):

        mid_building = buildings[j]
        left_1_building = buildings[j - 1]
        left_2_building = buildings[j - 2]

        right_1_building = buildings[j + 1]
        right_2_building = buildings[j + 2]

        # # 좌우 1칸씩 검증, 가려지는 부분 있으면 바로 스킵
        # if left_1_building >= mid_building or right_1_building >= mid_building :
        #     continue

        # # 1차 정답 후보군 획득, 바로 옆 1칸만 비교하여서 얻는 조망권 수치
        # answer_candidate = mid_building - max(left_1_building, right_1_building)

        # # 좌우 2칸씩 검증, 다 가려지면 스킵
        # if left_2_building >= mid_building or right_2_building >= mid_building:
        #     continue

        # 더 간단하게, 양쪽 비교 후 max 값으로 처리하기?

        near_top_building = max(left_2_building, left_1_building, right_2_building, right_1_building)
        if mid_building <= near_top_building :
            continue

        # 이번 Loop에서 얻은 정답 값
        A = mid_building - near_top_building
        answer += A

    print(f"#{i} {answer}")