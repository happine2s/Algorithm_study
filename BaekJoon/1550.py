hexa=list(input())
n=len(hexa)
cnt=0
m=1

while n>0:
	st=ord(hexa[n-1])
	if st>64:
		cnt+=(st-55)*m
	elif st>47:
		cnt+=(st-48)*m
	n=n-1
	m*=16

print(cnt)