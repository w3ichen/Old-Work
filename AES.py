# AES
def encrypt(message):
	key = input("Enter User Defined Password: ")
	cipher = []
	length = len(message)
	remainder = length%16
	num_of_blocks = int(((length-remainder)/16)+1)
	cipher.append(num_of_blocks)

	for blocks in range(num_of_blocks):
		message_block = get_message(message)
		message = list(message)
		del message[0:16]
		''.join(message)
		key_block = get_key(key)
		cipher.append(encrypt_1(message_block,key_block))
	return cipher

	# if decrypt is called
def decrypt(message):
	try:
		key = input("Enter Password: ")
		decrypted = []
		num_of_blocks = message[0]

		for blocks in range(num_of_blocks):
			message_block = message[blocks+1]
			key_block = get_key(key)
			d = decrypt_1(message_block,key_block)
			decrypted.append(d)
		return ''.join(decrypted)
	except:
		print('ERROR')
	
def get_message(message):
	# only returns one of the blocks
	#convert to 4 by 4 matrix
	message = list(message)
	output = []
	#convert to ascii
	ascii_message = []

	for non_ascii in message:
		ascii_message.append(ord(non_ascii))
	while len(ascii_message)<4:
		# append with space
		ascii_message.append(32)

	for row_of_4 in range(4):
		output.append((ascii_message[0:4]))
		#delete thatthe first 4
		del ascii_message[0:4]
		while len(ascii_message)<4:
			# append with space
			ascii_message.append(32)
	return output

def get_key(key):
	#gets the key in a block
	if len(key)<=16:
		#must input ascii number in the block
		key = list(key)
		output = []
		#convert to ascii
		ascii_key = []
		for non_ascii in key:
			ascii_key.append(ord(non_ascii))
		while len(ascii_key)<4:
			# append with space
			ascii_key.append(32)
		for row_of_4 in range(4):
			output.append((ascii_key[0:4]))
			#delete thatthe first 4
			del ascii_key[0:4]
			while len(ascii_key)<4:
				# append with space
				ascii_key.append(32)
	elif len(key)>16:
		# if length is longer than 16, need to group it
		key = list(key)
		output = []
		#convert to ascii
		ascii_key = []
		for non_ascii in key:
			ascii_key.append(ord(non_ascii))
		for row_of_4 in range(4):
			output.append((ascii_key[0:4]))
			#delete thatthe first 4
			del ascii_key[0:4]
			#add remaining to other first few
		while len(ascii_key)!=0:
			# add remainig ones to first couple
			for row in range(0,4):
				for column in range(0,4):
					if len(ascii_key)==0:
						break
					output[row][column] += ascii_key[0]
					del ascii_key[0]
	return output

def multiply_matrix(matrix1,matrix2):
	import numpy as np 
	output = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	for move_row in range(0,4):
		for move_col in range(0,4):
			#matrix multiplication		
			output[move_row][move_col] = (int(round(np.dot(matrix1[move_row],[matrix2[0][move_col],matrix2[1][move_col],matrix2[2][move_col],matrix2[3][move_col],]))))
	return output
	#NOTE formating block[row][column]

def encrypt_1(message_block,key_block):
	output = []
	#STEP 1: XOR key and ascii text
	for xor_row in range(0,4):
		output.append([ message_block[xor_row][0]^key_block[xor_row][0],
						message_block[xor_row][1]^key_block[xor_row][1],
						message_block[xor_row][2]^key_block[xor_row][2],
						message_block[xor_row][3]^key_block[xor_row][3]
			])
	#=====================================
	#STEP 2: 10 loops of sub, row shift, column mix, and XOR
	for NineLoops in range(0,9):

		#STEP 2-i row shift, 1st row, now shift, 2nd row shift by 1
		for shift_row in range(0,4):
			for shift_amount in range(0,shift_row):
				output[shift_row].append(output[shift_row].pop(0))
		#STEP 2-ii column mixer
		matrix = [[2,3,1,1],[1,2,3,1],[1,1,2,3],[3,1,1,2]]
		output = multiply_matrix(matrix,output)

		#STEP 2-iii XOR again
		for xor_row2 in range(0,4):
			
			output[xor_row2][0] = output[xor_row2][0]^key_block[xor_row2][0]
			output[xor_row2][1] = output[xor_row2][1]^key_block[xor_row2][1]
			output[xor_row2][2] = output[xor_row2][2]^key_block[xor_row2][2]
			output[xor_row2][3] = output[xor_row2][3]^key_block[xor_row2][3]
		#end of loop
	#=============================================
	# end with row shift 
	for shift_row in range(0,4):
		for shift_amount in range(0,shift_row):
			output[shift_row].append(output[shift_row].pop(0))

	for xor_row3 in range(0,4):
		output[xor_row3][0] = output[xor_row3][0]^key_block[xor_row3][0]
		output[xor_row3][1] = output[xor_row3][1]^key_block[xor_row3][1]
		output[xor_row3][2] = output[xor_row3][2]^key_block[xor_row3][2]
		output[xor_row3][3] = output[xor_row3][3]^key_block[xor_row3][3]
	#make output a string and output
	# output_string = ''.join([''.join(str(x) for x in output[0]),''.join(str(x) for x in output[1]),''.join(str(x) for x in output[2]),''.join(str(x) for x in output[3])])
	return output

def decrypt_1(message_block,key_block):

	output = []
	for xor_row3 in range(0,4):
		output.append([ message_block[xor_row3][0]^key_block[xor_row3][0],
						message_block[xor_row3][1]^key_block[xor_row3][1],
						message_block[xor_row3][2]^key_block[xor_row3][2],
						message_block[xor_row3][3]^key_block[xor_row3][3]
			])

	for shift_row in range(0,4):
		for shift_amount in range(0,shift_row):
			output[shift_row].insert(0,output[shift_row].pop(3))

	#decrypt goes in reverse
	for NineLoops in range(0,9):
		#STEP 1: start with XOR
		for xor_row2 in range(0,4):
			output[xor_row2][0] = output[xor_row2][0]^key_block[xor_row2][0]
			output[xor_row2][1] = output[xor_row2][1]^key_block[xor_row2][1]
			output[xor_row2][2] = output[xor_row2][2]^key_block[xor_row2][2]
			output[xor_row2][3] = output[xor_row2][3]^key_block[xor_row2][3]

		#STEP 2: column mixer
		#encryped * inverse matrix = reverse
		inverse_matrix = [[-4/35,3/35,-11/35,17/35],[17/35,-4/35,3/35,-11/35],[-11/35,17/35,-4/35,3/35],[3/35,-11/35,17/35,-4/35]]
		output = multiply_matrix(inverse_matrix,output)

		#STEP 3: row shifter
		for shift_row in range(0,4):
			for shift_amount in range(0,shift_row):
				output[shift_row].insert(0,output[shift_row].pop(3))
		#end of loop

	#STEP 4: XOR key and ascii text
	for xor_row2 in range(0,4):
		output[xor_row2][0] = output[xor_row2][0]^key_block[xor_row2][0]
		output[xor_row2][1] = output[xor_row2][1]^key_block[xor_row2][1]
		output[xor_row2][2] = output[xor_row2][2]^key_block[xor_row2][2]
		output[xor_row2][3] = output[xor_row2][3]^key_block[xor_row2][3]

	original_message = []
	try:
		#STEP 5 :convert to ascii
		for ascii_row in range(0,4):
			for ascii_column in range(0,4):
				original_message.append(chr(output[ascii_row][ascii_column]))
		return ''.join(original_message)

	except ValueError:
		raise