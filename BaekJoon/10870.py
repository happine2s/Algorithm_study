def fibo(n):
	if n==1:
		return 1
	elif n>0:
		return fibo(n-1)+fibo(n-2)
	else:
		return 0

print(fibo(int(input())))