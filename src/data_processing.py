import pandas as pd
from pathlib import Path


class DataProcessing:
    def __init__(self, data_file):
        self.data_file = data_file

    def data_parser(self):
        data_set = pd.read_csv(self.data_file)
        data_set["Country Name"] = data_set["Country Name"].astype("string")
        data_set["Country Code"] = data_set["Country Code"].astype("string")
        data_set["Indicator Name"] = data_set["Indicator Name"].astype("string")
        data_set["Indicator Code"] = data_set["Indicator Code"].astype("string")
        year_columns = data_set.columns[4:]
        data_set[year_columns] = data_set[year_columns].apply(pd.to_numeric, errors = "coerce")

        return data_set
    
    def data_cleaning(self):
        pass
    
    def main(self):
        self.data_cleaning()
        self.data_parser()

if __name__ == "__main__":
    data_file = Path("data", "api_inflation_data.csv")
    data_processing = DataProcessing(data_file)
    data_processing.main()