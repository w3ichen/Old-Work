import random   

'''
Description: validate function will take an input and determing
			if it is secure, insecure or invalid
Arguments: password is the input from user
Returns: outputs either secure, insecure, or invalid
'''

# validate function
def validate(password):
	# print invalid if length is less than 8 or contains space, - , or _
	if len(password) < 8 or password.count(' ') > 0 or password.count('-') > 0 or password.count('_') > 0:
		# if the count method counts more than zero for invalid characters, then it is invalid
		print("Invalid")
		return 0 # stop program
	# check for upper case, lower case, and numbers
	# define variables to count number of lower, upper case and numbers
	lowerCount = 0
	upperCount = 0
	numCount = 0

	# loops through each element of password string
	for i in range(0,len(password)):  
		# if the element is lower case
		if password[i].islower() == True: 
			# count number of lower cases
			lowerCount+=1  
		if password[i].isupper() == True:  
			upperCount+=1 
		if password[i].isdigit() == True:  
			numCount+=1  

	# check for special characters
	# define variable to count special characters
	specialCount = 0  
	#puts the special characters in a list
	special = list('!#$%&\'()*+,./:;<=>?@[]^`{|}~') 
	# loop through all characters to see if it is in password
	for i in range(0,len(special)):  
		 # counts how many of the special characters are in password
		sCharacter = password.count(special[i]) 
		# add up number of special characters
		specialCount += sCharacter  


	# if no upper, lower case letters or numbers or special characters are counted, print insecure
	if (lowerCount == 0 or upperCount == 0) or (numCount == 0 or specialCount == 0):
		print('Insecure')
		return 0  # stop program
	else:
		print('Secure')  # if program passes all above requirements and program is not stopped, print secure
		return 0  # stop program

# ========================================================================
'''
Descrition: generate function will generate a random secure password
Arguments: n is the input, which is the length of the password
Returns: outputs the secure password with length n
'''
# generate password function
def generate(n):
	n = int(n)  
	# n length must be 8 or more
	if n < 8:  
		print('Error: Password must have a length of 8 or more') 
		return 0 
	# empty list to make new password
	newPassword = []  

	# define variables to count password requirements
	lowerCount = 0
	upperCount = 0
	numCount = 0
	specialCount = 0
	# counts number of loops so can do quality check before password is fully defined
	loopCount = 0  
	 # keeps looping until password has the length needed
	while len(newPassword) != n: 
		# generate a number to decide what type next element will be
		typeNum = random.randint(1,4) 
		# generates upper case
		if typeNum == 1: 
			# generates a random upper case letter
			upperLetter = random.randint(65,90)  
			# converts to letter using chr
			upperLetter = chr(upperLetter) 
			# add to new password list
			newPassword.append(upperLetter) 
			# add count
			upperCount+=1  
		# generates lower case
		if typeNum == 2:  
			lowerLetter = random.randint(97,122)  
			lowerLetter = chr(lowerLetter)  
			newPassword.append(lowerLetter)  
			lowerCount+=1 
		# generates number
		if typeNum == 3:  
			ranNum = random.randint(0,9)  
			ranNum = str(ranNum)  
			newPassword.append(ranNum)  
			numCount+=1  
		 # generate special character
		if typeNum == 4: 
			# puts the special characters in a list
			special = list('!#$%&\'()*+,./:;<=>?@[]^`{|}~')  
			# generate a random number in range of special list
			specialLetter = random.randint(0,len(special)-1)  
			specialLetter = special[specialLetter]  
			newPassword.append(specialLetter)  
			specialCount+=1  
			
		# quality control, check that all conditions are included
		# stop before full password in order to check requirements are met. must have enough spaces left if no requirements are met
		if  loopCount == n-4: 
			# generate random number to determine a random index
			randomIndex = random.randint(0,n-4) 
			# if there are no upper case letters
			if upperCount == 0: 
				# generates a random upper case letter
				upperLetter = random.randint(65,90)  
				# convert to letter
				upperLetter = chr(upperLetter)  
				# inserts to a random position in newPassword using randomIndex
				newPassword.insert(randomIndex,upperLetter) 
			# if there are no lower case letters
			if lowerCount == 0:  
				lowerLetter = random.randint(97,122)  
				lowerLetter = chr(lowerLetter)  
				newPassword.insert(randomIndex, lowerLetter)
			# if there are no numbers
			if numCount == 0: 
				ranNum = random.randint(0,9) 
				ranNum = str(ranNum)  
				newPassword.insert(randomIndex,ranNum)
			# if there are no special characters
			if specialCount == 0:  
				special = list('!#$%&\'()*+,./:;<=>?@[]^`{|}~')  
				specialLetter = random.randint(0,len(special)-1) 
				specialLetter = special[specialLetter]  
				newPassword.insert(randomIndex,specialLetter)
			loopCount += 1
	newPassword = ''.join(newPassword)
	# print the new password
	print(newPassword)  

# ==================================
# PROGRAM INPUTS
print('Welcome to password validator ')
passwordInput = input('Password: \n         ')
print('Your password is: ')
validate(passwordInput) # run the validate function
print('\n')


print('Welcome to password generator ')
passwordLength = input('Password Length:  \n                ')
print('Your secure password is: ')
generate(passwordLength)  # run the generate function
print('\n\n')

