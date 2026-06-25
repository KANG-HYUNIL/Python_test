def solution(begin, target, words):
    answer = 0

    # 각 문자열 상태를 이미 방문하였는지 여부를 보관하는 dict
    visited_dict = dict()

    # 시작 문자열 start에서, 변환된 문자열 end로 변환을 시도할 때에 한 알파멧만의 변환으로 가능한지를 검증하는 메서드

    def check_string(start, end):

        diff_cnt = 0

        # 문자열에 대한 하나하나 검증 루프 진행
        for i in range(len(start)):

            # 만약 문자열이 같다면 continue
            if start[i] == end[i]:
                continue
            
            # 문자열이 다른 위치가 잇다면 cnt 증가
            diff_cnt += 1

        # 문자열이 다른 개수가 한 개면 True, 아니면 False 반환 하게 처리
        return diff_cnt == 1

    # BFS Loop용 list 구축
    global_queue = []
    
    # 정답 찾음 여부 변수
    find_solution = False

    # 최초 시작 단어 집어넣기
    global_queue.append(begin)

    while global_queue:

        this_loop_queue = []

        #global_queue에 있는 모든 것들으 다 pop해서 빼서 비워두기
        for i in range(len(global_queue)):
            this_loop_queue.append(global_queue.pop())

        local_queue = []

        # 이번 loop_queue들의 단어들을 하나하나 검증해보기

        for j in range(len(this_loop_queue)):


            # 이번 Loop에서 볼 단어 ㅊ획득
            cur_word = this_loop_queue.pop()

            #이미 정답을 찾았다면, break
            if cur_word == target:
                find_solution = True
                break

            
            # 단어 list들에 대한 loop
            for word in words:

                # 변환 가능한 시작 -> 끝 문자열이고, 끝 문자열에 도달한 적이 없다면
                if check_string(cur_word, word) and word not in visited_dict:

                    # local_queue에 이번 끝 단어 추가
                    local_queue.append(word)

                    # 해당 끝 단어의 도달 했음 기록 표시
                    visited_dict[word] = True

        # 이번 Loop에서 찾고자 하는 정답을 찾앗다면, break
        if find_solution:
            break

        # 변횐 횟수에 1 증가
        answer += 1

        # 다음 외부 BFS loop에서 봐야 할 단어들 전달해주기
        global_queue = local_queue


    if not find_solution:
        answer = 0

    
    return answer