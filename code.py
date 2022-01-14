from os import access
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("final_v3.csv")

distance = df["Distance"].to_list()
gravity = df["Gravity"].to_list()
#print(distance[0:3])

for index, star_data in enumerate(distance):
  if float(star_data) > 100:
    df = df.drop(labels=index, axis=0)
  else:
    if float(gravity[index]) < 150 or float(gravity[index]) > 350:
      df = df.drop(labels=index, axis=0)

del df["Row_Number"]

df.to_csv("main.csv", index=False)

# add index
df = pd.read_csv("main.csv")
df.to_csv("main_v2.csv")
# 158 planets within 100 light years