def dfs(graph,v,visited):
	global cnt
	visited[v]=True
	cnt+=1

	for i in graph[v]:
		if visited[i]==False:
			dfs(graph,i,visited)
	return cnt-1

n=int(input())
k=int(input())
graph=[
	[] for _ in range(n+1)
]
for _ in range(k):
	li=list(map(int,input().split()))
	graph[li[0]].append(li[1])
	graph[li[1]].append(li[0])
cnt=0

visited=[False]*(n+1)
print(dfs(graph,1,visited))