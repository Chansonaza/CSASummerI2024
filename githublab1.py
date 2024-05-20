# Prompt user to enter the minutes (e.g., 1 billion), and displays the number of years and days for the minutes. 
# Sample run:
# Enter the number of minutes:  1000000000
# 1000000000 minutes is approximately 1902 years and 214 days

input = eval(input("Enter the minutes: "))
day = input//(60*24)
year = day//365
remain = day % 365
print(f"{input} minutes is approximately {year} years and {remain} days")
