# This program determines whether a permanent resident
# is eligible to apply for citizenship

MIN_AGE = 18  # The minimum age
MIN_YEARS = 5 # The minimum years residing in the United States
green_card = str(input("Do you have a green card? Enter Y or N: ").strip().upper())



# Determine whether the applicant is eligible to apply for citizenship
if green_card == 'N':
    print('You are not eligible to apply for citizenship')

else:
    age = float(input('Enter your age: '))

    # Get the number of years the applicant has lived in the US.
    years_in_US = int(input('Enter how many years' +
                         ' you have held your green card: '))
    
    if age >= MIN_AGE and years_in_US >= MIN_YEARS:
        print('You are eligible to apply for citizenship!')

    else: 
        print(f''' You are not eligible to apply for citizenship!, You need have resided in the US for {MIN_YEARS} years and be {MIN_AGE} years of age''')