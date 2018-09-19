#get user input(int)
#print a list of all divisors for user input
User_Num = int(input("Enter a number please:"))
Divisors = []
for i in range(1,User_Num + 1,1):
	if User_Num % i == 0:
		Divisors.append(i)
print("The Divisors are: ", Divisors)


