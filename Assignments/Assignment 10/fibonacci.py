# File: Fibonacci.py

# Description:

# Student's Name: Melvin Sureshbabu

# Student's UT EID: ms82362

# Partner's Name:

# Partner's UT EID:

# Course Name: CS 313E

# Unique Number: 50845

# Date Created: 10/9/2020

# Date Last Modified: 10/9/2020

import sys

# Input: n a positive integer
# Output: a bit string
def f (n, memo):

    if n == 0 or n == 1:
        return str(memo[n])
    else:
        if (n>= len(memo)):
            f_next = str(f(n-1, memo)) + str(f(n-2, memo))
            memo.append(f_next)
            return f_next
        else:
            return str(memo[n])

# Input: s and p are bit strings
# Output: an integer that is the number of times p occurs in s
def count_overlap (s, p):

    #gets length of the substring
    l = len(p)

    #gets all the substrings of length l from the bit string (s)
    bit_subs = [s[i:i+l] for i in range(len(s)) if i + l <= len(s)]

    #counts the number of
    count = bit_subs.count(p)

    return count

def main():
    # read n and p from standard input
    n = sys.stdin.readline()
    n = int(n.strip())
    p = sys.stdin.readline()
    p = p.strip()

    # compute the bit string f(n)
    memo = [0, 1]
    s = f(n,memo)

    # determine the number of occurrences of p in f(n)
    # print the number of occurrences of p in f(n)
    print(count_overlap(s, p))

if __name__ == "__main__":
  main()