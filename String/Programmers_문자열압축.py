def solution(s):
    answer = 1
    
    #문자열의 길이
    N = len(s)
    
    # 압축할 문자열 단위 길이를 i로
    for i in range(1, N//2 + 1):
        
        # 압축된 문자열 저장용 리스트
        compressed_str_list = []
        
        #현재 문자열 위치 idx
        current_idx = 0
        
        
        while True:
            
            #탈출 조건문
            if current_idx >= N :
                break
            
            
            cur_str = s[current_idx : current_idx + i]
            
            repeat_cnt = 1
            
            while True:
                
                # 끝까지 간 경우
                if current_idx + i * repeat_cnt >= N :
                    break
                    
                if cur_str == s[current_idx + i * repeat_cnt : current_idx + i * (repeat_cnt + 1)] :
                    repeat_cnt += 1
                
                else : 
                    break
            
            current_idx += repeat_cnt * i
            
            #압축된 문자열 삽입
            if repeat_cnt > 1:
                compressed_str = str(repeat_cnt) + cur_str
                compressed_str_list.append(compressed_str)
            else:
                compressed_str_list.append(cur_str)
            
        # 문자열 압축된 것들 합치기
        
        final_comp_str = "".join(compressed_str_list)
        
        answer_candidate = len(final_comp_str)
        
        if answer == 1:
            answer = answer_candidate
        else:
            answer = min(answer, answer_candidate)
        

        
    
    return answer