n=int(input())
li=[list(map(int,input().split())) for _ in range(n)]
cnt=[]
ch=[[0]*n for _ in range(n)] #행번 학생이 열번 학생과 같은 반->1 다른 반->0

for i in range(5): #학년 별
	z=0
	for j in range(n): #학생 별
		z=j+1 #j번 학생과 비교할 학생
		while z<n:
			if li[j][i]==li[z][i]:
				ch[j][z]=1
				ch[z][j]=1
			z+=1

for i in ch:
	cnt.append(i.count(1))

print(cnt.index(max(cnt))+1)