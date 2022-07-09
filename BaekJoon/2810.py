n=int(input())
li=list(input())
cnt,f=1,0

for i in li:
	if i=='S':
		cnt+=1
		#print('s+=1')
	elif i=='L' and f==1:
		cnt+=1
		f=0
		#print('l+=1')
	else:
		f=1
print(cnt if cnt<=n else n)