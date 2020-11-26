# This program determines for how long should one save, based on
# his/her salary in order to buy a house in San Francisco, Bay Area
# giving that he gets a semi annual raise in his/her salary
import math

print(
    "This program computes how many months it will take you to save enough money for a down payment on your Bay Area house.\n"
)
annual_salary = eval(input("Annual salary (dollars): "))
portion_saved = eval(input("Salary portion to be saved on a monthly basis (decimal): "))
total_cost = eval(input("House price (dollars): "))
semi_anual_raise = eval(input("Salary raise every six months (decimal): "))

portion_down_payment = 0.25 * total_cost
current_savings = 0
r = 0.04  # yearly return rate of invesment - 4%
months = 1
investment_return = 0
total_savings = 0

while total_savings < portion_down_payment:
    if months % 6 == 0:
        annual_salary = annual_salary + annual_salary * semi_anual_raise# if months == 5:
    #     break
    # print("Month: ", months)
    investment_return = total_savings * r / 12
    current_savings = investment_return + (portion_saved * (annual_salary / 12))
    total_savings = total_savings + current_savings
    # print("Investment return: ", investment_return)
    # print("Current savings: ", current_savings)
    # print("Total savings: ", total_savings)
    # print("")
    months += 1


# current_savings = current_savings + current_savings * r / 12
# print("Current savings: ", current_savings)
# print("Total savings: ", current_savings)
# months = portion_down_payment / current_savings

print("Number of months to save for the house: ", months)
