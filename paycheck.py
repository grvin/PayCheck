# program to calulate gross pay for a given wage or salary
# convert wage to salary and vice versa
# calculate tax deductions
import math
print('Do you make a salary or a wage?')
# take input options
var = int(input('Press (1) for wage\nPress (2) for salary\n'))

# method to make sure input is valid

def getFloat(prompt):
    # start with while loop, contents must be true to loop
    while True:
        try:
            # take input as float
            value = float(input(prompt))
        except ValueError:  # exception if value is not float
            print('Please enter a valid value')
            continue
        # statement if value is less than 0
        if value < 0:
            print('Try inputting a positive value')
            continue
        else:
            break
    return value


if var == 1:

    # NEW WAY with float method, still store as vars
    wage = getFloat('Enter your wage: \n--> ')
    hours = getFloat(
        'How many hours did you work in your last pay period?\n--> ')
    payPeriod = getFloat('You get paid every __ weeks?\n--> ')

    payCheck = round(wage * hours, 2)

    # define method to calculate salary for 3 common pay periods
    def wage2salary():
        salary = payPeriod*payCheck
        if payPeriod == 1:
            salary *= 52
        if payPeriod == 2:
            salary *= 26
        if payPeriod == 4:
            salary *= 13
        return round(salary, 2)

    # print data and converto to strings
    print('Gross Paycheck: $' + str(payCheck))
    print('Yearly Salary for consistant work: $' + str(wage2salary()))
    input('Press *Enter* for Net Paycheck...')
    print('Net Paycheck: Taxation is theft, it should be the same damn amount!')
    print('Tax deductions not calculated, taxes are hard')

# create separate methods to do bracket calculations


def bracketCalcSingle():
    # upper bound of tax brackets
    brac1, brac2, brac3, brac4, brac5, brac6, brac7 = 9875, 40125, 85525, 163300, 207350, 518400, math.inf
    # tax rate for each bracket
    tax1, tax2, tax3, tax4, tax5, tax6, tax7 = .1, .12, .22, .24, .32, .35, .37
    # satic value of decucted tax after each bracket is passed
    deduct1, deduct2, deduct3, deduct4, deduct5, deduct6 = 987.5, 4815, 18815.5, 39192, 66352, 181440

    def netPay():
        netPay = (salary - taxDeduct)/24
        print('Semi-monthly Net Paycheck ' + str(netPay))

    # bracket 1
    if salary <= brac1:
        taxDeduct = (salary * tax1)
        netPay()
    
    #bracket 2
    if brac1 <= salary < brac2:
        taxDeduct = (salary - brac1) * tax2 + deduct1
        netPay()

    # bracket 3
    if brac2 <= salary < brac3:
        taxDeduct = (salary - brac2) * tax3 + deduct1 + deduct2
        netPay()

    # bracket 4
    if brac3 <= salary < brac4:
        taxDeduct = (salary - brac3) * tax4 + deduct1 + deduct2 + deduct3
        netPay()

    # bracket 5
    if brac4 <= salary < brac5:
        taxDeduct = (salary - brac4) * tax5 + deduct1 + \
            deduct2 + deduct3 + deduct4
        netPay()

    # bracket 6
    if brac5 <= salary < brac6:
        taxDeduct = (salary - brac5) * tax6 + deduct1 + \
            deduct2 + deduct3 + deduct4 + deduct5
        netPay()

    # bracket 7
    if brac6 <= salary < brac7:
        taxDeduct = (salary - brac6) * tax7 + deduct1 + \
            deduct2 + deduct3 + deduct4 + deduct5 + deduct6
        netPay()

    

def bracketCalcMarriedJointly():
    # upper bound of tax brackets
    brac1, brac2, brac3, brac4, brac5, brac6, brac7 = 19750, 80250, 171050, 326600, 414700, 622050, math.inf
    # tax rate for each bracket
    tax1, tax2, tax3, tax4, tax5, tax6, tax7 = .1, .12, .22, .24, .32, .35, .37
    # satic value of decucted tax after each bracket is passed
    deduct1, deduct2, deduct3, deduct4, deduct5, deduct6 = 1975, 9630, 37631, 78384, 132704, 217717.5

    def netPay():
        netPay = (salary - taxDeduct)/24
        print('Semi-monthly Net Paycheck ' + str(netPay))

    # bracket 1
    if salary <= brac1:
        taxDeduct = (salary * tax1)
        netPay()
    
    #bracket 2
    if brac1 <= salary < brac2:
        taxDeduct = (salary - brac1) * tax2 + deduct1
        netPay()

    # bracket 3
    if brac2 <= salary < brac3:
        taxDeduct = (salary - brac2) * tax3 + deduct1 + deduct2
        netPay()

    # bracket 4
    if brac3 <= salary < brac4:
        taxDeduct = (salary - brac3) * tax4 + deduct1 + deduct2 + deduct3
        netPay()

    # bracket 5
    if brac4 <= salary < brac5:
        taxDeduct = (salary - brac4) * tax5 + deduct1 + \
            deduct2 + deduct3 + deduct4
        netPay()

    # bracket 6
    if brac5 <= salary < brac6:
        taxDeduct = (salary - brac5) * tax6 + deduct1 + \
            deduct2 + deduct3 + deduct4 + deduct5
        netPay()

    # bracket 7
    if brac6 <= salary < brac7:
        taxDeduct = (salary - brac6) * tax7 + deduct1 + \
            deduct2 + deduct3 + deduct4 + deduct5 + deduct6
        netPay()

    # CONTINUE...
    # ********************


if var == 2:
    # take input as float
    salary = float(input('What is you annual salary?\n--> '))
    # most salaries are payed out bi-monthly
    semiMonthly = salary/24
    # claculate and round payout
    print('Semi-monthly Gross Paycheck: ' + str(round(semiMonthly, 2)))
    # calculate tax
    yesNoTax = (input('Do you want to calculate Net Paycheck? ').upper())
    if yesNoTax == 'YES':
        fileStatus = int(input(
            'Select filing status:\n1) Single\n2) Married Jointly\n3) Married Separatley\n4) Head of Household\n(press number then enter)\n--> '))
        if fileStatus == 1:
            # status is single, call method for single filers
            bracketCalcSingle()
        if fileStatus == 2:
            # status is Married & filing jointly
            bracketCalcMarriedJointly()

    if yesNoTax == 'NO':
        print('Goodbye')
