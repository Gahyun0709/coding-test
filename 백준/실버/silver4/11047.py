# 11047.py
# 동전 0

n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)
count = 0
# 시간을 줄이기 위해 k가 0이면 break하는 조건을 걸면 더 좋다고 한다
for i in coins:
    count += k // i
    k %= i

print(count)