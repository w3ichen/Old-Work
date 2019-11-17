# ==================================
# Name: Weichen Qiu
# ID: 1578205
# Collaborated with: n/a
# CMPUT 274, Fall 2019
#
# Assignment: Weekly Exercise 1
# Description: password validator
# ==================================

import random   # import random module to generate random numbers

'''
Description: validate function will take an input and determing
			if it is secure, insecure or invalid
Arguments: password is the input from user
Returns: outputs either secure, insecure, or invalid
'''

#validate function
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

	for i in range(0,len(password)):  # loops through each element of password string
		if password[i].islower() == True:  # if the element is lower case
			lowerCount+=1  # count number of lower cases
		if password[i].isupper() == True:  # if the element is upper case
			upperCount+=1  # count number of upper cases
		if password[i].isdigit() == True:  # if the element is a number
			numCount+=1  # count number of digits


	# check for special characters
	specialCount = 0  # define variable to count special characters
	special = list('!#$%&\'()*+,./:;<=>?@[]^`{|}~') #puts the special characters in a list
	for i in range(0,len(special)):  # loop through all characters to see if it is in password
		sCharacter = password.count(special[i])  # counts how many of the special characters are in password
		specialCount += sCharacter  # add up number of special characters


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

	n = int(n)  # convert n to integer

	if n < 8:  # n length must be 8 or more
		print('Error: Password must have a length of 8 or more') #print error message
		return 0   # stop program
	newPassword = []  # empty list to make new password


# define variables to count password requirements
	lowerCount = 0
	upperCount = 0
	numCount = 0
	specialCount = 0
	loopCount = 0  # counts number of loops so can do quality check before password is fsully defined

	while len(newPassword) != n:  # keeps looping until password has the length needed
	
		typeNum = random.randint(1,4)  # generate a number to decide what type next element will be

		if typeNum == 1:  # generates upper case
			upperLetter = random.randint(65,90)  # generates a random upper case letter
			upperLetter = chr(upperLetter)  # converts to letter using chr
			newPassword.append(upperLetter)  # add to new password list

			upperCount+=1  # add count
		elif typeNum == 2:  # generates lower case
			lowerLetter = random.randint(97,122)  # generates a random lower case letter
			lowerLetter = chr(lowerLetter)  # converts to letter using chr
			newPassword.append(lowerLetter)  # add to new password list

			lowerCount+=1  # add count
		elif typeNum == 3:  # generates number
			ranNum = random.randint(0,9)  # generates a random number
			ranNum = str(ranNum)  # convert to string
			newPassword.append(ranNum)  # add to new password list

			numCount+=1  # add count
		elif typeNum == 4:  # generate special character
			special = list('!#$%&\'()*+,./:;<=>?@[]^`{|}~')  # puts the special characters in a list
			specialLetter = random.randint(0,len(special)-1)  # generate a random number in range of special list
			specialLetter = special[specialLetter]  # set to special character
			newPassword.append(specialLetter)  # add to new password list

			specialCount+=1  # add count

			
# quality control, check that all conditions are included
		if  loopCount == n-4:  # stop before full password in order to check requirements are met. must have enough spaces left if no requirements are met
			
			randomIndex = random.randint(0,n-4)  # generate random number to determine a random index

			if upperCount == 0:  # if there are no upper case letters
				upperLetter = random.randint(65,90)  # generates a random upper case letter
				upperLetter = chr(upperLetter)  # convert to letter
				# inserts to a random position in newPassword using randomIndex
				newPassword.insert(randomIndex,upperLetter)  # add to new password list

			elif lowerCount == 0:  # if there are no lower case letters
				lowerLetter = random.randint(97,122)  # generates a random lower case letter
				lowerLetter = chr(lowerLetter)  # convert to letter
			# inserts to a random position in newPassword using randomIndex
				newPassword.insert(randomIndex, lowerLetter)#add to new password list

			elif numCount == 0:  # if there are no numbers
				ranNum = random.randint(0,9)  # generates a random number
				ranNum = str(ranNum)  # convert to string
			# inserts to a random position in newPassword using randomIndex
				newPassword.insert(randomIndex,ranNum)#add to new password list

			elif specialCount:  # if there are no special characters
				special = list('!#$%&\'()*+,./:;<=>?@[]^`{|}~')  # puts the special characters in a list
				specialLetter = random.randint(0,len(special)-1)  # generate random index number for special list
				specialLetter = special[specialLetter]  # set to special character
			# inserts to a random position in newPassword using randomIndex
				newPassword.insert(randomIndex,specialLetter)  # add to new password list
			loopCount += 1
	newPassword = ''.join(newPassword)  # converts newPassword list to string
	
	print(newPassword)  # print the new password


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

