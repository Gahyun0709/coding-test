# 11279.py
# 최대 힙

import heapq
import sys

input = sys.stdin.readline

n = int(input())

q = []
for _ in range(n):
    num = int(input())
    
    if num == 0:
        if len(q) == 0:
            print(0)
        else:
            print(-heapq.heappop(q))
    else:
        heapq.heappush(q, -num)