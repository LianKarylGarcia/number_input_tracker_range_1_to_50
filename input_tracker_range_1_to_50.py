# Next, assign ranges: Range 1 for 1–10, Range 2 for 11–20, Range 3 for 21–30, Range 4 for 31–40. Range 5 for 41–50
range_1 = 1 - 10
range_2 = 11 - 20
range_3 = 21 - 30
range_4 = 31 - 40
range_5 = 41 - 50

ranges = {range_1: 0, range_2: 0, range_3: 0, range_4: 0, range_5: 0}

# Ask the user for input.
while True: # using loop
    try: # using try and except incase of an error
        num = int(input("Please enter a number between 1 and 50: "))

        # 
        if num >= 1 and num <= 10:
            ranges[range_1] += 1
        elif num >= 11 and num <= 20:
            ranges[range_2] += 1
        elif num >= 21 and num <= 30:
            ranges[range_3] += 1
        elif num >= 31 and num <= 40:
            ranges[range_4] += 1
        elif num >= 41 and num >= 50:
            ranges[range_5] += 
        
    
    except ValueError:
        break
    



# Set a valid number range from 1 to 50.
# Set a count for all ranges to 0.
# Count each user input, adding it to the respective range based on the number they input.
# If the user input is invalid, print "Invalid input" and display the results.