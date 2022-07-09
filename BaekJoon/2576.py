cnt=0
minum=100
f=0
for i in range(7):
	n=int(input())
	if n%2==1:
		f=1
		cnt+=n
		if n<minum:
			minum=n

if f:
	print(cnt)
	print(minum)
else:
	print(-1)