T = int(input())
for test_case in range(1, T + 1):
    #######################################################################################################

    # 상자 개수 N
    N = int(input())
    answer = 0 # 정답 값

    #상자 list
    box = list(map(int, input().split()))

    # 평탄화가 되었을 때 사탕의 값
    mean_value = sum(box) // N


    while True:

        # 이미 평평한 상태인지를 검증하기
        passed = True

        # 단순하게, 평탄화 사탕값이 아닌 값이 box에 존재하는지 검증
        for sweet in box:

            # 평탄화 사탕값이 아닌 값이 발견되면, 이번 loop 또 돌아야 함
            if sweet != mean_value:
                passed = False
                break

        # 모든 값이 다 평탄화 값으로 되어 있으면, 반복루프 중단
        if passed:
            break

        # 가장 적은 사탕
        min_box = min(box)
        min_box_idx = box.index(min_box)

        # 가장 많은 사탕
        max_box = max(box)
        max_box_idx = box.index(max_box)

        # 가장 많은 사탕을 가장 적은 사탕으로 하나 옮기기
        box[max_box_idx] -= 1
        box[min_box_idx] += 1

        # 옮김 횟수 1 증가
        answer += 1

    #######################################################################################################

    # 표준출력(화면)으로 답안을 출력합니다.
    print(f"#{test_case} {answer}")