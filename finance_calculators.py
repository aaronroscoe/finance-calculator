import math

# Show instructions, with details about the options they can choose.
print("investment - to calculate the amount of interest you'll earn on your investment")
print("mortgage   - to calculate the amount you'll have to pay monthly to fully replay your mortgage.")

# Input from the user, choosing the interest type. 
calculator_selector = input("Enter either 'investment' or 'mortgage' from the menu above to proceed: ").lower()

# Calculator based on previous input from user
# Includes further inputs to calculate either the simple 
# or compound interest on an investment, or the monthly amount payable on a bond.
if calculator_selector == "investment":
    amount_money_deposting = float(input("Enter the amount you are depositing: "))
    interest_rate = float(input("Enter the interest rate (only the number): "))
    number_of_years = int(input("Enter the number of years you plan on investing: "))
    interest_type = str(input("Do you want 'simple' or 'compound' interest? ").lower())
    if interest_type == "simple":
        simple_interest_total = amount_money_deposting * (1 + ((interest_rate/100) * number_of_years))
        simple_interest_total = round(simple_interest_total, 2)
        print(f"After {number_of_years} years, you will have £{simple_interest_total}")
    elif interest_type == "compound":
        compound_interest_total = amount_money_deposting * math.pow(1 + (interest_rate/100), number_of_years)
        compound_interest_total = round(compound_interest_total, 2)
        print(f"After {(number_of_years)} years, you will have £{compound_interest_total}")
    else:
        print("Error. Please try again, and enter either 'simple' or 'compound'.")
elif calculator_selector == "mortgage":
    current_house_value = float(input("Enter the current value of the house: "))
    interest_rate = float(input("Enter the interest rate (only the number): "))
    number_of_months = int(input("Enter the number of months you plan to repay the bond: "))
    repayment_amount =  (((interest_rate / 100) / 12) * current_house_value)/(1 - (1 + ((interest_rate / 100) / 12))**(0 - number_of_months))
    repayment_amount = round(repayment_amount, 2)
    print(f"You will have to repay £{repayment_amount} per month to repay £{current_house_value} in {number_of_months} months.")
else:
    print("Error. Please try again, and enter either 'investment' or 'mortgage'.")
        
        
        