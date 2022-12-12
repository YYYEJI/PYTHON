prices = [3.16, 5.12, 4.49, 6.12]
data = ["B15", "S10", "B2", "S3"]

total = 100
profit = 0
### YOUR CODE STARTS HERE
# This line is about buying and selling.
info = []

# This line iterates code 4.
for i in range(4):
    # This if statement separates "B" from "S".
    # This line verifies that "B" is included in the string.
    if "B" in data[i]:
        # This line divides the data by "B" and puts it in the info list.
        info = data[i].split("B")
        # If you buy a stock, this line multiplies the price by how many you bought and subtracts it from the total price.
        total = total - (float(info[1])*prices[i])
    # This line verifies that "S" is included in the string.
    else:
        # This line divides the data by "S" and puts it in the info list.
        info = data[i].split("S")
        # This line adds to the total price by multiplying the price and how many you bought when I sold the stock.
        total = total + (float(info[1])*prices[i])
    
# This line first subtracts the price from the total price to make a profit.
profit = total - 100


### YOUR CODE ENDS HERE
print("Balance =", total)
print("Profit =", profit)

"""
### YOUR EXPLANATION STARTS HERE

It's a program that calculates the profits left after buying and selling stocks.

### YOUR EXPLANATION ENDS HERE
"""