#!/usr/bin/python

import math
import argparse

# References
# https://medium.com/@antash/six-ways-to-find-max-value-of-a-list-in-python-b7d7ccfabc0d


# How can I turn a list into an object?
# How can I iterate over an object?
# If stock increases, subtract the lower, earlier occuring value from the increased value

# def find_max_profit(prices):
#   max = 0
#   min = math.inf
#   prices = [int(x) for x in prices]
#   for price in prices:
#     if price > max:
#       max = price
#   for price in prices:
#     if price < max:
#       min = price
#   return max-min

# learned list.index(item)

# want to locate the most recent, largest price

def find_max_profit(prices):
  min_price = prices[0] # initiate the minimum as the first item in the list
  max_profit = prices[1] - prices[0] # initiate the maximum profit as the difference between the first two list items
  
  for i in range(1, len(prices)):  # iterate prices by index
    price = prices[i] # define the price as each value in prices
    max_profit = max(price - min_price, max_profit) # check which is greater, the previos profit or the newly calculated one
    min_price = min(price, min_price) # check each price in the loop to see if it is smaller than the previously identified minimum
  return max_profit

testArr = [10, 7, 5, 8, 11, 9]
testArr[-1]

print(find_max_profit(testArr))

# def find_max_profit(prices):
#     max = 0
#     for x in prices:
#         if x > max:
#             max = x
#     return max


# recursive function to find maximum

# def find_max_profit(prices):
#   if len(prices) == 1:
#     return prices[0]
#   v1 = prices[0]
#   v2 = find_max_profit(prices[1:])
#   if v1 > v2:
#     return v1
#   else:
#     return v2

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))