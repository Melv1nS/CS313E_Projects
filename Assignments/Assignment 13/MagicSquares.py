#  File: MagicSquare.py

#  Description:

#  Student Name: Melvin Sureshbabu

#  Student UT EID: ms82362

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 50845

#  Date Created: 10/18/2020

#  Date Last Modified:

import math
import time

# checks if a 1-D list if converted to a 2-D list is magic
# a is 1-D list of integers
# returns True if a is magic and False otherwise
def is_magic(a):

  a = convert_2D(a)

  row_sum = sum(a[0])

  #checks rows
  for row in a:
    if row_sum - sum(row[:-1]) != row[-1]:
      return False

  #checks columns
  for col in zip(*a):
    if row_sum - sum(col[:-1]) != col[-1]:
      return False

  n = len(a)
  diag = []

  #gets down left diag
  for i in range(n):
    diag.append(a[i][i])

  if row_sum - sum(diag[:-1]) != diag[-1]:
    return False

  diag = []

  #gets up right diag
  for i in range(n):
    diag.append(a[i][n - 1 -i])

  if row_sum - sum(diag[:-1]) != diag[-1]:
    return False

  return True


def convert_2D(a):
  n = math.sqrt(len(a))

  a_2D = []
  temp = []

  for num in a:
    temp.append(num)
    if len(temp) == 3:
      a_2D.append(temp)
      temp = []

  return a_2D

# this function recursively permutes all magic squares
# a is 1-D list of integers and idx is an index in a
# it stores all 1-D lists that are magic in the list all_magic
def permute ( a, idx, all_magic):

  hi = len(a)

  if idx == hi and is_magic(a):
    print(a)
  else:
    for i in range(idx,hi):
      a[idx], a[i] = a[i], a[idx]
      permute(a, idx + 1, all_magic)
      a[i], a[idx] = a[idx], a[i]


def main():
  # read the dimension of the magic square
  in_file = open ('magic.in', 'r')
  line = in_file.readline()
  line = line.strip()
  n = int (line)
  in_file.close()

  '''
  # check if you read the input correctly
  print (n)
  '''

  start = time.time()

  # create an empty list for all magic squares
  all_magic = []

  # create the 1-D list that has the numbers 1 through n^2
  a = [ i for i in range(1, n**2 + 1)]

  # generate all magic squares using permutation
  # print all magic squares

  permute(a, 0, all_magic)

  end = time.time()
  print('runtime: ', end - start)


if __name__ == "__main__":
  main()