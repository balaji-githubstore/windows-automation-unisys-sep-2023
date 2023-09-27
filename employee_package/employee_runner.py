from employee_package.employee_module import Employee

Employee.company_name='Unisys'
Employee.company_location='chennai'

Employee.company_name='Unisys Ltd'

emp1=Employee()
emp2=Employee()
emp3=Employee()

emp1.id=101
emp1.name='saul'
emp1.salary=9000
emp1.performance='A'

emp2.id=102
emp2.name='peter'
emp2.salary=5000
emp2.performance='C'

print(emp1)
print(emp2)

print(type(emp1))

print(emp1.id)

emp2.print_employee_details()
emp1.print_employee_details()

emp3.print_employee_details()

author_name=Employee.get_author_name()
print(author_name)

# Employee.print_employee_details(emp1)