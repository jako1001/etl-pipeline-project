import pandas as pd
from pandas import DataFrame


class Transform():
    def __init__(self, file_path) -> None:
        self.file_path = file_path

    def ppp(self):
        print("COLUMN NAMES IN TRANSFORM: ", self.column_names)

    def csv_to_dataframe(
        self,
    ) -> DataFrame | str:
        """Converts csv file at a given directory into a pandas DataFrame"""
        try:
            df = pd.read_csv(self.file_path)

            print(
                f"Successfully created DataFrame from the csv file located at: ({self.file_path})"
            )
            return df

        except:
            return f"Something went wrong while reading the csv with file path ({self.file_path}). Is the file path correct?"
