# Functions with outputs

def format_name(first,last):
    return f"{first.title()} {last.title()}"

first_name = input("Enter your first name: \n")
last_name = input("Enter your last name: \n")

final_name = format_name(first_name,last_name)

print(final_name)    