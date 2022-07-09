import sys 
sys.setrecursionlimit(10000)

def dfs(x,y,h):
	if x<0 or x>=n or y<0 or y>=n:
		return
	if graph[x][y]>h and visited[x][y]==0:
		visited[x][y]=1

		dfs(x+1,y,h)
		dfs(x-1,y,h)
		dfs(x,y+1,h)
		dfs(x,y-1,h)
	return

n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]
maxsafe=1

for h in range(min(map(min,graph)),max(map(max,graph))+1):
	cnt=0
	visited=[[0]*n for _ in range(n)]
	for i in range(n):
		for j in range(n):
			if graph[i][j]>h and visited[i][j]==0:
				visited[i][j]=1
				cnt+=1
				dfs(i,j,h)
		print(h,cnt)
	if maxsafe<cnt:
		maxsafe=cnt

print(maxsafe)
