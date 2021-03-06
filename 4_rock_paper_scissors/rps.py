#!/usr/bin/python

import sys
from itertools import combinations
from itertools import repeat
from itertools import combinations_with_replacement

# https://www.youtube.com/watch?v=smU0eIqdzd0

# def repeat(object, times = None):
#   if times is None:
#     while True:
#       yield object
#     else:
#       for i in range(times):
#         yield object

# def product(*args, **kwds):
#     # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
#     # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
#     pools = map(tuple, args) * kwds.get('repeat', 1)
#     result = [[]]
#     for pool in pools:
#         result = [x+[y] for x in result for y in pool]
#     for prod in result:
#         return tuple(prod)


# def arrangements(element, r):
#   pool = tuple(element)
#   n = len(pool)
#   for indices in product(range(n), repeat = r):
#     if sorted(indices) == list(indices):
#       return tuple(pool[i] for i in indices)

# for c in combinations_with_replacement(['rock', 'paper', 'scissors'],4):
#   print(c)

# def rock_paper_scissors(n):
#   storage = []
#   for c in combinations_with_replacement(['rock', 'paper', 'scissors'],4):
#     storage.append(c)
#   return storage

# print(rock_paper_scissors(4))

def rock_paper_scissors(n):
  plays = ['rock', 'paper', 'scissors']
  outcomes = []

  def find_outcome(n, result = []):
    # base case
    if n == 0:
      outcomes.append(result)
      return
    # move towards the base case
    for play in plays:
      find_outcome(n - 1, result + [play])

  # have to call the function to initiate
  find_outcome(n, [])
  return outcomes

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')