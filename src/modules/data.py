import pandas as pd
import streamlit as st
import modules.converters as conv

from modules.database import GuppyPostGres


# Helper data functions

def GetBenchmarkData(db) -> pd.DataFrame:

  flatData = pd.DataFrame(db.GetProcessorData())
  typeData = conv.ConvertFlatToType(flatData=flatData)

  return flatData, typeData