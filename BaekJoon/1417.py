n=int(input())
li=[]
for i in range(n):
	li.append(int(input()))

cnt=0

while True:
	maxin=0
	if n==1:
		break
	for i in range(1,n):
		if li[maxin]<=li[i]:
			maxin=i
	if maxin==0:
		break
	else:
		li[maxin]-=1
		li[0]+=1
		#print('m',maxin)
		#print(li)
		cnt+=1

print(cnt)

