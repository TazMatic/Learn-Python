Initial_List = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
Output_List = []
User_Input = int(input("Enter a number:"))
for i in Initial_List:
    if i < User_Input:
        Output_List.append(i)
print(Output_List)
