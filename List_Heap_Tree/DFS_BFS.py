def dfs(v):
    visited[v] = True
    cc.append(v)
    for i in adj_list[v]:
        if not visited[i]:
            dfs(i)

adj_list = [[2,1],[3,0],[3,0],[9,8,2,1],[5],[7,6,4],[7,5],[6,5],[3],[3]]
N = len(adj_list)
visited = [False] * N
CCList = []

for i in range(N):
    if not visited[i]:
        cc = []
        dfs(i)
        CCList.append(cc)
print('연결성분리스트:');
print(CCList)