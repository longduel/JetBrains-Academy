from math import log, pow, ceil, floor
import argparse
from types import NoneType

parser = argparse.ArgumentParser()

parser.add_argument('--type', choices=["diff", "annuity"], help='choice of the payment')
parser.add_argument('--principal', type=int, help='loan principal')
parser.add_argument('--payment', type=int, help='monthly payment')
parser.add_argument('--interest', type=float, help='loan interest')
parser.add_argument('--periods', type=int, help='number of periods')

args = parser.parse_args()

def main_calculus():
    if args.type == 'diff':
            differentiated_payment()
    elif args.type == 'annuity':
        if type(args.principal) == NoneType:
            loan_principal()
        elif type(args.payment) == NoneType:
            annuity_payment()
        elif type(args.periods) == NoneType:
            monthly_payments()

def monthly_payments():
    nominal_interest = (args.interest / 100) / 12 * 1
    n_of_months = ceil(log(args.payment / (args.payment - nominal_interest * args.principal), nominal_interest + 1))
    if n_of_months % 12 == 0: 
        year = round(n_of_months / 12)
        print(f"It will take {year} years to repay this loan!")
    elif n_of_months % 12 != 0:
        year = floor(n_of_months / 12)
        month = n_of_months % 12
        print(f"It will take {year} years and {month} months to repay this loan!")

def annuity_payment():
    nominal_interest = (args.interest / 100) / 12 * 1
    annuity_pay = ceil(args.principal * ((nominal_interest * pow(1 + nominal_interest, args.periods)) / (pow(1 + nominal_interest, args.periods) - 1)))
    overpayment = args.periods * annuity_pay - args.principal 
    print(f"Your monthly payment = {annuity_pay}!")
    print(f"Overpayment = {overpayment}")

def loan_principal():
    nominal_interest = (args.interest / 100) / 12 * 1
    principal = round(args.payment / ((nominal_interest * pow(1 + nominal_interest, args.periods)) / (pow(1 + nominal_interest, args.periods) - 1)))
    #principal = round(args.annuity / ((nominal_interest * pow(1 + nominal_interest, args.periods)) / (pow(1 + nominal_interest, args.periods) - 1)))
    print(f"Your loan principal = {principal}!")

def differentiated_payment():
    if args.principal == NoneType or args.periods == NoneType or args.interest == NoneType:
        print("Invalid parameters")
    else:
        nominal_interest = (args.interest / 100) / 12 * 1
        counter = 1
        overpayment = 0
        for i in range(args.periods):
            result = ceil((args.principal / args.periods) + nominal_interest * (args.principal - ((args.principal * (counter - 1) / args.periods))))
            overpayment += result
            print(f"Month {counter}: payment is {result}")  
            counter += 1
        overpayment -= args.principal
        print(f"Overpayment = {overpayment}")
    
if type(args.principal) == NoneType and type(args.payment) == NoneType:
    print("Incorrect parameters")
elif type(args.type) == NoneType:
    print("Incorrect parameters")
elif args.principal < 0 or args.payment > 0 or args.interest > 0 or args.periods > 0:
    print("Incorrect parameters")
else:
    main_calculus()
        