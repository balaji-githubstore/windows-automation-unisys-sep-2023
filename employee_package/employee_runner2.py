from employee_package.employee_module import Employee



emp1=Employee(101,'balaji')

emp1.print_employee_details()

emp2=Employee()
emp2.name='ken'

emp2.print_employee_details()

name=emp2.get_name
print(name)

print(emp2.get_name)