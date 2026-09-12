#Tip Calculator
try:
    print("Here is the tip calculator...!")
    total_bill = float(input("How much was the total bill : "))
    tip_given = float(input("How Much Percentage of tip do you want to give (10,12,15...): "))
    no_of_people = int(input("how many of you split this : "))
    tip_percentage = tip_given / 100
    bill_sharing = total_bill  / no_of_people
    indvl_share = bill_sharing + tip_percentage
    print(f"The induvidual share or tip is : {indvl_share} ")
except ValueError:
    print("Invalid Bill ..! ")