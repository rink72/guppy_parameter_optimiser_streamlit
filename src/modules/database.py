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

  def GetProcessorData(self):

    cursor = self.dbConnection.cursor()
    cursor.execute("SELECT * FROM ProcessorData")

    if not cursor.rowcount or cursor.rowcount == 0:
      return

    data = cursor.fetchall()

    records = []
    for processorRecord in data:
      records.append(
        {
          "Processor": processorRecord[0],
          "FAST": processorRecord[1],
          "HAC": processorRecord[2],
          "SUP": processorRecord[3]
        }
      )

    return records

  def LoadProcessorRecord(self, record: dict):

    cursor = self.dbConnection.cursor()
    cursor.execute(
      """
      INSERT INTO
        ProcessorData (processor, fastops, hacops, supops)
      VALUES
        (%s, %s, %s, %s)
      ON CONFLICT DO NOTHING
      """,
      (record["Processor"],
      record["FAST"],
      record["HAC"],
      record["SUP"],)
    )

  def Close(self):
    self.dbConnection.close()

