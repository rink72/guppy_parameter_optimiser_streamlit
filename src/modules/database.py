from sqlite3 import Row
import psycopg2

class GuppyPostGres():

  dbConnection = None

  def __init__(self, host: str, database: str, user: str, password: str) -> None:

      try:
        self.dbConnection = psycopg2.connect(
          host=host,
          database=database,
          user=user,
          password=password
        )

      except Exception as Err:
        print(Err)
        raise Exception("Unable to connect to database")

      self.SetDbConnectionSettings()


  def SetDbConnectionSettings(self) -> None:
    try:
      self.dbConnection.autocommit = True

    except Exception as Err:
      print(Err)
      raise Exception("Unable to configure database connection settings")

  def GetDbVersion(self):
    cursor = self.dbConnection.cursor()
    cursor.execute("SELECT version()")

    return cursor.fetchone()

  def ExecuteScript(self, sqlScript: str) -> list:

    cursor = self.dbConnection.cursor()
    cursor.execute(sqlScript)

    if cursor.rowcount > 0:
      return cursor.fetchall()
    else:
      return []

  def GetProcessorData(self):

    cursor = self.dbConnection.cursor()
    cursor.execute("SELECT * FROM ProcessorData")

    if not cursor.rowcount or cursor.rowcount == 0:
      return

    data = cursor.fetchall()

    for processorRecord in data:


