def solution(tickets):
    answer = []

    # 문자열(공항 이름)을 Key로, Value는 알파벳 정렬된 리스트

    ticket_dict = dict()    

    visited_airpot_dict = dict()

    INITIAL_AIRPORT = "ICN"

    # 출발지와 도착지 공항 리스트 정립
    for airport in tickets:

        if  airport[0] not in ticket_dict:
            ticket_dict[airport[0]] = []
        
        ticket_dict[airport[0]].append(airport[1])

        #매 번 삽입 후에 공항 경로 처리 위해서 알파벳 정렬해주기
        ticket_dict[airport[0]].sort()

    # 출발지에서 도착지  가는 공항 목록들의 방문 dict 처리(중복 방문 및 무한 루프 방지위함)
    for key, value in ticket_dict.items():

        target_airport_len = len(value)

        visited_airpot_dict[key] = [0] * target_airport_len    

    

    def dfs(cur_airport):


        # 모든 티켓을 다 사용했으면 정답
        if len(answer) == len(tickets) + 1:
            return True

        # 막다른 길에 도달했으면 오답, 뒤로 돌아가기 해봐야됨
        if cur_airport not in ticket_dict:
            return False

        # 현재 위치한 공항에서 갈 수 있는 다른 공항들에 대한 loop
        for target_airport_idx in range(len(ticket_dict[cur_airport])):

            target_airport = ticket_dict[cur_airport][target_airport_idx]

            # 아직 방문한 적 없는 루트라면
            if visited_airpot_dict[cur_airport][target_airport_idx] == 0:
                #방문 처리
                visited_airpot_dict[cur_airport][target_airport_idx] = 1

                answer.append(target_airport)

                if dfs(target_airport):
                    return True

                # backtracking
                answer.pop()
                visited_airpot_dict[cur_airport][target_airport_idx] = 0

                
    answer.append(INITIAL_AIRPORT)

    dfs(INITIAL_AIRPORT)


    return answer
    