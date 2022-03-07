import streamlit as st
import pandas as pd
import modules.data as data

from modules.database import GuppyPostGres

guppyDb = GuppyPostGres(**st.secrets.pg_credentials)


if "flatData" not in st.session_state or "typeData" not in st.session_state:
  flatData, typeData = data.GetBenchmarkData(db=guppyDb)
  st.session_state["flatData"] = flatData
  st.session_state["typeData"] = typeData
else:
  flatData = st.session_state["flatData"]
  typeData = st.session_state["typeData"]

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

guppyDb.Close()

