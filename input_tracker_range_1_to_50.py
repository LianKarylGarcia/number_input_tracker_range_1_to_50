# Set a valid number range from 1 to 50.
ranges = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

# Ask the user for input.
while True: # using loop
    try: # using try and except incase of an error
        num = int(input("Please enter a number between 1 and 50: "))
    except ValuError:
        break
    



# Next, assign ranges: Range 1 for 1–10, Range 2 for 11–20, Range 3 for 21–30, Range 4 for 31–40. Range 5 for 41–50
# Set a count for all ranges to 0.
# Count each user input, adding it to the respective range based on the number they input.
# If the user input is invalid, print "Invalid input" and display the results.