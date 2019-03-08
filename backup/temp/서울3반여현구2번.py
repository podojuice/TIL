# 2번

T = int(input())


def check(i, j):
    global max_h
    if M[i][j] > max_h:
        max_h = M[i][j]
    visit[i][j] = True
    route = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for k in range(len(route)):
        a, b = i+route[k][0], j+route[k][1]
        if a >= 0 and a <= N-1 and b >= 0 and b <= N-1:
            if M[a][b] != 0 and not visit[a][b]:
                check(a, b)


for test_case in range(1, T+1):
    N = int(input())

    M = []
    visit = [[False for _ in range(N)] for _ in range(N)]

    for i in range(N):
        M.append(list(map(int, input().split())))

    max_h = 0

    island = 0

    for i in range(N):
        for j in range(N):
            if M[i][j] != 0 and not visit[i][j]:
                check(i, j)
                island += 1

    print('#{} {} {}'.format(test_case, island, max_h))
