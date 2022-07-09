def binary(num,a,r,l):
	if r>l:
		return 0
	k=(r+l)//2

	if a[k]==num:
		return 1
	elif a[k]>num:
		return binary(num,a,r,k-1)
	else:
		return binary(num,a,k+1,l)

n=int(input())
a=sorted(list(map(int,input().split())))
m=int(input())
li=list(map(int,input().split()))

for i in li:
	print(binary(i,a,0,len(a)-1))
