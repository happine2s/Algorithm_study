scen=1
def func(o,w):
	global scen
	while True:
		status,num=input().split()
		if status=='F' and w>0:
			w+=int(num)
		elif status=='E' and w>0:
			w-=int(num)
		elif status=='#':
			break

	if o/2<w<o*2:
		print(scen,':-)')
	elif w<=0:
		print(scen,'RIP')
	else:
		print(scen,':-(')
	scen+=1

while True:
	o,w=map(int,input().split())
	if o==0 and w==0:
		break
	else:
		func(o,w)