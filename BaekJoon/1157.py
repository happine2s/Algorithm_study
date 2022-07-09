li=list(input().upper())
abc=[0]*26

for i in li:
	abc[ord(i)-65]+=1

if abc.count(max(abc))>1:
	print('?')
else:
	print(chr(abc.index(max(abc))+65))
