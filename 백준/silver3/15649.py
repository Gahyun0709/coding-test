# 15649.py
# N과 M (1)

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, n + 1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

n, m = map(int, input().split())
s = []

dfs()