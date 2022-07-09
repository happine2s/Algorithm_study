a,b=map(int,input().split())
c=a-b
if c<0:
	print('<')
elif c>0:
	print('>')
else:
	print('==')