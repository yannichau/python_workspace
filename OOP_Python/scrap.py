# Define a class
class Employee:
	
	# Class variable
	num_of_emps = 0
	raise_amount = 1.04
	
	# Constructor (initialise members)
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + last + "@company.com"
		Employee.num_of_emps += 1 # don't use self, will be different for different unique instances.

	# Regular Methods
	def print_full_name(self):
		print ('{} {}'.format(self.first, self.last))

	def apply_raise(self):
		# self.pay = int(self.pay*1.04)
		self.pay = int(self.pay * self.raise_amount)
	
	# Class Method
	@classmethod # this means that class is the first argument. cls used for convention (can't use class)
	def set_raise_amt(cls, amount):
		cls.raise_amount = amount
	
	@classmethod
	# Alternative constructor from long string
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split("-")
		return cls(first, last, pay)

	@staticmethod
	# just takes in arguments in needs, for when you don't need to access the class.
	def is_workday(day):
		if day.weekday() == 5 or  day.weekday() == 6: # Saturday or Sunday
			return False
		return True
				
# Unique instance variables of employees (preferred)
emp_1 = Employee("Corey", "Schafer", 5000)
emp_2 = Employee("Yanni", "Chau", 10000)

# Assign members manually
emp_1.first = "Corey"
emp_1.last = "schafer"
emp_1.email = "coreyschafer@company.com"
emp_1.pay = 5000

# Call print method (2 ways)
emp_1.print_full_name()
Employee.print_full_name(emp_1)