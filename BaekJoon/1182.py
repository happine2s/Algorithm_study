def dfs(v,seqsum):
	global cnt
	if v==n:
		return
	if seqsum+li[v]==s:
		cnt+=1
	dfs(v+1,seqsum)
	dfs(v+1,seqsum+li[v])

n,s=map(int,input().split())
li=list(map(int,input().split()))
cnt,seqsum=0,0
dfs(0,0)
print(cnt)