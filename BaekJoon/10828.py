n=int(input())
li=[input() for _ in range(n)]
stack=[]

for i in li:
	if 'push' in i:
		stack.append(i.split()[1])
	elif i=='pop':
		if len(stack)==0:
			print('-1')
		else:
			print(stack.pop())
	elif i=='size':
		print(len(stack))
	elif i=='empty':
		a=1 if len(stack)==0 else 0
		print(a)
	elif i=='top':
		a=-1 if len(stack)==0 else stack[-1]
		print(a)
