# import pandas as pd

# CD = "Data/16_diecasting.csv"
# TP = "Data/17_열처리.csv"

# df = pd.read_csv(CD)

# Q1 = df["실린더압력"].quantile(0.25)
# Q2 = df["실린더압력"].quantile(0.5)
# Q3 = df["실린더압력"].quantile(0.75)

# print(Q1, Q2, Q3)

# print(df["실린더압력"].describe())

# import pandas as pd

# CD = "Data/16_diecasting.csv"

# df = pd.read_csv(CD)

# print(df.head())
# print(df.shape)
# print(df.columns.tolist())
# df.info()

# import pandas as pd

# CD = "Data/16_diecasting.csv"

# df = pd.read_csv(CD)

# 최소 = df["실린더압력"].min()
# 최대 = df["실린더압력"].max()
# 범위 = 최대 - 최소

# print(최소)
# print(최대)
# print(round(범위, 1))

# import pandas as pd

# CD = "Data/16_diecasting.csv"

# df = pd.read_csv(CD)
# Set = df.sort_values("사이클타임", ascending=False)
# print(Set[["샷", "사이클타임", "상태"]].head())


# import pandas as pd

# CD = "Data/16_diecasting.csv"

# df = pd.read_csv(CD)

# 평균 = df["사이클타임"].mean()
# 중앙값 = df["사이클타임"].median()

# 정상 = df[df["상태"] == 0]

# 정상평균 = 정상["사이클타임"].mean()

# print(round(평균, 2))
# print(중앙값)
# print(round(정상평균, 2))

# import pandas as pd

# CD = "Data/16_diecasting.csv"

# df = pd.read_csv(CD)

# Q1 = df["실린더압력"].quantile(0.25)
# Q2 = df["실린더압력"].quantile(0.50)
# Q3 = df["실린더압력"].quantile(0.75)

# print(Q1)
# print(Q2)
# print(Q3)

# print(df["실린더압력"].median())

# import pandas as pd

# CD = "Data/16_diecasting.csv"

# df = pd.read_csv(CD)

# 요약 = df[["실린더압력", "주조압력", "사이클타임", "비스킷두께", "형체력"]].describe().T

# 요약["격차"] = (요약["mean"] - 요약["50%"]).abs()

# 결과 = 요약.sort_values("격차", ascending=False)

# print(결과[["mean", "50%", "max", "격차"]].head(3))

# import pandas as pd

# CD = "Data/16_diecasting.csv"

# df = pd.read_csv(CD)

# q = df[["실린더압력", "사이클타임", "비스킷두께"]].quantile([0.25, 0.50, 0.75])

# print(q)

# IQR = q.loc[0.75] - q.loc[0.25]

# print(IQR)

# import pandas as pd

# df = pd.DataFrame(
#     {"설비": ["A", "B", "C", "D", "E"], "temperature": [85, 95, 88, 101, 90]}
# )

# print(df)

# check = df["temperature"] > 92.75
# print(check)
# print(df[check])


# import pandas as pd

# CD = "Data/16_diecasting.csv"

# df = pd.read_csv(CD)

# Q1 = df["사이클타임"].quantile(0.25)
# Q2 = df["사이클타임"].quantile(0.50)
# Q3 = df["사이클타임"].quantile(0.75)

# IQR = Q3 - Q1

# lower = Q1 - 1.5 * IQR
# upper = Q3 + 1.5 * IQR

# mask = (df["사이클타임"] < lower) | (df["사이클타임"] > upper)

# print(mask.sum())
# print(df[~mask].shape)

# print(round(mask.mean() * 100, 1))


# import pandas as pd

# CD = "Data/16_diecasting.csv"

# df = pd.read_csv(CD)

# Q1 = df["사이클타임"].quantile(0.25)
# Q3 = df["사이클타임"].quantile(0.75)

# IQR = Q3 - Q1

# lower = Q1 - 1.5 * IQR
# upper = Q3 + 1.5 * IQR

# print(round(Q1, 2))
# print(round(Q3, 2))
# print(round(IQR, 2))
# print(round(lower, 2))
# print(round(upper, 2))


# import pandas as pd

# CD = "Data/16_diecasting.csv"

# df = pd.read_csv(CD)

# Q1 = df["사이클타임"].quantile(0.25)
# Q3 = df["사이클타임"].quantile(0.75)

# IQR = Q3 - Q1

# lower = Q1 - 1.5 * IQR
# upper = Q3 + 1.5 * IQR

# mask = (df["사이클타임"] < lower) | (df["사이클타임"] > upper)

# print(df[mask][["샷", "사이클타임", "상태"]])

# print(mask.sum())
# print(round(mask.mean() * 100, 1))


# import pandas as pd

# CD = "Data/16_diecasting.csv"

# df = pd.read_csv(CD)

# Q1 = df["실린더압력"].quantile(0.25)
# Q3 = df["실린더압력"].quantile(0.75)

# IQR = Q3 - Q1

# lower = Q1 - 1.5 * IQR
# upper = Q3 + 1.5 * IQR

# mask = (df["실린더압력"] < lower) | (df["실린더압력"] > upper)

# rm = df.loc[~mask, "실린더압력"]

# Set = df["실린더압력"].clip(lower=lower, upper=upper)

# ch = df["실린더압력"].mask(mask)

# Cu = ch.fillna(ch.median())

# print(round(df["실린더압력"].mean(), 2))
# print(round(rm.mean(), 2))
# print(round(Set.mean(), 2))
# print(round(Cu.mean(), 2))


import pandas as pd

CD = "Data/16_diecasting.csv"

df = pd.read_csv(CD)

Q1 = df["사이클타임"].quantile(0.25)
Q3 = df["사이클타임"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

print(df.duplicated().sum())

print(df[df.duplicated()])

print(df.duplicated(keep=False).sum())
