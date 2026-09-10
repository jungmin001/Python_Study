# import csv
# import numpy as np

# tall = np.array([153, 142, 178, 198, 203, 163])
# fixed = np.clip(tall, 158, 178)

# print(fixed)


#   files = "StudyFile/Data/11_diecasting_series.csv"
# data = []
# with open(files, "r", encoding="utf-8") as f:
#     reader = csv.reader(f)

#     next(reader)

#     for i in reader:
#         data.append(i[2])


# arr1 = [1, 2, 3, 4, 5]
# arr22 = np.cumsum(arr1)

# print(arr22)

# import csv
# import numpy as np

# files = "StudyFile/Data/11_diecasting_series.csv"

# pressure = []

# with open(files, "r", encoding="utf-8") as f:
#     reader = csv.reader(f)
#     header = next(reader)

#     idx = header.index("실린더압력")

#     for row in reader:
#         pressure.append(float(row[idx]))

# pressure = np.array(pressure)

# pressure[0] = 9999

# print(np.mean(pressure))

# pressure = np.clip(pressure, 100, 300)

# print(np.mean(pressure))

# import csv
# import numpy as np

# ct = np.genfromtxt(files, delimiter=",", skip_header=1, usecols=1)
# label = np.where(ct >= 1000, 2, np.where(ct >= 50, 1, 0))
# kinds, count = np.unique(label, return_counts=True)
# print(kinds, count)  # [0 1 2] [46 2 2]
# print(count / count.sum())  # [0.92 0.04 0.04]


# def col(c):
#     return np.genfromtxt(files, delimiter=",", skip_header=1, usecols=c)


# cyc, ct, cyl = col(0), col(1), col(2)
# i = ct.argmax()
# print(int(cyc[i]), ct[i])
# ch = np.abs(np.diff(ct))
# j = ch.argmax()
# print(int(cyc[j]), int(cyc[j + 1]))  # 49 50
# warn = np.where((ct >= 50) | (cyl < 150), 1, 0)
# print(round(warn.mean(), 2))
# top = np.argsort(ct)[::-1][:3]
# print(cyc[top].astype(int))

import pandas as pd

file = "StudyFile/Data/12_metro_compressor.csv"
file_semi = "StudyFile/Data/12_metro_compressor_semicolon.csv"

df = pd.read_csv("StudyFile/Data/12_metro_compressor.csv")
df.head()

print(df.shape)
print(df.columns)
print(df.columns.tolist())

print(df["오일온도"].values)

motor = df["모터전류"].values

print(f"모터 최소 전류 ")
