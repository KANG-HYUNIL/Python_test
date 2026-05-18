# N개 Node의 무방향 그래프. 
# Node 사이에는 무조건 Edge가 존재함.
# 모든 edge에는 양의 정수 가중치 weight 값이 존재함
# 길이가 N(N-1)/2 안 리스트에, 각 간선에 적혔던 가중치의 리스트?


# --- 문제 코드 ----

# TC 받기
TC = int(input())

# TC 만큼 loop
for i in range(TC):

    # 정수 N 받기
    N = int(input())


    # M개의 정수들 받기
    num_m = map(int, input().split())
    

