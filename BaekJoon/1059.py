l=int(input())
setli=list(map(int,input().split()))
n=int(input())

setli.append(0)
setli.sort()

cnt=0
for i in range(l):
	if setli[i]==n:
		cnt=0
		break
	elif setli[i]<n and setli[i+1]>n:
		cnt=(n-setli[i])*(setli[i+1]-n)-1
		break

print(cnt)