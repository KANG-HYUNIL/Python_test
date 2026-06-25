def solution(str1, str2):
    answer = 0

    MUL = 65536


    #자카드 유사도 활용 필요.
    # 각 문자열에서 원소 중복 허용하는 다중집합을 적용해야 하므로,
    # dict등을 활용해서 접근할  수 있을 듯.

    # 대소문자 구분을 안하므로 우선 다 upper 처리
    upper_str1 = str1.upper()
    upper_str2 = str2.upper()


    # 양 문자열의 다중집합 원소 처리를 위한 dict
    dict_str1 = dict()
    dict_str2 = dict()


    # str1에 대한 두 글자씩 잘라서 원소 처리

    for idx1 in range(len(upper_str1) - 1):

        # 두 글자 잘라서 part 맏늘어내기
        part = upper_str1[idx1 : idx1 + 2]

        # 해당 part가 알파벳만 있는지 검증하기
        if part.isalpha():
            dict_str1[part] = dict_str1.get(part, 0) + 1


    # str2에 대한 두 글자 씩 잘라서 원소 처리

    for idx2 in range(len(upper_str2) - 1):

        # 두 글자 잘라서 part 만들어내기
        part = upper_str2[idx2 : idx2 + 2]

        # 해당 part의 알파벳만 존재 여부 검증
        if part.isalpha():
            dict_str2[part] = dict_str2.get(part, 0) + 1


    # str1 과 str2의 자카드 유사도 구하기(교집합과 합집합 동시에 구하기 시도)

    # 자카드 유사도 분자(교집합) 분모(합집합) 계산 위한 dict
    top_dict = dict()
    under_dict = dict()


    for key_str1, value_str1 in dict_str1.items():

        # 교집합 부터 검사 시도해보자

        # 만약 현재 str1에서 보는 key(part)가, str2에도 있으면 > 겹치는 part 존재한다는 것
        if key_str1 in dict_str2:

            # 우선 교집합부터 연산 처리 진행
            top_dict[key_str1] = min(value_str1, dict_str2[key_str1])

            # 그 후 합집합도 연산 처리 진행
            under_dict[key_str1] = max(value_str1, dict_str2[key_str1])


        # 현재 str1에서 보는 key가 str2에 없어서 > str1에만 존재하는 거라면
        else : 

            # 교집합 처리 필요 X, 합집합만 연산 처리 진행
            under_dict[key_str1] = value_str1

    for key_str2, value_str2 in dict_str2.items():


        # 현재 str2에서 보는 key part가 str1에도 있으면, 
        # 이미 위의 str1 루프에서 겹치는 part에 대한 처리는 햿지만,
        # 한 번 더 반복하도록 하자 우선

        if key_str2 in dict_str1:

            top_dict[key_str2] = min(value_str2, dict_str1[key_str2])

            under_dict[key_str2] = max(value_str2, dict_str1[key_str2])

        else : 

            under_dict[key_str2] = value_str2



    # 구한 자카드 유사도 값에 상수 곱셈 및 소숫점 버리기

    sum_top = 0

    for key, value in top_dict.items():
        sum_top += value

    sum_under = 0

    for key, value in under_dict.items():
        sum_under += value

    # 교집합과 합집합이 모두 다 공집합이면  1로 정의됨(알파벳이 아예 안들어올 경우 대응)
    if sum_top == 0 and sum_under == 0 :
        answer = 1 * MUL
        return answer

    answer = int((sum_top / sum_under) * MUL)
    return answer