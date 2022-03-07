import os
import csv
import pandas as pd
import json

def ConvertStringToFloat(string: str) -> float:
  try:
    return float(string)
  except:
    return None

def ConvertStringToInt(string: str) -> int:
  try:
    return int(ConvertStringToFloat(string))
  except:
    return None


# Convert the flat csv file to a JSON file
# based on model. This is mainly for ease of
# presenting the data

def ConvertFlatToType(flatData: pd.DataFrame) -> pd.DataFrame:

  typeData = list()

  for r, row in flatData.iterrows():
    typeData.append(
      {
        "Processor": row["Processor"],
        "Model": "FAST",
        "Samples": ConvertStringToFloat(row["FAST"])
      }
    )

    typeData.append(
      {
        "Processor": row["Processor"],
        "Model": "HAC",
        "Samples": ConvertStringToFloat(row["HAC"])
      }
    )

    typeData.append(
      {
        "Processor": row["Processor"],
        "Model": "SUP",
        "Samples": ConvertStringToFloat(row["SUP"])
      }
    )

  return pd.DataFrame(typeData)
