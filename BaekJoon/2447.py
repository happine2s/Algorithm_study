def pattern(n):
	global pat

	if n==3: #반복 패턴 초기 설정
		pat[0][:3],pat[1][:3]=['*','*','*'],['*',' ','*']
		pat[2][:3]=['*','*','*']
		return

	k=n//3
	pattern(k)
	for i in range(3): #n패턴은 n/3패턴으로 3*3(2차원 배열->i,j)
		for j in range(3):
			if i==1 and j==1: #가운데 공백
				continue
			for z in range(k): #n/3패턴을 복사하기 위해 n/3^2패턴에 접근
				pat[i*k+z][j*k:(j+1)*k]=pat[z][0:k] #16

n=int(input())
pat=[[' ' for i in range(n)] for i in range(n)]
pattern(n)
for i in pat:
	for j in i:
		print(j,end='')
	print('')