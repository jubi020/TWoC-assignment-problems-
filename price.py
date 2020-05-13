cost_price = float(input("enter the cost price"))
selling_price = float(input("enter the selling price"))
profit = selling_price - cost_price 
newsp = 1.05 * selling_price - 0.5 * cost_price
print("profit earned is", profit)
print("new selling price should be", newsp)