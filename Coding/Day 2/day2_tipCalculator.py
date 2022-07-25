#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print(f"Welcome to the tip calculator!")
total_bill = input("What was the total bill? $") 
tip = input("How much tip would you like to give? 10, 12, or 15?")
number_of_people = input("How many people to split the bill?")

total_amount = float(total_bill) + float(total_bill) * (int(tip) / 100 )
individual_share = total_amount / int(number_of_people)
individual_share = "{:.2f}".format(individual_share) # write it for getting 33.60 value. Else it will print 33.6 though its 33.60
print(f"Each person should pay ${individual_share}")
