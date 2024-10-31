# Assign ranges: Range 1 for 1–10, Range 2 for 11–20, Range 3 for 21–30, Range 4 for 31–40. Range 5 for 41–50
range_1 = 1 - 10
range_2 = 11 - 20
range_3 = 21 - 30
range_4 = 31 - 40
range_5 = 41 - 50

# Set a count for all ranges to 0.
range_1_count = 0
range_2_count = 0
range_3_count = 0
range_4_count = 0
range_5_count = 0

while True: # Using loop to ask user for input
    try: # using try and except incase of an error

        num = int(input("Please enter a number between 1 and 50: ")) # To ask user for input

        # Using if statements to compare the user's input, based on the ranges, it will add 1 to the respective range count.
        if num >= 1 and num <= 10:
            range_1_count += 1
        elif num >= 11 and num <= 20:
            range_2_count += 1
        elif num >= 21 and num <= 30:
            range_3_count += 1
        elif num >= 31 and num <= 40:
            range_4_count += 1
        elif num >= 41 and num <= 50:
            range_5_count += 1
        else:
            print("Input Invalid. Processing Results...")
            break
        
    except ValueError:
        print("Input Invalid. Processing Results...")
        break # To break the loop if the input is invalid.

print(f"1 - 10 = {range_1_count}")
print(f"11 - 20 = {range_2_count}")
print(f"21 - 30 = {range_3_count}")
print(f"31 - 40 = {range_4_count}")
print(f"41 - 50 = {range_5_count}")





