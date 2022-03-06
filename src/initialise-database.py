import psycopg2
import os

from configparser import ConfigParser
from modules.database import GuppyPostGres

# Script vars
pgConfigSection = "pg_credentials"
pgInitScripts = [
  os.path.join(os.path.dirname(__file__), "schema", "ProcessorDataCreate.sql"),
  os.path.join(os.path.dirname(__file__), "schema", "ProcessorDataSeed.sql")
]

# Check configuration vars
if not os.environ["GUPPY_CONFIG_PATH"]:
  raise Exception("Environment variable <GUPPY_CONFIG_PATH> not set.")


parser = ConfigParser()
parser.read(os.environ["GUPPY_CONFIG_PATH"])

pgCreds = {}
if parser.has_section(pgConfigSection):
    params = parser.items(pgConfigSection)
    for param in params:
        pgCreds[param[0]] = param[1]
else:
    raise Exception('Section {0} not found in the {1} file'.format(pgConfigSection, os.environ["GUPPY_CONFIG_PATH"]))

guppyDb = GuppyPostGres(**pgCreds)

# Run init scripts
for dbScriptPath in pgInitScripts:
  print("Executing <{0}>".format(dbScriptPath))

  with open(dbScriptPath) as f:
   dbScript = f.read()

  print(guppyDb.ExecuteScript(dbScript))

print(guppyDb.GetProcessorData())

