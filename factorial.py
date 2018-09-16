x=int(input("Enter the number you want to find factorial of "))
i=0
z=1
for i in range(x):
	z*=(x-i)
print(z)
