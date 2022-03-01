import streamlit as st
import pandas as pd
import os


def GetBenchmarkData() -> pd.DataFrame:

  # We will likely change this in the future to pull from
  # a URL or dataabase
  flatDataPath = os.path.join(os.path.dirname(__file__), '..', 'data', 'benchmark-data.csv')
  typeDataPath = os.path.join(os.path.dirname(__file__), '..', 'data', 'benchmark-data.json')

  flatData = pd.read_csv(flatDataPath)
  typeData = pd.read_json(typeDataPath)
  return flatData, typeData


flatData, typeData = GetBenchmarkData()
cardTypes = flatData["Processor"]

st.write("### Guppy optimiser table")
selectedCards = st.multiselect("Select cards", cardTypes)

if not selectedCards:
  flatDisplayData = flatData
  typeDisplayData = typeData
else:
  flatDisplayData = flatData.loc[flatData["Processor"].isin(selectedCards)]
  typeDisplayData = typeData.loc[typeData["Processor"].isin(selectedCards)]

st.write(flatDisplayData)
st.vega_lite_chart(typeDisplayData, {
     'mark': {'type': 'bar', 'tooltip': True},
     "encoding": {
      "column": {"field": "Model", "type": "ordinal", "spacing": 10},
      "x": {
        "field": "Processor",
        "type": "ordinal",
        "axis": {"title": "", "labelAngle": 45}
      },
      "y": {"field": "Samples", "type": "quantitative"},
      "color": {
        "field": "Processor",
        "scale": {"range": ["#675193", "#ca8861", "#c7c7c7", "#ffbb00"]}
      },
      "tooltip": [
        {"field": "Processor", "title": "Hardware"},
        {"field": "Samples", "title": "samples/s"}
      ]
    }
 })

