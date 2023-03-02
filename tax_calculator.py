# 1. Create a variable called amount and set a value to 10. 10 is the purchase amount.
# 2. Create another variable for tax and set that to .0625. This will be the sales tax as 6.25%.
# 3. Get the total.


def purchase(amount):
  tax = float(0.0625)
  total = amount + amount*tax
  print(f'${total}')

purchase(10)
purchase(300)