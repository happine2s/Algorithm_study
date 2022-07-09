n=int(input())

while True:
	f=True
	for i in str(n):
		if i!='4' and i!='7':
			n-=1
			f=False
	if f:
		print(n)
		break
