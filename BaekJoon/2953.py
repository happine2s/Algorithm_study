li=[list(map(int,input().split())) for i in range(5)]
win=0
cnt=0

for i in range(5):
	n=0
	for j in range(4):
		n+=li[i][j]
	if cnt<n:
		cnt=n
		win=i
print(win+1,cnt)