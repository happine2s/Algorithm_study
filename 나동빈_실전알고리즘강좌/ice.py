m,n=map(int,input().split()) #가로*세로
graph=[]

for i in range(n):
	graph.append(list(map(int,input())))

def dfs(x,y):
	if x<=-1 or x>=n or y<=-1 or y>=m:
		return False
	if graph[x][y]==0:
		graph[x][y]=1

		dfs(x,y+1)
		dfs(x,y-1)
		dfs(x-1,y)
		dfs(x+1,y)
		return True
	return False

cnt=0
for i in range(n):
	for j in range(m):
		if dfs(i,j)==True:
			cnt+=1
print(cnt)
