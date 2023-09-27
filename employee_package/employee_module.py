class Employee:
    company_name = None  #static or class variable
    company_location=None

    # non-static variable or instance variable
    def __init__(self,emp_id=None,emp_name=None):
        self.id = emp_id
        self.name = emp_name
        self.salary = None
        self.performance = None

    def print_employee_details(self):
        print(self.id)
        print(self.name)
        print('--------------------------')

    @staticmethod
    def get_author_name():
        return 'Balaji Dinakaran'

    @property
    def get_name(self) -> str:
        return self.name