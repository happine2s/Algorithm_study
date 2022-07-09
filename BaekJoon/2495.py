li=[list(input()) for _ in range(3)]

for i in range(3):
	w,mx=0,0
	for j in range(7):
		if li[i][j]==li[i][j+1]:
			w+=1
		else:
			w=0
		if w>mx:
			mx=w
	print(mx+1)
