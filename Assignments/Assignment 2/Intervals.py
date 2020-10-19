'''
How to use this Template:
For this assignment, do not change the function names or parameters
You will need to read from standard input. In order to do this, when 
you run your program in the command line, you will do it as follows:

$ python3 Intervals.py < intervals.in


If you read intervals.in as a file, it will not work on HackerRank. 
You should be able to paste this whole file into HackerRank. Please 
run your code to ensure it passes, and write your own test cases to 
ensure your answer is correct.
'''

import sys


# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval
def merge_tuples (tuples_list):

  merged_tuples = tuple_merger(tuples_list)

  checker = tuple_checker(merged_tuples)
  merged_tuples_addition = merged_tuples.copy()

  while checker == True:

    merged_tuples_addition = tuple_merger(merged_tuples_addition)
    checker = tuple_checker(merged_tuples_addition)

  merged_tuples = tuple_cleaner(merged_tuples)

  for tup in merged_tuples_addition:

    if tup not in merged_tuples:
      merged_tuples.append(tup)

  i = 0
  tups_to_remove = []
  for merged_tup in merged_tuples:
    for tup in tuples_list:
      if merged_tup[0] <= tup[0] and merged_tup[1] >= tup[1]:
        tups_to_remove.append(tup)

  for tup in tups_to_remove:
    if tup in tuples_list:
      tuples_list.remove(tup)


  merged_tuples = merged_tuples + tuples_list

  #removes duplicates
  merged_tuples = list(set(merged_tuples))

  merged_tuples.sort()


  return merged_tuples


# Input: tuples_list is a list of tuples of denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval
def sort_by_interval_size (tuples_list):

  interval_list = []
  for tup in tuples_list:

    interval = tup[1] - tup[0]
    interval_list.append((interval, tup[0], tup[1]))

  interval_list.sort()

  tup_sorted_by_interval = []

  for tup in interval_list:
    tup_to_append = (tup[1], tup[2])
    tup_sorted_by_interval.append(tup_to_append)

  return tup_sorted_by_interval

def read_input():

  #for running in pycharm
  #python3 Intervals.py < intervals.in
  num_tuples = int(input())
  tup_list = []

  for i in range(num_tuples):
    tup_numbers = input().split()

    tup = (int(tup_numbers[0]), int(tup_numbers[1]))
    tup_list.append(tup)

  return tup_list



def tuple_merger(tuples_list):

  merged_tuples = []

  #tuples that don't need to be merged
  mergless_tuples = []

  first = 0
  second = 1

  while second < len(tuples_list):

    # checks if lower bound of second tuple is in the interval of 1st
    if tuples_list[first][0] <= tuples_list[second][0] and \
       tuples_list[second][0] <= tuples_list[first][1]:

      # checks if upper bound of second tuple is > upper bound of first tuple
      if tuples_list[first][1] < tuples_list[second][1]:
        merged_tuples.append((tuples_list[first][0], tuples_list[second][1]))

      if tuples_list[first][1] > tuples_list[second][1]:
        merged_tuples.append(tuples_list[first])

    first += 1
    second += 1

  return merged_tuples

def tuple_checker(tuples_list):

   first = 0
   second = 1

   check = False

   while second < len(tuples_list):

     if tuples_list[first][0] <= tuples_list[second][0] and tuples_list[second][0] <= tuples_list[first][1]:

        if tuples_list[first][1] < tuples_list[second][1]:
          check = True

     first += 1
     second += 1

   return check

def tuple_cleaner(tuples_list):

  first = 0
  second = 1

  values_to_remove = []



  while second < len(tuples_list):

    if tuples_list[first][0] <= tuples_list[second][0] and tuples_list[second][0] <= tuples_list[first][1]:


      if tuples_list[first][1] < tuples_list[second][1]:

        if tuples_list[first] not in values_to_remove:
          values_to_remove.append(tuples_list[first])
        if tuples_list[second] not in values_to_remove:
          values_to_remove.append(tuples_list[second])

      if tuples_list[first][0] < tuples_list[second][0]:

        if tuples_list[second] not in values_to_remove:
          values_to_remove.append(tuples_list[second])

    first += 1
    second += 1

  for tup in values_to_remove:
    tuples_list.remove(tup)

  return tuples_list

def main():

  # read the input data and create a list of tuples
  tup_list = read_input()
  tup_list_copy = tup_list.copy()
  tup_list_copy.sort()

  # merge the list of tuples
  final = merge_tuples(tup_list_copy)
  final.sort()

  # print the merged list
  print(final)
  #print()

  # sort the list of tuples according to the size of the interval

  interval_sorted = sort_by_interval_size(final)

  # print the sorted list
  print(interval_sorted)

if __name__ == "__main__":
  main()
