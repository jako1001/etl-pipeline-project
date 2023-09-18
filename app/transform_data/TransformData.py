import pandas as pd

class TransformData:
  def __init__(self, file_path, type) -> None:
    self.file_path = file_path
    self.type = type

  def csv_to_dataframe(self):
    if self.type == "csv":
      try:
        df =  pd.read_csv(self.file_path)

        return df
      except:
        return "Something went wrong while reading the csv. Is the file path correct?"

    return "File is not a csv."
