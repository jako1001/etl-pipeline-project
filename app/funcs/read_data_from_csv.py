import pandas as pd
from pandas import DataFrame

def read_csv_data(csv_file_path) -> DataFrame:
  df = pd.read_csv(csv_file_path)

  return df
