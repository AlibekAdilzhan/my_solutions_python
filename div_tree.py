cnt = 0

def dfs(j, used, g, n):
    used[j] = 1
    global cnt
    for i in range(n):
        if used[i] == 0 and g[j][i] == 1 and used2[i] == 0:
            used[i] = 1
            cnt += 1
            dfs(i, used, g, n)


t = int(input())

ans = []

for i in range(t):


    n, m = map(int, input().split())
    used = [0 for i in range(n)]
    used2 = [0 for i in range(n)]
    l = list(map(int, input().split()))
    g = [[0 for i in range(n)] for j in range(n)]

    for i in range(0, len(l), 2):
        g[l[i] - 1][l[i + 1] - 1] = 1
        g[l[i + 1] - 1][l[i] - 1] = 1

    cnt_edges = 0


    for i in range(n):
        for j in range(n):
            used[i] = 1
            if g[i][j] == 1 and used[j] == 0 and used2[j] == 0:
                dfs(j, used, g, n)
                if cnt > 0 and (cnt + 1) % 2 == 0:
                    g[i][j] = 0
                    g[j][i] = 0
                    cnt_edges += 1
            cnt = 0
            used = [0 for k in range(n)]
        used2[i] = 1

    ans.append(cnt_edges)

for i in ans:
    print(i)

