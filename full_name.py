full_name = str(input("Please enter your full name"))
stripped_full_name = full_name.strip()
parts = stripped_full_name.split(' ')
if stripped_full_name == "":
    print("Please enter your name")
elif len(stripped_full_name) < 4:
    print("You have entered entered less than 4 characters. Please make sure you have entered your name and surname")
elif  len(stripped_full_name) > 25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name") 
elif len(parts) == 2:
    print("Thank you for entering your name")
else:
    print("Please enter your full name")
