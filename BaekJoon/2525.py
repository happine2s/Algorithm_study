a,b=map(int,input().split())
c=int(input())
h,m=a,b+c

while m>=60 or h==24:
	if m>=60:
		h+=1
		m-=60
	if h==24:
		h=0

print(h,m)
