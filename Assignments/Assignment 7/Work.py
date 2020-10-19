import time
import math

# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series (v, k):
  series_sum = v
  productivity = k

  while((v//k) != 0):

    series_sum += v//k
    k *= productivity

  return series_sum

def get_num_list(n):

  num_list = [ x for x in range(n + 1)]
  return num_list

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, k):
  num_list = get_num_list(n)

  for num in num_list:

    if(sum_series(num, k) >= n and sum_series(num + 1, k) > n and sum_series(num - 1, k) < n):
      return num


# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search (n, k):

  num_list = get_num_list(n)

  #declare low and high
  low = 0
  high = len(num_list) - 1

  #loop while the search range has at least one element in it
  while(low <= high):

    #declare mid
    mid = (low + high) // 2

    # condition for finding V is if the sum of the series of v + 1 is > n
    # and if the sum of the series of v - 1 < n
    # and sum_series of v is >= n
    if(sum_series(mid,k) >= n and sum_series(mid + 1, k) > n and sum_series(mid - 1, k) < n):
      return mid

    elif sum_series(mid, k) < n:
      low = mid + 1

    else:
      high = mid - 1



# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  # write your own test cases

  return "all test cases passed"

def main(params):

  n = params[0]
  k = params[1]

  start = time.time()
  print("Binary Search: " + str(binary_search(n, k)))
  finish = time.time()
  print("Time: " + str(finish - start))

  print()

  start = time.time()
  print("Linear Search: " + str(linear_search(n, k)))
  finish = time.time()
  print("Time: " + str(finish - start))


def get_params():
  for i in range(num_cases):
    line = input().split()
    nums = [int(x) for x in line]
  return (nums[0], nums[1])

if __name__ == "__main__":
  num_cases = int(input())

  if num_cases > 1:
    num_cases -= 1

  for i in range(num_cases):
    params = get_params()
    main(params)