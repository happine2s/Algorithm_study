e,f,c=map(int,input().split())
cnt=0
i=e+f

while i>=c:
	i-=c
	cnt+=1
	i+=1
print(cnt)
