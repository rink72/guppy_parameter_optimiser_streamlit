import os
import pandas as pd
import toml

from modules.database import GuppyPostGres

# Script vars
pgConfigSection = "pg_credentials"

# Check configuration vars
if not os.environ["GUPPY_CONFIG_PATH"]:
  raise Exception("Environment variable <GUPPY_CONFIG_PATH> not set.")

if not os.environ["GUPPY_CSV_PATH"]:
  raise Exception("Environment variable <GUPPY_CSV_PATH> not set.")


try:
  config = toml.load(os.environ["GUPPY_CONFIG_PATH"])
  pgCreds = config[pgConfigSection]

except:
    raise Exception('Unable to load configuration from <{0}> config file'.format(os.environ["GUPPY_CONFIG_PATH"]))

guppyDb = GuppyPostGres(**pgCreds)

csvData = pd.read_csv(os.environ["GUPPY_CSV_PATH"])

for index, record in csvData.iterrows():
  print ("Adding record for processor <{0}>, FAST: <{1}>, HAC: <{2}>, SUP: <{3}>".format(
    record["Processor"],
    record["FAST"],
    record["HAC"],
    record["SUP"]
  ))

  guppyDb.LoadProcessorRecord(record.to_dict())




