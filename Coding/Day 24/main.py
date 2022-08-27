# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()
#
# # with open("/Users/satheeshpandian.j/Desktop/my_file.txt") as file:
# with open("../../../../../../../Desktop/my_file.txt") as file:
#     contents = file.read()
#     print(contents)

with open("./Input/Letters/starting_letter.txt") as data:
    content = data.read()
    # print(content)

with open("./Input/Names/invited_names.txt", mode="r") as names:
    individual_name = names.readlines()
    # print(individual_name)

    for each_name in individual_name:
        each_name = each_name.strip()
        replaced_list = content.replace("[name]", each_name)
        with open(f"./Output/ReadyToSend/letters_to_{each_name}.txt", mode="w") as complete_letter:
            complete_letter.write(replaced_list)
