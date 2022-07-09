while True:
	li=list(map(int,input().split()))
	if li==[0,0,0]:
		break
	li.sort()
	if li[0]*li[0]+li[1]*li[1]==li[2]*li[2]:
		print('right')
	else:
		print('wrong')
