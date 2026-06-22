def solution(n, computers):
    answer = 0

    # 해당 컴퓨터가 이미 네트워크에 연결이 되어있는지 여부를 판단하는 방문배열
    visited_list = [0] * n 

    
    # 1. n에 대해서 루프 돌리기
    # 2. n번째 computer의 연결정보 확인을 위해서, computers에서 n번째 인덱스에 대해
    # loop를 돌려 네트워크 연결점 확인하기
    # 3. 재귀로 돌려서 끝까지 네트워크 닿을 수 있는 곳 까지 나아가기,
    # 4. 방문 배열에 방문한 곳은 1표시를 박아두어서 추가방문 안해도 되게 하기

    def dfs(idx):

        # 이미 방문을 했어서 네트워크 연결 필요가 없으면 return 스킵
        if visited_list[idx] == 1:
            return
        
        # 해당 컴퓨터 방문 처리
        visited_list[idx] = 1
        
        # 해당 컴퓨터의 네트워크 배열에 대한 루프
        for j in range(n):

            # 연결되어 있고 방문한 적이 없다면
            if computers[idx][j] == 1 and visited_list[j] == 0:

                # 재귀
                dfs(j)    
        

    # n에 대해서 루프 돌리기
    for i in range(n):

        # 방문하지 않은 노드에 대해서만
        if visited_list[i] == 0:

            # dfs 실행 (네트워크 연결된 노드들 다 찾아서 방문처리)
            dfs(i)

            # 
            answer += 1
        

    
    return answer