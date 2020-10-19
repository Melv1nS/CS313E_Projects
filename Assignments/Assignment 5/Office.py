# Input: a rectangle which is a tuple of 4 integers (x1, y1, x2, y2)
# Output: an integer giving the area of the rectangle
def area (rect):

    width = rect[2] - rect[0]
    length = rect[3] - rect[1]

    area = width * length

    return area

# Input: no input
# Output: a string denoting all test cases have passed
"""def test_cases ():
  assert area ((0, 0, 1, 1)) == 1
  # write your own test cases

  return "all test cases passed"
  """

def create_grid(dimensions):

    grid =[]
    for i in range(dimensions[1]):
        grid.append([])

    for row in grid:
        for i in range(dimensions[0]):
            row.append(0)


    return grid

def read_input():

    #note dimensions need to be within 1 and 100
    #names 1-20 characters
    dimensions = tuple([int(x) for x in input().split()])

    num_employees = int(input())

    emp_list = []

    for i in range(num_employees):

        employee = input().split()
        emp_list.append(employee.copy())
        employee.clear()

    return dimensions, emp_list


def get_length(rect):

    length = rect[3] - rect[1]
    return length

def get_width(rect):

    width = rect[2] - rect[0]
    return width

def increment_grid(grid, rect):

    row_start = len(grid) - rect[3]
    row_end = len(grid) - rect[1]

    col_start = rect[0]
    col_end = rect[2]

    for row in range(row_start, row_end):
        for col in range(col_start, col_end):

            grid[row][col] += 1


def unallocated_space(grid):

    unallocated = 0

    for row in grid:
        unallocated += row.count(0)

    return unallocated

def total_space(grid):

    total = len(grid[0]) * len(grid)

    return total

def contestedSpace(grid):

    contested = 0

    for row in grid:
        for col in row:
            if col > 1:
                contested += 1

    return contested

def find_guaranteed(grid, rect):

    row_start = len(grid) - rect[3]
    row_end = len(grid) - rect[1]

    col_start = rect[0]
    col_end = rect[2]

    guaranteed = 0

    for row in range(row_start, row_end):
        for col in range(col_start, col_end):

            if grid[row][col] == 1:
                guaranteed += 1

    return guaranteed


def main():

    # read the data

    dimensions, emp_list = read_input()

    name_list = []
    rect_list = []

    for emp in emp_list:
        name_list.append(emp[0])
        rect_list.append((int(emp[1]), int(emp[2]), int(emp[3]), int(emp[4])))


    grid = create_grid(dimensions)

    for rect in rect_list:

        increment_grid(grid, rect)

    """for row in grid:
        print(row)"""

    print('Total', total_space(grid))
    print('Unallocated', unallocated_space(grid))
    print('Contested', contestedSpace(grid))

    i = 0

    for rect in rect_list:

        print(name_list[i], str(find_guaranteed(grid, rect)))
        i += 1

    # run your test cases
    '''
    print (test_cases())
    '''

    # print the following results after computation

    # compute the total office space

    # compute the total unallocated space

    # compute the total contested space

    # compute the uncontested space that each employee gets

if __name__ == "__main__":
  main()
