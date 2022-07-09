n=int(input())
li=[list(input().split()) for _ in range(n)]

for i in range(n):
	li[i].reverse()
	print('Case #%d: '%(i+1),end='')
	for j in li[i]:
		print(j,end=' ')
	print()