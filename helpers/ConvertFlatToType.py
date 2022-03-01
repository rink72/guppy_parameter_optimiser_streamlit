import os
import csv
import pandas as pd
import json

def ConvertStringToFloat(string: str) -> float:
  try:
    return float(string)
  except:
    return None


# Convert the flat csv file to a JSON file
# based on model. This is mainly for ease of
# presenting the data

flatDataPath = os.path.join(os.path.dirname(__file__), '..', 'data', 'benchmark-data.csv')
typeDataPath = os.path.join(os.path.dirname(__file__), '..', 'data', 'benchmark-data.json')

typeData = list()

flatData = pd.read_csv(flatDataPath)

for r, row in flatData.iterrows():
  typeData.append(
    {
      "Procesor": row["Processor"],
      "Model": "FAST",
      "Samples": ConvertStringToFloat(row["FAST"])
    }
  )

  typeData.append(
    {
      "Procesor": row["Processor"],
      "Model": "HAC",
      "Samples": ConvertStringToFloat(row["HAC"])
    }
  )

  typeData.append(
    {
      "Procesor": row["Processor"],
      "Model": "SUP",
      "Samples": ConvertStringToFloat(row["SUP"])
    }
  )

typeFileHandle = open(typeDataPath, "w")
typeJson = json.dumps(typeData)
typeFileHandle.write(typeJson)
typeFileHandle.close()


