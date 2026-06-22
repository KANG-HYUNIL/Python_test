T = int(input())
for test_case in range(1, T + 1):
    #######################################################################################################

    # 보급 개수 N
    N = int(input())
    answer = 0 # 정답 값

    #보급 list
    supply = list(map(int, input().split()))
    supply.sort()

    # 가능한 모든 x 좌표에 대해서 loop 진행
    for x in range(supply[0], supply[-1] + 1):

        for i in range(N):

            s = supply[i]

            # 지금 보는 supply 위치가 x 좌표보다 작으면 일단 스킵
            if s < x:
                continue

            if s > x:

                left_supply_gap = x - supply[i - 1]
                right_supply_gap = s - x

                answer_candidate = max(left_supply_gap, right_supply_gap)
                answer = max(answer, answer_candidate)
                break

            # 현재 x 좌표가 보급이 있는 위치라면
            if s == x:

                # 가장 좌측 x좌표면
                if x == supply[0]:
                    answer = max(answer, supply[1] - x)

                # 가장 우측 x 좌표면
                elif x == supply[-1]:
                    answer = max(answer, x - supply[-2])

                # 그 가운데라면
                else:
                    left_supply_gap = x - supply[i - 1]
                    right_supply_gap = supply[i + 1] - x

                    answer_candidate = min(left_supply_gap, right_supply_gap)

                    answer = max(answer, answer_candidate)

                # 이 x 좌표에 대한 정답값 구했으니 break
                break

    #######################################################################################################

    # 표준출력(화면)으로 답안을 출력합니다.
    print(f"#{test_case} {answer}")