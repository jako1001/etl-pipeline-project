import pandas as pd
from pandas import DataFrame


class Transform:
    def __init__(self, file_path, type) -> None:
        self.file_path = file_path
        self.type = type

    def csv_to_dataframe(
        self,
    ) -> DataFrame | str:
        """Converts csv file at a given directory into a pandas DataFrame"""
        if self.type == "csv":
            try:
                df = pd.read_csv(self.file_path)

                print(
                    f"Successfully created DataFrame from the csv file located at: ({self.file_path})"
                )
                return df

            except:
                return f"Something went wrong while reading the csv with file path ({self.file_path}). Is the file path correct?"

        return "File is not a csv."

    # def dataframe_to_sql_format(self, dataframe, db_conn, column):
    #     return dataframe.to_sql("users", con=db_conn, if_exists="append", index=False)
