
# 주어진 숫자
N = 5
M = 2

# 방문 배열
visited = [False] * (N + 1)

#경로 처리 배열
path = []


#dfs 메서드
def dfs(cnt):

    # 개수 판별
    if cnt == M:
        return

    # 추출 진행
    for i in range(1, N + 1):

        #이미 방문했으면 스킵
        if visited[i]:
            continue

        visited[i] = True

        path.append(i)
        dfs(cnt + 1)

        path.pop()
        visited[i] = False


def main():
    print('Hello World')


if __name__ == "__main__":
    main()