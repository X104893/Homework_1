#Automate the Calculations

loan_cost = [500,600,200, 1000, 450]
number_of_loans = len(loan_cost)
sum_of_loans =sum(loan_cost)
average_of_loans = sum_of_loans / number_of_loans
print(f'"There are {number_of_loans} total loans  and the sum of the loans is ${sum_of_loans}.')
print(f'"The average loan amount is ${average_of_loans}.')

#Analyze Loan Data 

loan = {
    "loan_price":500,
    "remaining_months" : 9,
    "repayment_interval":"bullet",
    "future_value":1000,
}
future_value = loan.get("future_value")
remaining_months =loan.get("remaining_months")
loan_price = loan.get("loan_price")

print(f'"The face value of the loan is ${future_value} and the loan needs to be repaid in {remaining_months} months."')

discount_rate = .20
PV = (future_value)/ 1 + (discount_rate) /12 **(remaining_months)

if PV > loan_price:
    print("The loan is worth more than the  cost to purchase it")
elif PV == loan_price:
    print("The loan will is worth the cost to buy it")
else:
    print("The loan is too expensive and not worth the price")

#Perform Financial Calculations

New_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
    "annual_discount_rate":.20,
}

def present_value_loan(New_loan):
    FV = New_loan.get("future_value")
    DR = New_loan.get("annual_discount_rate")
    RM = New_loan.get("remaining_months")
    PVNL =FV/(1+DR/12)**RM
    PVNLR = round(PVNL,2)
    print(f"The present value of the loan is:{PVNLR}.")

present_value_loan(New_loan)

#Conditionally filter list of loans

loans = [
    {"loan_price": 700,
    "remaining months": 9,
    "repayment_intervals":"monthly",
    "future_value": 1000,
    },
    {"loan_price": 500,
    "remaining_months": 13,
    "repayment_intervals": "bullet",
    "future_value": 1000,
    },
    {"loan_price": 200,
    "remaining_months":13,
    "repayment_interval": "bullet",
    "future_value": 1000,
    },
    {"loan_price": 900,
    "remaining_months": 16,
    "repayment_interval": "bullet",
    "future_value": 1000,
    }
]
inexpensive_loans =[]
expensive_loans = []

for item in loans:
    loan_amount = item["loan_price"]
    if loan_amount <= 500:
        inexpensive_loans.append(loan_amount)
    elif loan_amount > 500:
        expensive_loans.append(loan_amount)
    else:
        print("NO")   
    # print(inexpensive_loans)
    # print(expensive_loans)
    # print("-------------")

print(inexpensive_loans)
number_of_loans = len(inexpensive_loans)
#print(number_of_loans)
print(f'The dictionary has {number_of_loans} inexpensive loans and they are priced at ${inexpensive_loans[0]} and ${inexpensive_loans[1]}.')

# created cheap_loans as alternative csv.  Used the inexpensive_loans list to create line 96

cheap_loans = []
for item in loans:
    if item["loan_price"] <= 500:
        cheap_loans.append(item)
print(cheap_loans)

import csv
from pathlib import Path

header = ["loan-price", "remaining_months", "repayment_intervals", "future_value"]
#print(header)
csvpath = Path("cheap_loans.csv")
#output_path = Path("cheap_loans")

with open (csvpath, "w") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",") 
    csvwriter.writerow(header)

    for item in cheap_loans:
        csvwriter.writerow(item.values())
print(item.values())
print(item.keys())




    


