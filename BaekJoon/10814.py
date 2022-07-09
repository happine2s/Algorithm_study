n=int(input())
li=[list(input().split()) for _ in range(n)]

li=sorted(li,key=lambda i:int(i[0]))

for i,j in li:
	print(i,j)