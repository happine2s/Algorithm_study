n=int(input())
li=[]
cnt, last=0,0
for i in range(n):
	st, end=map(int,input().split())
	li.append([st,end])
li=sorted(li, key=lambda i:i[0])
li=sorted(li, key=lambda i:i[1])

for i,j in li:
	if last<=i:
		last=j
		cnt+=1

print(cnt)