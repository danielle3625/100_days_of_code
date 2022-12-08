print('Welcome to the tip calculator!')
total_bill =float(input('What was the total bill? $'))
tip_percent = float(input('How much tip percent would you like to give? 10, 12, or 15? '))
num_people = int(input('How many people to split the bill? '))

tip_amount = total_bill * (tip_percent/100)

bill_per_person = (total_bill + tip_amount) / num_people
bill_per_person = "{:.2f}".format(bill_per_person)

print(f'Each person should pay ${bill_per_person}')
