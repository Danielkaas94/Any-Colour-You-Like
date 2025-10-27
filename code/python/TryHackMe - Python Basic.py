"""
    In this project, you'll create a program that calculates the total
    cost of a customers shopping basket, including shipping.

    - If a customer spends over $100, they get free shipping
    - If a customer spends < $100, the shipping cost is $1.20 per kg of the baskets weight

    Print the customers total basket cost (including shipping) to complete this exercise.

"""

customer_basket_cost = 101
customer_basket_weight = 44
weight_cost = customer_basket_weight*1.2
total_basket_cost = customer_basket_cost

# Write if statement here to calculate the total cost
if customer_basket_cost > 100:
  print(customer_basket_cost)
else:
  print(total_basket_cost + weight_cost)


"""
    In this project, you'll create a program that that tells
    you when the value of your Bitcoin falls below $30,000.

    You will need to:
    - Create a function to convert Bitcoin to USD
    - If your Bitcoin falls below $30,000, print a message.

    You can assume that 1 Bitcoin is worth $40,000

"""

investment_in_bitcoin = 1.2
bitcoin_to_usd = 40000

# 1) write a function to calculate bitcoin to usd
def bitcoinToUSD(bitcoin_amount,bitcoin_value_usd):
  total = bitcoin_amount * bitcoin_value_usd
  return total

# 2) use function to calculate if the investment is below $30,000
value = bitcoinToUSD(investment_in_bitcoin,bitcoin_to_usd)
if(value < 30000):
  print("Alert!! Sell everybody and everything! But keep the TV like a proper boomer!!?!")
elif(value == 30000):
  print("Exactly $30.000 in value! - Don't worry! There is only upwards volatility! The only way is up! 📈🤡")
else:
  print("Your \"Investment\" is above $30.000 - No need to sell the kidney of your narcissistic family member.")


"""
✅ Just completed the Python Basics room on TryHackMe!

It’s a great interactive room, using a web-based code editor to learn Python fundamentals and ending with a small Bitcoin investment project.

Something I’ve learned over time: learning is a circle, not a straight line.
There is nothing wrong with going back to the basics in any subject, that is where true understanding happens.
Only a fool believes mastery comes from doing something once. Real growth comes from repetition, reflection, and refinement.

#Python #CyberSecurity #TryHackMe #LifelongLearning #GrowthMindset
"""