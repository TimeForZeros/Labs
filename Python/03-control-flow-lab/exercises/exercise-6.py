# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the season (Jan - Dec):
# 2. Then propts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

month = input('Enter the month of the season in three characters: ')
month = month.upper()
day = input('Endter the day of the month: ')

if month in ['DEC', 'JAN', 'FEB', 'MAR']:
    if month == 'MAR' and int(day) > 19:
        print(f'{month} {day} is in Spring')
    elif month == 'DEC' and int(day) <=20:
        print(f'{month} {day} is in Fall')
    else:    
        print(f'{month} {day} is in Winter')

elif month in ['MAR', 'APR', 'MAY', 'JUN']:
    if month == 'JUN' and int(day) > 20:
        print(f'{month} {day} is in Summer')
    else:
        print(f'{month} {day} is in Spring')

elif month in ['JUN', 'JUL', 'AUG', 'SEP']:
    if month == 'SEP' and int(day) > 21:
        print(f'{month} {day} is in Fall')
    else:
        print(f'{month} {day} is in Summer')

elif month in ['SEP', 'OCT', 'NOV', 'DEC']:
    if month == 'DEC' and int(day) > 20:
        print(f'{month} {day} is in Winter')
    else:
        print(f'{month} {day} is in Fall')