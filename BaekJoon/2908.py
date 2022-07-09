i,j=map(int,input().split())
i=(i%10)*100+(((i//10)%10)*10)+(i//100)
j=(j%10)*100+(((j//10)%10)*10)+(j//100)
num=i if i>j else j
print(num)