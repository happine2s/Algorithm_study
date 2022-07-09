n,m=map(int,input().split())
nli=list(map(int,input().split()))
mli=list(map(int,input().split()))

nli.extend([0]*1000)
mli.extend([1001]*1000)
cur,i=0,0
while i<m:
	if nli[cur]>mli[i]:
		cur+=1
	else:
		nli[cur]-=mli[i]
		i+=1

cnt=0
for i in nli:
	cnt+=i

print(cnt)