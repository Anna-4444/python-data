import re
import json
from statsmodels.graphics.mosaicplot import mosaic
import pandas as pd
import matplotlib.pyplot as plt

with open("data.json", "r") as text:
    data = json.load(text)

for item in data:
  item["Category"] = re.split(r"[.(]", item["Category"])[0] 
  # print(item["Category"])

classes = ["Mammalia", "Aves", "Reptilia"]
statuses = ["Endangered ", "Critically endangered ", "Vulnerable "]
mosaic_data = []

for item in data:
  if item["Category"] in statuses and item["Animal Class"] in classes:
    mosaic_data.append(item)
  # print(mosaic_data)    

mosaic_dataframe = pd.DataFrame(mosaic_data)

def props(key):
    if key[0] == "Critically endangered ":
      return {"color": "#c5cade"}
    elif key[0] == "Endangered ":
      return {"color": "#facdb6"}
    elif key[0] == "Vulnerable ":
      return {"color": "#a8dbd2"}

plt.rcParams["font.size"] = 8

mosaic(mosaic_dataframe, index=["Category", "Animal Class"], properties=props, gap= [0.02, 0.02], title="Conservation Status By Animal Class", axes_label=True)

plt.savefig("conservation-status.png")