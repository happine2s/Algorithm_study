li=[int(input()) for _ in range(5)]

minum=2000
for i in range(3):
	s=li[i]+li[3]
	minum=s if minum>s else minum
	s=li[i]+li[4]
	minum=s if minum>s else minum
print(minum-50)