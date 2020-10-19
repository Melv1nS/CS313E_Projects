
import math

# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def encrypt ( strng ):

	# calls get_next_square function to get the next perfect square that is larger
	# than the length
	M = get_next_square(len(strng))

	#gets the length of the message
	L = len(strng)

	#number of astricks to pad
	num_astricks = M-L

	#pads message with astricks
	for i in range(num_astricks):

		strng += '*'

	#separtes original message and padded message into new variable
	padded_str = strng


	#gets K or the length of the grid
	num_rows = int(math.sqrt(len(padded_str)))

	#calls get_rows methods which splits the padded message into K rows of K length
	str_in_rows = get_rows(padded_str, num_rows)

	#calls rotate_rows to rotate the grid and returns the rows of the rotated grid
	str_rotated = rotate_rows(str_in_rows)

	#turns the rotated grid back into string form
	encrypted_message = make_rows_string(str_rotated)

	#removes astricks
	encrypted_message = encrypted_message.replace('*', '')

	return encrypted_message

# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def decrypt ( strng ):

	M = get_next_square(len(strng))

	L = len(strng)

	num_astricks = M - L

	place_of_astricks = find_place_of_astricks(L, M, num_astricks)

	# replaces the # characters with letters from the message
	# leaves the astericks
	i = 0

	for row in range(len(place_of_astricks)):
		place_of_astricks[row] = list(place_of_astricks[row])
		for letter in range(len(place_of_astricks[row])):
			if place_of_astricks[row][letter] == '#':
				place_of_astricks[row][letter] = strng[i]
				i += 1

	#sets new variable = to the message with astricks in place
	msg_with_astricks = place_of_astricks

	#returns message decrypted but in a list of rows
	decrypted_rows = rotate_counter_clockwise(msg_with_astricks)

	#makes the rows into one string
	decrypted_msg = make_rows_string(decrypted_rows)

	#removes astricks
	decrypted_msg = decrypted_msg.replace('*', '')

	return decrypted_msg


def rotate_counter_clockwise(strng):

	rotated_rows = list(zip(*strng))[::-1]

	return rotated_rows



def find_place_of_astricks(str_length, next_square, num_astricks):

	characters_replaced = '#' * str_length

	for i in range(num_astricks):

		characters_replaced += '*'

	string_with_astericks = characters_replaced

	# gets K or the length of the grid
	num_rows = int(math.sqrt(len(string_with_astericks)))

	# calls get_rows methods which splits the padded message into K rows of K length
	str_in_rows = get_rows(string_with_astericks, num_rows)

	str_rotated = rotate_rows(str_in_rows)

	return str_rotated




def make_rows_string(grid):

	message = ''

	for rows in grid:
		for letter in rows:

			message += letter

	return message

def rotate_rows(strng_in_rows):

	rotated_rows = list(zip(*strng_in_rows[::-1]))
	return rotated_rows

def get_rows(strng, rows):

	string_in_rows = []
	row_list = []

	i = 0

	for letter in strng:
		if i < rows:
			row_list.append(letter)
			i += 1
		else:
			string_in_rows.append(row_list.copy())
			row_list.clear()
			row_list.append(letter)
			i = 1

	string_in_rows.append(row_list.copy())

	return string_in_rows

def get_next_square(num):

	if(math.sqrt(num).is_integer()) == True:
		return num
	else:

		next_square_num = (math.floor(math.sqrt(num)) + 1) ** 2
		return next_square_num

def read_input():

	P = input()
	Q = input()

	return P, Q


def main():
	# read the strings P and Q from standard input
	P, Q = read_input()

	# encrypts the string P and prints it
	print(encrypt(P))

	# decrypt the string Q

	print(decrypt(Q))

	# print the encrypted string of P
	# and the decrypted string of Q

if __name__ == "__main__":
	main()


