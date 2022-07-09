n=int(input())
li=list(map(int,input().split()))
li2=list(sorted(set(li)))
dic={}
for i in range(len(li2)):
	dic[li2[i]]=i
for i in li:
	print(dic[i],end=' ')