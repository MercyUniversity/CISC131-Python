class Employee:
    company_name = "TechCorp"  # Class attribute

    def __init__(self, name, position):
        self.name = name           # Instance attribute
        self.position = position    # Instance attribute

    def work(self):
        print(f"{self.name} is working as a {self.position} at {self.company_name}.")

    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name

    @staticmethod
    def is_workday(day):
        return day.lower() not in ["saturday", "sunday"]

# Usage
emp1 = Employee("Alice", "Developer")
emp2 = Employee("Bob", "Manager")

emp1.work()  # Output: Alice is working as a Developer at TechCorp.
emp2.work()  # Output: Bob is working as a Manager at TechCorp.

Employee.change_company_name("InnovateCorp")  # Change class attribute for all instances
emp1.work()  # Output: Alice is working as a Developer at InnovateCorp.
emp2.work()  # Output: Bob is working as a Manager at InnovateCorp.

# Using the static method
print(Employee.is_workday("Monday"))   # Output: True
print(Employee.is_workday("Sunday"))   # Output: False
