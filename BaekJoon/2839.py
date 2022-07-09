n=int(input())
five=0 #5로 나누었을 때 몫
three=0
f=0

for i in range(n//5,-1,-1):
	if (n-(i*5))%3==0:
		five=i
		three=(n-(i*5))//3
		f=1
		break

if f:
	print(five+three)
else:
	print(-1)
