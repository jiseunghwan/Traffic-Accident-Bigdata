import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import os
import seaborn as sns
import platform

if platform.system() == 'Windows':
    matplotlib.rc('font', family='Malgun Gothic')
elif platform.system() == 'Darwin': # Mac
    matplotlib.rc('font', family='AppleGothic')
else: #linux
    matplotlib.rc('font', family='NanumGothic')

plt.figure(figsize=(10,6))

ratio = [6159, 28762, 21132]
ratio1 = [569, 2845, 496]
ratio2 = [179, 861, 794]

labels = ['사망', '부상', '그 외']
colors = ['#ff9999', '#ffc000', '#8fd9b6']
wedgeprops = {'width':0.7, 'edgecolor':'w', 'linewidth':5}

plt.subplot(131)
plt.pie(ratio1, labels=labels, autopct='%.1f%%', startangle=260, counterclock = False,
        colors = colors, wedgeprops = wedgeprops)
plt.title("2000 교통사고 현황")

plt.subplot(132)
plt.pie(ratio2, labels=labels, autopct='%.1f%%', startangle=260, counterclock = False,
        colors = colors, wedgeprops = wedgeprops)
plt.title("2020 교통사고 현황")

plt.subplot(133)
plt.pie(ratio, labels=labels, autopct='%.1f%%', startangle=260, counterclock = False,
        colors = colors, wedgeprops = wedgeprops)
plt.title("평균 교통사고 현황")

plt.show()
