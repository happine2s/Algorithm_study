n=int(input())
nli=sorted(list(map(int,input().split())))
m=int(input())
mli=list(map(int,input().split()))

def binary(l,r,n):
	global nli
	mid=(l+r)//2

	if l<=r:
		if nli[mid]==n:
			print('1',end=' ')
			return
		elif nli[mid]>n:
			return binary(l,mid-1,n)
		else:
			return binary(mid+1,r,n)
	else:
		print('0',end=' ')
		return


l,r=0,len(nli)-1

for i in mli:
	binary(l,r,i)