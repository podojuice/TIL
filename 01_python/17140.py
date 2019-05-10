import sys

sys.stdin = open('17140.txt')


def cal():
    global result, number, max_r, max_c
    if L[r-1][c-1] == k:
        result = number
        return
    if number > 100:
        return
    number += 1
    if max_c > max_r:
        cal_c()
    else:
        cal_r()


def cal_c():
    global max_c, max_r
    temp_r = max_r
    for p in range(max_c):
        temp = []
        dp = [0] * 101
        for q in range(temp_r):
            dp[L[q][p]] += 1
        for q in range(1, 101):
            if dp[q]:
                temp.append([dp[q], q])
        temp.sort()
        max_r = max(max_r, len(temp) * 2)
        cnt = 0
        for x in temp:
            for y in range(len(x)):
                L[cnt][p] = x[-y - 1]
                cnt += 1
        if temp_r > cnt:
            for x in range(cnt, temp_r):
                L[x][p] = 0
    cal()

def cal_r():
    global max_r, max_c
    temp_c = max_c
    for p in range(max_r):
        temp = []
        dp = [0] * 101
        for q in range(temp_c):
            dp[L[p][q]] += 1
        for q in range(1, 101):
            if dp[q]:
                temp.append([dp[q], q])
        temp.sort()
        max_c = max(max_c, len(temp)*2)
        cnt = 0
        for x in temp:
            for y in range(len(x)):
                L[p][cnt] = x[-y-1]
                cnt += 1
        if temp_c > cnt:
            for x in range(cnt, temp_c):
                L[p][x] = 0

    cal()


r, c, k = map(int, input().split())

L = [[0]*100 for _ in range(100)]
temp = []
for _ in range(3):
    temp.append(list(map(int, input().split())))

for i in range(3):
    for j in range(3):
        L[i][j] = temp[i][j]


max_r = max_c = 3

result = -1
number = 0


cal()

print(result)
