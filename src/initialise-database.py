import os
import toml

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

try:
  config = toml.load(os.environ["GUPPY_CONFIG_PATH"])
  pgCreds = config[pgConfigSection]

except:
    raise Exception('Unable to load configuration from <{0}> config file'.format(os.environ["GUPPY_CONFIG_PATH"]))

guppyDb = GuppyPostGres(**pgCreds)

# Run init scripts
for dbScriptPath in pgInitScripts:
  print("Executing <{0}>".format(dbScriptPath))

  with open(dbScriptPath) as f:
   dbScript = f.read()

  guppyDb.ExecuteScript(dbScript)


print("Retrieving current <ProcessorData> table records \n")
print(guppyDb.GetProcessorData())

