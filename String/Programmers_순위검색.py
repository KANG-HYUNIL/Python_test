def solution(info, query):
    answer = []

    # 개발언어 - cpp, java, python
    # 지원 직군 - backend, frontend
    # 경럭 구분 - junior, senior
    # 소울푸드 - chicken, pizza
    # 점수 - 150 ~ 1000

    WILDCARD = "-"

    # 각 col 별 항목을 key로 가지게 하는 중첩 dict로 접근을 해볼까?
    # 즉, 언어A : [직군A : [경력 A : [소울푸드 A : [], 소울푸드 B : []]], 직군 B: [경력 A : ]]
    database = dict()

    # 들어온 정보들에 대해서 루프 돌리기
    for i in info:

        # 각 항목은 빈 칸으로 구분되어 있으므로, split(" ")를 사용하여 분리한다.
        #그러면 5개의 항목이 나올테니, 그걸 항목별로 분리하기.
        language, position, carrer, soulfood, score = i.split(" ")

        # 점수는 정수형으로 변환해두자.
        int_score = int(score)

        # 우선 해당 language에 대한 항목 만들기
        if language not in database:
            database[language] = dict()

        # 그리고 해당 language -> position 되는 항목 만들기
        if position not in database[language]:
            database[language][position] = dict()
        
        # language > position > carrer로 가는 항목 만들기
        if carrer not in database[language][position]:
            database[language][position][carrer] = dict()
        
        # language > position > carrer > soulfood로 가는 항목 만들기
        if soulfood not in database[language][position][carrer]:
            database[language][position][carrer][soulfood] = []
        
        # 완성된 항목에 해당 지원자의 점수 저장
        database[language][position][carrer][soulfood].append(int_score)


    # 검색 효율성을 위해 score를 정렬해두기
    for language in database.keys():
        for position in database[language].keys():
            for carrer in database[language][position].keys():
                for soulfood in database[language][position][carrer].keys():
                    database[language][position][carrer][soulfood].sort()

    # query 검색 시작

    for q in query : 

        #동등하게 취급하기 위해, " and " 부분을 그냥  공백으로  치환해버리기. 
        q = q.replace(" and ", " ")

        q_list = q.split(" ")

        q_language = q_list[0]
        q_position = q_list[1]
        q_carrer = q_list[2]
        q_soulfood = q_list[3]
        q_score = int(q_list[4])

        candidate = []

        # q_language에 대한 검색 먼저 진행

        # WILDCARD 전체 검색이면
        if q_language == WILDCARD :

            #모든 langauge 항목 key 값 가져와서
            language_list = database.keys()

            # 그것들의 하위 전부 다 이용하기
            for l in language_list:
                candidate.append(database[l])
        
        #명확한 검색 대상이 있으면
        else : 

            # 해당 검색 대상이 있을 경우에만 
            if q_language in database:
                #그것만 이후 검색 항목에 넣기
                candidate.append(database[q_language])

        # q_position에 대한 검색 진행 

        sub_candidate = []
        while candidate : 
            # 이번에 볼 대상 획득
            can = candidate.pop()

            # 만약 전체 검색 와일드카드면
            if q_position == WILDCARD:
                
                #모든 key 획득
                position_list = can.keys()

                # 모든 key에 대해 하위 연결값 획득
                for p in position_list:
                    sub_candidate.append(can[p])
            
            # 하나만 검색이라면
            else :
                # 해당 검색 대상이 있을 경우에만
                if q_position in can:
                    # 그 하나만 획득하기
                    sub_candidate.append(can[q_position])

        # 다음 검색 후보로 candiadate교체
        candidate = sub_candidate

        # 임시로 담아둘 리스트 초기화
        sub_candidate = []


        # q_carrer에 대한 검색 진행
        while candidate:

            # 이번에 볼  대상 획득
            can = candidate.pop()

            if q_carrer == WILDCARD:
                carrer_list = can.keys()

                for c in carrer_list:
                    sub_candidate.append(can[c])
            
            # 하나만 검색이라면
            else :
                if q_carrer in can:
                    sub_candidate.append(can[q_carrer])

        candidate = sub_candidate
        sub_candidate = []

        # q_soulfood에 대한 검색 진행
        while candidate:

            can = candidate.pop()

            if q_soulfood == WILDCARD:
                soulfood_list = can.keys()

                for s in soulfood_list:
                    sub_candidate.append(can[s])
                
            else :
                if q_soulfood in can:
                    sub_candidate.append(can[q_soulfood])


        # 모든 검색이 끝났음, 이제 점수를 비교해서 통과한 지원자 수를 세면 된다.
        
        # 통과 지원자 수 계산 변수
        count = 0

        # 쿼리를 돌린 결과가 들어있는 2중 list에 대해서
        for score_list in sub_candidate:

            # 효율성 테스트 위해서 점수 검색을 Binary Search로 교체해보자
            # 이진탐색 적용해서 통과자 수 계산하기
            
            # 리스트 맨 처음, 리스트 맨 끝 다음 위치 처리용 투포인터 적용
            left = 0 
            right = len(score_list) 


            # 왼쪽이 오른쪽보다 커지기 전까지(추월되기 전까지)
            while left < right:

                # 중앙 위치 찾기
                mid = left + right // 2
        
                # 중앙 위치와 목표 점수 비교
                # 만약 중앙 값이 목표 점수보다 작으면, 탐색범위는 우측으로 가야 함
                if score_list[mid] < q_score:
                    left = mid + 1
                
                #만약 중앙 값이 목표 점수보다  크면, 탐색 범위는 좌측으로 가야 함
                elif score_list[mid] >= q_score:
                    right = mid

        answer.append(count)

    return answer