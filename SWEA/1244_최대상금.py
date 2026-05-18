



TC = int(input())


for t in range(1, TC + 1):

    num, cnt = list(map(int, input().split()))

    visited = set()

    answer_list = []

    num_list = list(str(num))

    L = len(num_list)

    def dfs(count_dfs, num_list_dfs):


        # 이미 볼 데까지 다 보았으면 return
        if count_dfs == cnt :
            answer_candidate = int("".join(num_list_dfs))
            answer_list.append(answer_candidate)
            return


        joined_num = int("".join(num_list_dfs))

        #이미 했던 조합이라면
        if (count_dfs, joined_num) in visited: 
            return

        # 방문 배열에 넣어두기
        visited.add((count_dfs, joined_num))

        # 숫자 스와핑 위한 loop
        for i in range(L - 1):

            for j in range(i + 1, L):

                # 스와핑 진행
                num_list_dfs[i], num_list_dfs[j] = num_list_dfs[j], num_list_dfs[i]

 

                # dfs 진행하기?
                dfs(count_dfs=count_dfs+1, num_list_dfs=num_list_dfs)

                # 스와핑 다시 복구

                num_list_dfs[i], num_list_dfs[j] = num_list_dfs[j], num_list_dfs[i]
 

    dfs(0, num_list)

    print(f"#{t} {max(answer_list)}")

