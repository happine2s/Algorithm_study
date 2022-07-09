num=int(input())
n=0
t=num
while True: 
	if t<10:
		cyc=t
		cyc=(t*10)+(cyc%10)
	else:
		cyc=int(t/10)+(t%10)
		cyc=(t%10)*10+(cyc%10)
	n+=1
	if num==cyc:
		break
	else:
		t=cyc

print(n)

