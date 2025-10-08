import csv
from faker import Faker

class Employee:    
    _fake = Faker('en_IN')
    
    def __init__(self):
        self.empid = f"EMP-{self._fake.unique.random_int(min=1, max=10)}"
        self.name = self._fake.unique.name()
        self.salary = self._fake.random_int(min=10000, max=100000)
        self.salary_date = self._fake.date_this_year()

class EmployeeDataGenerator:    
    def __init__(self, num_records, filename):
        self.num_records = num_records
        self.filename = filename
    
    def generate_and_save(self):
        print(f"Generating {self.num_records} employee records")
        
        with open(self.filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['empid', 'name', 'salary', 'salary_date'])
            
            for i in range(self.num_records):
                employee = Employee()
                writer.writerow([employee.empid, employee.name, employee.salary, employee.salary_date])
                
                # Print progress to the console
                if (i + 1) % 10 == 0:
                    print(f"Progress: {i + 1}/{self.num_records} records written.")

        print(f"\nSuccessfully generated {self.num_records} records to {self.filename}.")

if __name__ == "__main__":
    num_records_to_generate = 10
    output_filename = 'employees_1.csv'

    generator = EmployeeDataGenerator(num_records_to_generate, output_filename)
    generator.generate_and_save()
    