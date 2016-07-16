from datetime import date

student = {'name': ['David', 'Njakai'], 'year_of_birth': 1992, 'phone_number': '0790505019'}
age = date.today().year - student.get('year_of_birth')

print('last name is {0}'.format(student.get('name')[1]))
print('firsname: {0} lastname {1}'.format(student.get('name')[0], student.get('name')[1]))
print("phone number is {0}".format(student.get('phone_number')))
print('year of birth is {0}'.format(student.get('year_of_birth')))
print('age is {0}'.format(age))