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

data = pd.read_csv('D:/지승환/sleep/고속도로 교통사고 현황.csv',encoding='euc-kr')

plt.figure(figsize=(10,6))
data_dead = data.sort_values(by=["사고"], ascending=False)
sns.barplot(x="연도",y="사고", data=data_dead)
plt.title("연도별 교통사고 횟수")
plt.show()
