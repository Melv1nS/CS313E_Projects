import math

# counts all the possible paths in a grid
def count_paths (n):
    #there are n-1 steps right and n-1 steps down in any given path
    steps = (n-1) * 2
    #number of paths = steps!/((n-1)! * (n-1)!)
    paths = math.factorial(steps)//(math.factorial(n-1) ** 2)
    return int(paths)

# gets the greatest sum of all the paths in the grid
def path_sum (grid, n):

    grid_sums = grid.copy()

    #fill out sums for bottom row and last column first
    i = n - 2
    while (i >= 0):
        grid_sums[n-1][i] += grid_sums[n-1][i + 1]
        i -= 1

    i = n - 2
    while (i >= 0):
        grid_sums[i][n-1] += grid[i+1][n-1]
        i -= 1

    row = n-2

    #gets sums for the rest of the squares
    while (row >= 0):
        col = n - 2
        while (col >= 0):
            if grid_sums[row + 1][col] >= grid_sums[row][col + 1]:
                grid_sums[row][col] += grid_sums[row + 1][col]
            else:
                grid_sums[row][col] += grid_sums[row][col + 1]
            col -= 1
        row -= 1

    return grid_sums[0][0]


def main():
    # read data from standard input

    # read the dimension of the grid
    dim = int(input())

    # create an empty grid
    grid = []

    for i in range(dim):
      temp_list = [int(x) for x in input().split()]
      grid.append(temp_list)

    # populate the grid

    # get the number of paths in the grid and print
    num_paths = count_paths (dim)
    print ('Number of paths in a grid of dimension', dim, 'is', num_paths)
    print ()

    # get the maximum path sum and print
    max_path_sum = path_sum (grid, dim)
    print ('Greatest path sum is', max_path_sum)

if __name__ == "__main__":
  main()