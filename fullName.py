full_name = str(input("Please enter your full name")) # Get the user's full name as input

stripped_full_name = full_name.strip() # Remove leading and trailing whitespaces from the input

parts = stripped_full_name.split(' ') # Split the full name into parts using space as a separator

if stripped_full_name == "": # Check different conditions based on the user's input
    
    print("Please enter your name")  # If the input is empty, prompt the user to enter their name
    
elif len(stripped_full_name) < 4: 
    
    print("You have entered entered less than 4 characters. Please make sure you have entered your name and surname") # If the length is less than 4 characters, prompt for a valid name and surname
    
elif  len(stripped_full_name) > 25:
    
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name") # If the length is more than 25 characters, prompt for only the full name

elif len(parts) == 2:
    
    print("Thank you for entering your name") # If there are exactly two parts in the name, consider it valid
    
else:
    print("Please enter your full name") # If none of the above conditions are met, prompt to enter the full name
