import pickle
def printDict(dictionary):
	for i in dictionary:
		print('{0:<10} :  {1:<10}'.format(i,dictionary[i]));
def new_contact(contact={}):
	while True:
		name = input("{0:<20}:  ".format('Enter Full Name')).lower(); 
		phone = input("{0:<20}:  ".format('Enter Phone Number'))
		email = input("{0:<20}:  ".format('Enter Email'))
		address = input("{0:<20}:  ".format('Enter Address'))
		birthday = input("{0:<20}:  ".format('Enter Birthday'))
		try:
			contact[name] = {'name':name}
		except UnboundLocalError:
			contact = {}
			contact[name] = {'name':name}
		contact[name]['phone'] = phone
		contact[name]['email'] = email
		contact[name]['address'] = address
		contact[name]['birthday'] = birthday
		customLabel = input("Add a Custom Detail [y/n]?").lower()
		while customLabel == 'y':
			label = input("{:<20}:  ".format('Enter Custom Label'))
			detail = input("{:<20}:  ".format('Enter Detail'))
			contact[name][label] = detail
			customLabel = input("Add a More Custom Detail [y/n]?").lower()
		print("\nComplete: ",name)
		printDict(contact[name])
		more = input("Do You Wish To Add More Contacts [y/n]?").lower()
		if more != 'y':
			break;
	return contact

def contact_mode():
	print("Options:")
	print("  (1) Search for a person")
	print("  (2) Create New Contact")
	print("  (3) Add to Existing Contact")
	print("  (4) View All Contacts")
	contact_options = input("   ");
	new_file_created = False;

	try:
		contact = pickle.load(open("contacts.bin","rb"))
	except EOFError:
		print("No Existing Contacts List Found")
		print('Creating New Contact ...')
		contact = new_contact()
		new_file_created = True
	except FileNotFoundError:
		print("No Existing Contacts List Found")
		print('Creating New Contact ...')
		contactFile = open("contacts.bin","wb")
		contact = new_contact()
		new_file_created = True

	if contact_options == '1' and new_file_created == False:
		try:
			search = input("Search for:  ").lower()
			printDict(contact[search])
		except KeyError:
			print("Person Not Found")

	if contact_options == '2' and new_file_created == False:
		contact = new_contact(contact)
	
	if contact_options == '3' and new_file_created == False:
		try:
			search = input("{:<20}:  ".format('Enter the Full Name')).lower()
			printDict(contact[search])
			while True:
				adding = input("{:<20}:  ".format('Enter New Label'))
				detail = input("{:<20}:  ".format('Enter Detail'))
				contact[search][adding] = detail
				more = input("Do You Wish to Add More Labels [y/n]?").lower()
				if more == 'n':
					break;
			print('\nComplete: ',search)
			printDict(contact[search])
		except KeyError:
			print("Person Not Found")
			print("Creating New Contact ...")
			new_contact()

	if contact_options == '4' and new_file_created == False:
		sorted_contact = sorted(contact.keys())
		for i in sorted_contact:
			printDict(contact[i])
			print("\n-\n")
	pickle.dump(contact, open("contacts.bin","wb"))


def percent2letter(percent, grades, name):
	try:
		percent = float(percent)
	except ValueError:
		print("ERROR: Not A Number")
		return grades
	if 90 < percent <= 100:
		grades[name] = {'percent':percent, 'letter':'A+','gpa':'4.0','pORf':'pass'}
	elif 85 < percent <= 90:
		grades[name] = {'percent':percent, 'letter':'A','gpa':'4.0','pORf':'pass'}
	elif 80 < percent <= 85:
		grades[name] = {'percent':percent, 'letter':'A-','gpa':'3.7','pORf':'pass'}
	elif 75 < percent <= 80:
		grades[name] = {'percent':percent, 'letter':'B+','gpa':'3.3','pORf':'pass'}
	elif 72 < percent <= 75:
		grades[name] = {'percent':percent, 'letter':'B','gpa':'3.0','pORf':'pass'}
	elif 70 < percent <= 72:
		grades[name] = {'percent':percent, 'letter':'B-','gpa':'2.7','pORf':'pass'}
	elif 66 < percent <= 70:
		grades[name] = {'percent':percent, 'letter':'C+','gpa':'2.3','pORf':'pass'}
	elif 63 < percent <= 66:
		grades[name] = {'percent':percent, 'letter':'C','gpa':'2.0','pORf':'pass'}
	elif 60 < percent <= 63:
		grades[name] = {'percent':percent, 'letter':'C-','gpa':'1.7','pORf':'pass'}
	elif 55 < percent <= 60:
		grades[name] = {'percent':percent, 'letter':'D+','gpa':'1.3','pORf':'pass'}
	elif 50 < percent <= 55:
		grades[name] = {'percent':percent, 'letter':'D','gpa':'1.0','pORf':'pass'}
	elif 0 <= percent <= 50:
		grades[name] = {'percent':percent, 'letter':'F','gpa':'0.0','pORf':'fail'}
	else:
		print("ERROR: Percentage Out of Range\nMust be Between 0 and 100")
	return grades

def new_student(grades = {}):
	while True:
		name = input("{0:<30}:  ".format("Enter Student's Name")).lower()
		student_percent = input("{0:<30}:  ".format("Enter Student's Percent Grade"))
		
		grades = percent2letter(student_percent, grades, name)
		try:
			print("Added: {0:<15} :  {1:<2.2f}%  |  {2:<2}  |  gpa: {3:<1.1f}  |  {4:<4}".format(name,float(student_percent),grades[name]['letter'],float(grades[name]['gpa']),grades[name]['pORf']))
			more = input("Add More Students [y/n]?").lower()
		except KeyError:
			more = 'y'; print("")
		except ValueError:
			more = 'y'; print("")
		if more !='y':
			break
	return grades
		
def grade_mode():
	# should outputs number of students, top student, and average
	print("Options:")
	print("  (1) View Class Summary")
	print("  (2) Find a Student")
	print("  (3) Add a Student")
	print("  (4) Student List")
	print("  (5) Student Ranking")
	grade_options = input("   ")
	new_file_created = False
	try:
		grades = pickle.load(open("grades.bin","rb"))
	except FileNotFoundError:
		print("No Existing Grades List Found")
		print('Creating New File ...')
		gradeFile = open("contacts.bin","wb")
		grades = new_student()
		new_file_created = True
	sorted_names = sorted(grades.keys())

	if grade_options == '1' and new_file_created == False:
		attendance = float(len(sorted_names))
		added_percent = 0
		gradeCount = {'A+':0 , 'A':0 , 'A-':0 , 'B+':0 , 'B':0 , 'B-':0 , 'C+':0 , 'C':0 , 'C-':0 , 'D+':0 , 'D':0 , 'F':0}
		letters = ['A+','A','A-','B+','B','B-','C+','C','C-','D+','D','F']
		for i in sorted_names:
			added_percent += float(grades[i]['percent'])
			letterGrade = grades[i]['letter']
			gradeCount[letterGrade] += 1

		average_percent = added_percent/attendance
		summary = {}
		summary = percent2letter(average_percent,summary,'class_summary')
		average_letter = summary['class_summary']['letter']
		average_gpa = summary['class_summary']['gpa']

		print("Class Summary")
		print("  {0:<25}:  {1:<10}".format('Number of Students',attendance))
		print("  {0:<25}:  {1:<2.2f}%".format('Average Percent',average_percent))
		print("  {0:<25}:  {1:<10}".format('Average Letter Grade',average_letter))
		print("  {0:<25}:  {1:<10}".format('Average GPA',average_gpa))
		for j in letters:
			print(" {0:<2}: {1:<3}".format(j,gradeCount[j]), end="   ")
			if attendance <= 30:
				star_weighting = 1
			else:
				star_weighting = attendance/30
			star_num = round(star_weighting*int(gradeCount[j]))
			print(star_num*'*')
	if grade_options == '2' and new_file_created == False:
		try:
			search = input("Search for:  ").lower()
			printDict(grades[search])
			edit = input("Edit Grade [y/n]]?").lower()
			if edit == 'y':
				new_grade = input("{0:<20}:  ".format("Enter New Grade"))
				grades = percent2letter(new_grade,grades,search)
				print("\n",search," edited:")
				printDict(grades[search])
		except KeyError:
			print("Student Not Found")

	if grade_options == '3' and new_file_created == False:
		grades = new_student(grades)

	if grade_options == '4' and new_file_created == False:
		sorted_names = sorted(grades.keys())
		print("Number of Students: ",len(sorted_names))
		for i in range(len(sorted_names)):
			print(i+1,". ",sorted_names[i])

	if grade_options == '5' and new_file_created == False:
		print(" Rank |     Name       |    Grade")
		ranked_names = [sorted_names[0]]
		for i in range(0,len(sorted_names)):
			inserted = False
			test_name = sorted_names[i]
			for j in range(len(ranked_names)):	
				if (grades[test_name]['percent'] >= grades[ranked_names[j]]['percent']):
					ranked_names.insert(j,test_name)
					inserted = True
					break
				elif j == len(ranked_names)-1 and inserted == False:
					ranked_names.insert(j,test_name)

		for k in range(len(ranked_names)-1):
			print("  {0:<2}.       {1:<15} {2:<2.2f}%".format(k+1,ranked_names[k],float(grades[ranked_names[k]]['percent'])))

	pickle.dump(grades, open("grades.bin","wb"))

if __name__ == "__main__":
	print("Select Mode:")
	print("  (1) Contacts"); print("  (2) Student Grades")
	file_structure = input("   ");
	if file_structure == '1':
		contact_mode()
	elif file_structure == '2':
		grade_mode();
