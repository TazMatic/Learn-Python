#!/usr/bin/python3
name = input("Please Enter Your Name:")
age = int(input("How Old Are You, {0} :".format(name)))
print(name,age)

if age>= 18:
    print("you are old enough to vote")
else:
     print("you can not vote yet, wait {0} more years".format(18-age))
