li=[int(input()) for _ in range(10)]
remain=[]
for i in li:
	i=i%42
	if i not in remain:
		remain.append(i)
print(len(remain))