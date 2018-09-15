num=int(input("Enter a number you want to find prime of "))
i = 1
print(2)
while(i<=num):
	j = 2
	x=0
	while(j < i):
#		print("i is " ,i)
#		print("j is " ,j)
#		print("for number",i)
		if(i % j) != 0:
#			print("the number ",i , "is not a prime")
			x += 1
		else:
			x*=0
			break
		j +=1
	if(x!=0):
		print(i)
	i +=1
