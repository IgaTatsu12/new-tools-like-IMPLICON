# -*- coding: utf-8 -*-
"""MethHeatmap

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Gr6Y-Ex1CUSO0BhJeTEanKq4ftsWj9rD
"""

from google.colab import drive
drive.mount("/content/drive")

percentageData = []
averageData=[]
titleList=[]
rangeList=[]
# placeData=[]

import os
import gzip
import numpy as np
with open("/content/drive/MyDrive/Colab Notebooks/CpG_imprinted_positions_mouse.txt",mode="r") as ref:
  for line in ref:
    if(line.strip().split("\t")[4].find("Dlk1") != -1):
      rangeList.append(int(line.strip().split("\t")[2]))
print(len(rangeList))

for pathname, dirnames, filenames in os.walk("/content/drive/MyDrive/Colab Notebooks/IMPLICON"):
  for file in filenames:
    if(file[-12:] == "heart.cov.gz"):
      # print(file)
      newData=[]
      with gzip.open("/content/drive/MyDrive/Colab Notebooks/IMPLICON/"+file, 'rt', 'utf-8') as gz:
        for line in gz:
          if(line.strip().split("\t")[0] == "12" and int(line.strip().split("\t")[1]) in rangeList) :
            newData.append(float(line.split("\t")[3]))
            print(file,line.strip().split("\t")[1],line.strip().split("\t")[2])
      # if(np.average(newData) > -1):
        
      averageData.append(np.average(newData))
      percentageData.append(np.array(newData))
      titleList.append(file.split(".")[0][11:])

print(percentageData)
print(len(percentageData[0]),len(percentageData[1]),len(percentageData[2]))

import matplotlib.pyplot as plt
 
# ヒストグラムを出力
# plt.hist(averageData,bins=20)
# 箱ひげ図を出力
fig, ax = plt.subplots()


bp = ax.boxplot(percentageData) # 複数指定する場合はタプル型で渡します。
ax.set_xticklabels(titleList)
ax.set_ylim(0,100)

plt.title('Dlk1')
plt.show()

# print Heatmap
import seaborn as sns
sns.heatmap(percentageData,yticklabels=titleList)
plt.title('Dlk1')
plt.show()