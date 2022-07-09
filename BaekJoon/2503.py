
import itertools
from itertools import permutations

n=int(input())
permut=list(itertools.permutations([1,2,3,4,5,6,7,8,9],3))

for i in range(n):
	li=list(map(int,input().split()))
	num=list(str(li[0]))

	for j in permut:
		strike, ball=0,0
		for z in range(3):
			if int(num[z]) in j:
				if int(num[z])==j[z]:
					strike+=1
				else:
					ball+=1
		if strike!=li[1] or ball!=li[2]:
			print(j)
			permut.remove(j)

print()
print(permut)
print(len(permut))
