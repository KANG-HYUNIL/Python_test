TC = 10

for t in range(1, TC + 1):

    N = int(input())

    box_height_list = list(map(int, input().split()))

    answer = 0
    for i in range(N):

        top_value = max(box_height_list)
        min_value = min(box_height_list)

        if top_value - min_value <= 1:
            break

        top_index = box_height_list.index(top_value)
        min_index = box_height_list.index(min_value)

        box_height_list[top_index] -= 1
        box_height_list[min_index] += 1



    answer = max(box_height_list) - min(box_height_list)

    print(f"#{t} {answer}")


