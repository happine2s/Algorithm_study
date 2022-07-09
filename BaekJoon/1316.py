n=int(input())
li=[list(input()) for _ in range(n)]
cnt=0
for i in li:
	flag=1
	abc=[0]*26
	for j in range(len(i)):
		if abc[ord(i[j])-97]==0:
			abc[ord(i[j])-97]=1
		elif i[j]==i[j-1]:
			continue
		else:
			flag=0
	if flag==1:
		cnt+=1
print(cnt)



