def solution(numbers, target):
    answer = 0
    
    # 숫자 길이
    N = len(numbers)

    #DFS 메서드  정의
    def dfs(idx, current_sum):

        nonlocal answer

        # 이미 끝까지 숫자를 다 썼다면
        if idx == N:

            # target 값과 비교 검증 진행
            if current_sum == target:
                answer += 1
            return
        
        dfs (idx + 1, current_sum=current_sum + numbers[idx])
        dfs (idx + 1, current_sum=current_sum - numbers[idx])
    

    dfs(0, 0)





    return answer