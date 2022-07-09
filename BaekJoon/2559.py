n,k=map(int,input().split())
li=list(map(int,input().split()))

sm=0
for i in range(k):
	sm+=li[i]

mx=[sm]

for i in range(0,n-k):
	sm-=li[i]
	sm+=li[i+k]
	mx.append(sm)

print(max(mx))