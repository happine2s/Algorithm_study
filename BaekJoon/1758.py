n=int(input())
li=sorted([int(input()) for _ in range(n)],reverse=True)

tip=0

for i in range(n):
	if li[i]-i>0:
		tip+=li[i]-i

print(tip)