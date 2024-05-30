# Identify the bugs in the code and correct them.

# Corrected code:

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

food_preference = input("Are you a vegetarian? (yes/no) ")
if food_preference == "yes":
    print("We would recommend 'Veggie Delight Caterers'.")
else:
    print("We would recommend 'Gourmet Meals Caterers'.")