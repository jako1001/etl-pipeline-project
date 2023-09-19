import re
import pandas as pd
from pandas import DataFrame


class Transform:
    def __init__(self, file_path) -> None:
        self.file_path = file_path

    def csv_to_dataframe(
        self,
    ) -> DataFrame:
        """Converts csv file at a given directory into a pandas DataFrame"""
        try:
            df = pd.read_csv(self.file_path)

            print(
                f"Successfully created DataFrame from the csv file located at: ({self.file_path})"
            )
            return df

        except FileNotFoundError:
            raise FileNotFoundError(f"Something went wrong while reading the csv with file path ({self.file_path}). Is the file path correct?")

    def read_email_and_number_unstructured(self) -> DataFrame:
        try:
            with open(self.file_path, "r") as file:
                text = file.read()

                emails = re.findall(
                    r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b", text
                )

                phone_numbers = re.findall(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}", text)

            data = list(zip(emails, phone_numbers))
            df = pd.DataFrame(data, columns=["Emails", "Phone Numbers"])

            return df

        except FileNotFoundError:
            raise FileNotFoundError(f"Something went wrong while reading the file with file path ({self.file_path}). Is the file path correct?")
