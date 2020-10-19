### How to use this template ####
'''
  * save word.in into the same directory as this file
  * write code in the places indicated below
  * run this code and make sure your output looks correct
    based on what is in the text file
  * make changes to the text file if you want to use your own test
    cases (see the assignment description for the correct format)
  * when you want to submit, you can copy and paste everything in
    the section we indicated. Make sure to run it on HackerRank to
    ensure that it works correctly before submitting
'''


def read_input():
    # open file for reading
    in_file = open('word.in', 'r')
    # read m and n
    coords = in_file.readline().strip().split()
    m = int(coords[0])
    n = int(coords[1])

    # skip blank line
    in_file.readline()

    # read the grid of characters
    word_grid = []
    for _ in range(m):
        word_grid.append(list(map(lambda x: x[0], in_file.readline().rstrip().split())))

    # skip blank line
    in_file.readline()
    k = int(in_file.readline().strip())

    # read the list of words
    word_list = []
    for _ in range(k):
        word_list_item = in_file.readline().strip()
        word_list.append(word_list_item)

    # close the input file
    in_file.close()

    return word_grid, word_list


def main():
    # read input from file
    word_grid, word_list = read_input()

    #### do NOT change anything above this line ####
    #### make changes in this section only      ####
    # call word_search() using the word_grid and word_list parameters

    for word in word_list:
        word_grid_copy = word_grid.copy()
        print(word_search(word_grid_copy, word))

#  Input: word_grid is a 2-D list of characters
#         word_to_search is a SINGLE word to look for in the word_grid
#  Output: function RETURNS a TUPLE representing the
#          indices (row, col) of the first letter of the word_to_search
#          if word does not exist, return (-1, -1)

def word_search(word_grid, word_to_search):

    h_forwards = forwards_horizontal_search(word_grid, word_to_search)
    h_backwards = backwards_horizontal_search(word_grid, word_to_search)
    v_downwards = downwards_vertical_search(word_grid, word_to_search)
    v_upwards = upwards_vertical_search(word_grid, word_to_search)
    diagonal = diagonal_search(word_grid,word_to_search)

    cords = ()

    if h_forwards != None:
        cords = h_forwards
    elif h_backwards != None:
        cords = h_backwards
    elif v_downwards != None:
        cords = v_downwards
    elif v_upwards != None:
        cords = v_upwards
    elif diagonal != None:
        cords = diagonal
    else:
        cords = (-1, -1)

    output = str(cords[0]) + " " + str(cords[1])

    return output

#function for turning the search words into a list of each individual letter.
def word_to_let_list(word):
    i = 0
    let_list = []
    while(i < len(word)):
        let_list.append(word[i])
        i += 1
    return let_list

#function which turns each row in the word grid into a string and returns a list of the strings
def row_to_string(word_grid):

    row_list = []
    row_string = ''

    for rows in word_grid:
        for letter in rows:
            row_string += letter
        row_list.append(row_string)
        row_string = ''

    return row_list

#function which reverses the letters in each row of the grid and returns the grid
def reverse_rows(rowList):
    row_count = 0
    row_list_copy = rowList.copy()
    for row in row_list_copy:
        row = row[::-1]
        rowList[row_count] = row
        row_count += 1
    return row_list_copy

#function which searches the list of the row strings for the provided word using the find() function
def search_row(rowList, word_to_search):

    row_number = 0

    for row in rowList:
        if row.find(word_to_search) != -1:
            col_number = row.find(word_to_search)
            return (row_number, col_number)
        row_number += 1


#function for searching the grid for words horizontally
def forwards_horizontal_search(word_grid, word_to_search):

    word_grid_copy = word_grid.copy()
    rowList = row_to_string(word_grid_copy)
    cords = search_row(rowList, word_to_search)
    return cords


#function searches the grid for words horizontally but backwards
def backwards_horizontal_search(word_grid, word_to_search):

    word_grid_copy = word_grid.copy()
    rowList = reverse_rows(word_grid_copy)
    rowList = row_to_string(rowList)
    word_to_search = word_to_search[::-1]
    cords = search_row(rowList, word_to_search)

    if cords != None:
        cords = list(cords)
        cords[1] = cords[1] + len(word_to_search) - 1
        cords = tuple(cords)

    return cords

#function searches for words downwards along the columns
def downwards_vertical_search(word_grid,word_to_search):

    rowList = list(zip(*word_grid))
    rowList = row_to_string(rowList)

    cords = search_row(rowList, word_to_search)

    if cords != None:
        cords = list(cords)
        cords = cords[::-1]
        cords = tuple(cords)

    return cords

#function searchs for words upwards along the columns
def upwards_vertical_search(word_grid, word_to_search):

    rowList = list(zip(*word_grid[::-1]))
    rowList = row_to_string(rowList)

    cords = search_row(rowList, word_to_search)
    cords_copy = cords

    if cords != None:
        cords = list(cords)
        cords[1] = cords_copy[0]
        cords[0] = (len(word_grid) - 1) - cords_copy[1]
        cords = tuple(cords)

    return cords

def down_right_diagonal_to_string(word_grid):

    diag_list = []
    diag_str = ""

    row = 0
    col = 0
    row_counter = 0
    col_counter = 0

    for rows in word_grid:
        col_counter = 0
        for cols in rows:
            row = row_counter
            col = col_counter
            while row < len(word_grid) and col < len(word_grid[row]):

                letter = word_grid[row][col]
                diag_str += letter

                row += 1
                col += 1

            diag_list.append(diag_str)
            diag_str = ""

            col_counter += 1
        row_counter += 1

    return diag_list

def up_left_diag_to_string(word_grid):
    diag_list = []
    diag_str = ""

    row = 0
    col = 0
    row_counter = 0
    col_counter = 0

    for rows in word_grid:
        col_counter = 0
        for cols in rows:
            row = row_counter
            col = col_counter
            while row >= 0 and col < len(word_grid[row]):
                letter = word_grid[row][col]
                diag_str += letter

                row -= 1
                col += 1

            diag_list.append(diag_str)
            diag_str = ""

            col_counter += 1
        row_counter += 1

    return diag_list

def diagonal_downright_search(word_grid, word_to_search):

    diag_list = down_right_diagonal_to_string(word_grid)
    cords = search_row(diag_list, word_to_search)
    cords_two = cords
    if cords != None:
        cords = list(cords)
        cords[0] = (cords[0] // len(word_grid[0])) + cords[1]
        cords[1] = (cords_two[0] + cords[1]) % len(word_grid)
        cords = tuple(cords)

    return cords

def diagonal_upleft_search(word_grid, word_to_search):
    word_to_search = word_to_search[::-1]
    cords = diagonal_downright_search(word_grid, word_to_search)
    if cords != None:
        cords = list(cords)
        cords[0] = cords[0] + len(word_to_search) - 1
        cords[1] = cords[1] + len(word_to_search) - 1
        cords = tuple(cords)

    return cords

def diagonal_upright_search(word_grid, word_to_search):

    diag_list = up_left_diag_to_string(word_grid)
    cords = search_row(diag_list, word_to_search)
    cords_two = cords
    if cords != None:
        cords = list(cords)
        cords[0] = (cords[0] // len(word_grid[0])) + cords[1]
        cords[1] = (cords_two[0] + cords[1]) % len(word_grid[0])
        cords = tuple(cords)

    return cords


def diagonal_downleft_search(word_grid, word_to_search):

    word_to_search = word_to_search[::-1]
    cords = diagonal_upright_search(word_grid, word_to_search)

    if cords != None:
        cords = list(cords)
        cords[0] = cords[0] - (len(word_to_search) - 1)
        cords[1] = cords[1] + len(word_to_search) - 1
        cords = tuple(cords)

    return cords

def diagonal_search(word_grid, word_to_search):

    dr_diag = diagonal_downright_search(word_grid, word_to_search)
    ul_diag = diagonal_upleft_search(word_grid, word_to_search)
    ur_diag = diagonal_upright_search(word_grid, word_to_search)
    dl_diag = diagonal_downleft_search(word_grid,word_to_search)

    if dr_diag != None:
        return dr_diag
    elif ul_diag != None:
        return ul_diag
    elif ur_diag != None:
        return ur_diag
    elif dl_diag != None:
        return dl_diag
    else:
        return (-1,-1)

#################### do not change anything below this line ###################

if __name__ == "__main__":
    main()