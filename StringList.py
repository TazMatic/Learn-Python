#getting my user input
string = str(input("Please enter a word:"))
#conditioning input 
string = string.replace(' ','')
string = string.lower()
Rev_String = string[::-1]
#check the strings to see if they are equal and return result
if string == Rev_String:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
