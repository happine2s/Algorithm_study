n=int(input())
li=[list(input()) for _ in range(n)]

for i in li:
	cnt,w=0,0
	for j in i:
		if j=='X':
			w=0
		elif j=='O':
			w+=1
			cnt+=w
	print(cnt)
