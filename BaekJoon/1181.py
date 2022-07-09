n=int(input())
li=[]
dic={}
for i in range(n):
	li.append(str(input()))

li.sort()
for i in range(n):
	dic[li[i]]=len(li[i])
li=sorted(dic,key=dic.get)

for i in li:
	print(i)




