dx = [1, 1, 1, -1, -1, -1, 0, 0]
dy = [1, -1, 0, 1, -1, 0, 1, -1]

def check(x, y, n, m):
    return x >= 0 and x < n and y >= 0 and y < m

def dfs_mod(a, x0, y0, n, m):
    for i in range(8):
        if  check(x0 + dx[i], y0 + dy[i], n, m) and a[x0 + dx[i]][y0 + dy[i]] == 1:
            a[x0 + dx[i]][y0 + dy[i]] = 2
            dfs_mod(a, x0 + dx[i], y0 + dy[i], n, m)

def findIslands(a,n,m):
    # used = [[0 for i in range(m)] for j in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                a[i][j] = 2
                dfs_mod(a, i, j, n, m)
                cnt += 1
                
    return cnt
            

n, m = map(int, input().split())

l = []

for i in range(n):
    x = list(map(int, input().split()))
    l.append(x)

print(findIslands(l, n, m))
