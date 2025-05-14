class Employee:

    company = 'Guinya Studio'
    
    # Constructor
    # def Employee():
    def __init__(self, name, age, salary, dept, title):
        self.name = name
        self.age = age
        self.salary = salary
        self.email = self.generateEmail(Employee)
        self.job = self.Job(dept, title)

    def generateEmail(self, cls):
        return(f'{self.name}@{cls.company}.com')

    # def __init__(self):
    #     self.name = 'Default'
    #     self.age = 0
    #     self.salary = 0
    #     self.job = 'None'
    
    # always take self as argument 
    def showEmployeeData(self):
        print(self.name, self.age, self.salary, self.job)
    
    def showInfo(self):
        print(self.name, self.age, self.salary, self.job, self.email)

    @classmethod
    def changeCompanyName(cls, newName):
        cls.company = newName

    def __str__(self):
        return (f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}, '
                f'Position: {self.job}, Email: {self.email}.')
    
    class Job:
    
        def __init__(self, dept, title):
            self.dept = dept
            self.title = title

        def __str__(self):
            return f"Department: {self.dept}, Title: {self.title}"
        
        def showInfo(self):
            print(f"Department: {self.dept}, Title: {self.title}")

obj = Employee('Jane', '34', '45000', 'OS', 'Engineer')
Employee.changeCompanyName('Guinya Code')
# obj.showEmployeeData() also works
# Employee.showEmployeeData(obj)

# ThisIsPascalCase
# thisIsCamelCase

# Job makes it static, ig
obj.job.showInfo()