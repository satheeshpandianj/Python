# 🚨 Don't change the code below 👇
row1 = ["1","2","3"]
row2 = ["4","5","6"]
row3 = ["7","8","9"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

column = int(position[0])
print(column)

row = int(position[1])
print(row)

# selected_field = map[row-1][column-1]
# print(selected_field)
map[row-1][column-1] = "x"
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")