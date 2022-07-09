n=int(input())
li=list(map(int,input().split()))
mx=0
dp=[1]*n

for i in range(n):
	cnt=1
	num=0
	for j in range(i):
		if li[i]>li[j]:
			num=li[j]
			
	dp[i]=cnt

print(dp)