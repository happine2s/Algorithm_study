n=int(input())
li=list(map(int,input().split()))
li.sort()

cnt=0
for i in range(n):
	for j in range(i+1):
		cnt=cnt+li[j]

print(cnt)