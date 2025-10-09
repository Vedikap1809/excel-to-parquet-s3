import pandas as pd

class ExcelToParquetConverter:
    def __init__(self, excel_file, parquet_file):
        self.excel_file = excel_file
        self.parquet_file = parquet_file

    def convert(self):
        df = pd.read_excel(self.excel_file)
        df.to_parquet(self.parquet_file, engine='pyarrow', index=False)

if __name__ == "__main__":
    excel_filename = "em.xlsx"
    parquet_filename = "employee.parquet"

    converter = ExcelToParquetConverter(excel_filename, parquet_filename)
    converter.convert()
