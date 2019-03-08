# 1번

T = int(input())


def sum_num(i, j):
    l_1 = l_2 = 0
    for p in range(K):
        l_1 += X[i + p][j + p]
        l_2 += X[i + (K - 1) - p][j + p]
    return abs(l_1 - l_2)


for test_case in range(1, T+1):
    N, K = map(int, input().split())

    X = []

    for i in range(N):
        X.append(list(map(int, input().split())))

    # 대각선 돌릴거 인덱스 구하기
    temp = []
    min_num = sum_num(0, 0)
    for i in range(N-K+1):
        for j in range(N-K+1):
            result = sum_num(i, j)
            if min_num > result:
                min_num = result

    print('#{} {}'.format(test_case, min_num))
