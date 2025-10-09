import pandas as pd
from faker import Faker

class EmployeeDataGenerator:
    def __init__(self, num_records, filename):
        self.num_records = num_records
        self.filename = filename
        self._fake = Faker('en_IN')
        self.rows = []  

    def generate_employees(self):
        for i in range(1, self.num_records + 1):
            row = [
                f"EMP{i}",                             
                self._fake.name(),               
                self._fake.random_int(10000,200000),    
                self._fake.date_between(start_date='-3y', end_date='today') 
            ]
            self.rows.append(row)
        print("Employee data generation completed.")

    def employees_to_dataframe(self):
        columns = ["empid", "name", "salary", "salary_date"]
        df = pd.DataFrame(self.rows, columns=columns)
        return df

    def save_to_excel(self):
        df = self.employees_to_dataframe()
        df.to_excel(self.filename, index=False)
        print(f"Data successfully saved to {self.filename}.")


if __name__ == "__main__":
    num_records = 1000000
    output_filename = 'em.xlsx'

    generator = EmployeeDataGenerator(num_records, output_filename)
    print(generator.employees_to_dataframe().dtypes)
    generator.generate_employees()
    generator.save_to_excel()
