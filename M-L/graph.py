import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
class Mat:
 def Top(self):
  df=pd.read_csv("EPL_20_21.csv")
  fig,axes=plt.subplots(nrows=3,ncols=2,figsize=(8,8))
  fig.suptitle("Premier Lig")
  axes[0,0].plot(df.groupby("Club")["Goals"].sum().sort_values(ascending=False).head(5),color="y")
  axes[0,0].set_title("Top Scored Teams")
  axes[0,1].plot(df.groupby("Name")["Goals"].sum().sort_values(ascending=False).head(5),color="r")
  axes[0,1].set_title("Top Scored Players")
  axes[1,0].plot(df.groupby("Name")["Mins"].sum().sort_values(ascending=False).head(5),color="b")
  axes[1,0].set_title("Top Mins Players")
  axes[1,1].plot(df.groupby("Name")["Matches"].sum().sort_values(ascending=False).head(5),color="g")
  axes[1,1].set_title("Top Played Players")
  axes[2,0].plot(df.groupby("Name")["xG"].sum().sort_values(ascending=False).head(5),color="purple")
  axes[2,0].set_title("Top Played xG Players")
  axes[2,1].plot(df.groupby("Name")["Yellow_Cards"].sum().sort_values(ascending=False).head(5),color="gray")
  axes[2,1].set_title("Top Yellow Cards")
  plt.legend()
  plt.tight_layout()
  plt.show()



