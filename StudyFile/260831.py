# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.set_theme(style="whitegrid")

# cd = "StudyFile/Data/20_cmapss_fd001_sample_65_260831.csv"

# df = pd.read_csv(cd)

# #print(df[["unit_nr", "time_cycles", "s_2", "s_4"]].head())

# print(df.shape)
# print(df.columns)
# print(df.head)


# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.set_theme(style="whitegrid")

# cd = "StudyFile/Data/20_cmapss_fd001_sample_65_260831.csv"

# df = pd.read_csv(cd)

# print(df.isna().sum())
# print(df.describe())



# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.set_theme(style="whitegrid")

# cd = "StudyFile/Data/20_cmapss_fd001_sample_65_260831.csv"

# df = pd.read_csv(cd)

# num = df[df["unit_nr"] == 2].sort_values("time_cycles")

# a, b = num["s_2"].iloc[0], num["s_2"].iloc[-1]

# print("s_1", a, ": ", b, '떡상' if a < b else '떡락')



# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.set_theme(style="whitegrid")

# cd = "StudyFile/Data/20_cmapss_fd001_sample_65_260831.csv"

# df = pd.read_csv(cd)

# engine_2 = df[df["unit_nr"] == 2]
# print(engine_2[["s_2", "s_11", "s_12"]].describe())
# print(engine_2[["s_2", "s_11", "s_12"]].mean())



# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.set_theme(style="whitegrid")

# cd = "StudyFile/Data/20_cmapss_fd001_sample_65_260831.csv"

# df = pd.read_csv(cd)

# for c in ['s_1', 's_6', 's_7', 's_11', 's_12']:
#     print(c, round(df[c].std(), 3))

# print(int(df.isna().sum().sum()))


# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import matplotlib.pyplot as plt

# sns.set_theme(style="whitegrid")

# cd = "StudyFile/Data/20_cmapss_fd001_sample_65_260831.csv"

# df = pd.read_csv(cd)

# e2 = df[df["unit_nr"] == 2]

# plt.plot(e2['time_cycles'], e2['s_11'])
# plt.title('Engine 2 - s_11'); 
# plt.xlabel('time_cycles')
# plt.show()

# plt.plot(e2['time_cycles'], e2['s_12'])
# plt.title('Engine 2 - s_12'); 
# plt.show() 



# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import matplotlib.pyplot as plt

# sns.set_theme(style="whitegrid")

# cd = "StudyFile/Data/20_cmapss_fd001_sample_65_260831.csv"

# df = pd.read_csv(cd)

# e2 = df[df["unit_nr"] == 2]

# plt.plot(e2["time_cycles"], e2["s_2"])
# plt.plot(e2["time_cycles"], e2["s_7"])
# plt.legend()
# plt.show()

# plt.plot(e2["time_cycles"], e2["s_14"])
# plt.plot(e2["time_cycles"], e2["s_20"])
# plt.legend()
# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import matplotlib.pyplot as plt

# sns.set_theme(style="whitegrid")

# cd = "StudyFile/Data/20_engine01_timestamp_sample_67_260831.csv"

# df = pd.read_csv(cd)

# ts = pd.to_datetime(df["timestamp"])
# print(ts.dt.year.iloc[0], ts.dt.month.iloc[0])
# print(ts.dt.day.iloc[0], ts.dt.hour.iloc[0])
# print(ts.dt.hour.head(3).tolist())



# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import matplotlib.pyplot as plt

# sns.set_theme(style="whitegrid")

# cd = "StudyFile/Data/20_engine01_timestamp_sample_67_260831.csv"

# df = pd.read_csv(cd)

# df["timestamp"] = pd.to_datetime(df["timestamp"])

# df = df.set_index("timestamp").sort_index()

# print(type(df.index).__name__)
# print(df.index[0], df.index[-1])
# print("전체 행 :", len(df))



# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import matplotlib.pyplot as plt

# sns.set_theme(style="whitegrid")

# cd = "StudyFile/Data/20_engine01_timestamp_sample_67_260831.csv"

# df = pd.read_csv(cd)

# df["timestamp"] = pd.to_datetime(df["timestamp"])

# df = df.set_index("timestamp").sort_index()

# day = df.loc["2024-03-02"]
# print(len(day))
# span = df.loc["2024-03-05" : "2024-03-07"]
# print(len(span))




# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import matplotlib.pyplot as plt

# sns.set_theme(style="whitegrid")

# cd = "StudyFile/Data/20_engine01_timestamp_sample_67_260831.csv"

# df = pd.read_csv(cd)

# df["timestamp"] = pd.to_datetime(df["timestamp"])

# df = df.set_index("timestamp").sort_index()

# print(df["temp_core"].resample("D").mean().head(3))
# print(df["temp_core"].resample("D").max().head(1))




# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import matplotlib.pyplot as plt

# sns.set_theme(style="whitegrid")

# cd = "StudyFile/Data/20_engine01_timestamp_sample_67_260831.csv"

# df = pd.read_csv(cd)

# df["timestamp"] = pd.to_datetime(df["timestamp"])

# df = df.set_index("timestamp").sort_index()

# six_hour_mean = df['temp_out'].resample('6h').mean()
# print(six_hour_mean.head(2))

# six_hour_max = df['temp_out'].resample('6h').max()
# print(six_hour_max.iloc[0])




# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import matplotlib.pyplot as plt

# sns.set_theme(style="whitegrid")

# cd = "StudyFile/Data/20_engine01_timestamp_sample_67_260831.csv"

# df = pd.read_csv(cd)

# df["timestamp"] = pd.to_datetime(df["timestamp"])

# df = df.set_index("timestamp").sort_index()

# freqs = ["h", "6h", "12h"]
# for c in freqs :
#     print(f"{c} 단위 행 : {len(df["temp_out"].resample(c).mean())}")




# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import matplotlib.pyplot as plt

# sns.set_theme(style="whitegrid")

# cd = "StudyFile/Data/20_engine01_timestamp_sample_67_260831.csv"

# df = pd.read_csv(cd)

# df["timestamp"] = pd.to_datetime(df["timestamp"])

# df = df.set_index("timestamp").sort_index()

# print(df["temp_core"].asfreq("D").head(3))
# print(df["temp_core"].resample("D").mean().head(3))



# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import matplotlib.pyplot as plt

# sns.set_theme(style="whitegrid")

# cd = "StudyFile/Data/20_engine01_timestamp_sample_67_260831.csv"

# df = pd.read_csv(cd)

# df["timestamp"] = pd.to_datetime(df["timestamp"])

# df = df.set_index("timestamp").sort_index()

# up = df["temp_core"].resample("30min").mean()

# print(up.isna().sum())

# up_filled = up.interpolate()   

# print(up_filled.isna().sum())



# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import matplotlib.pyplot as plt

# sns.set_theme(style="whitegrid")

# cd = "StudyFile/Data/20_engine01_timestamp_sample_67_260831.csv"

# df = pd.read_csv(cd)

# df["timestamp"] = pd.to_datetime(df["timestamp"])

# df = df.set_index("timestamp").sort_index()

# up = df["flow"].resample("30min").mean()
# vi = df["vibration"].resample("2h").mean()

# print(f"업샘플링 결측 : {up.isna().sum()} / 보간 후 : {up.interpolate().isna().sum()}")
# print(f"진동 원본 결측 : {vi.isna().sum()} / 진동 보간 후 : {vi.interpolate().isna().sum()}")




# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import matplotlib.pyplot as plt

# sns.set_theme(style="whitegrid")

# cd = "StudyFile/Data/20_engine01_timestamp_sample_67_260831.csv"

# df = pd.read_csv(cd)

# df["timestamp"] = pd.to_datetime(df["timestamp"])

# df = df.set_index("timestamp").sort_index()

# daily = df["temp_out"].resample("D").mean()
# plt.plot(df["temp_out"], alpha = 0.4)
# plt.plot(daily, linewidth = 2)
# plt.legend()
# plt.show()

# print(round(daily.iloc[0], 2), round(daily.iloc[-1], 2))




# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import matplotlib.pyplot as plt

# sns.set_theme(style="whitegrid")

# cd = "StudyFile/Data/20_cmapss_fd001_sample_65_260831.csv"

# df = pd.read_csv(cd)

# e1 = df[df['unit_nr'] == 1].sort_values('time_cycles')

# e1['ma5'] = e1['s_4'].rolling(window=5).mean()
# e1['std5'] = e1['s_4'].rolling(window=5).std()

# print(e1[['ma5', 'std5']].round(3).head())



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

cd = "StudyFile/Data/20_cmapss_fd001_sample_65_260831.csv"

df = pd.read_csv(cd)

e2 = df[df['unit_nr'] == 2].sort_values('time_cycles')

e2["ma5"] = e2["s_11"].rolling(window = 5).mean()
e2["std5"] = e2["s_11"].rolling(window = 5).std()

print(e2[["std5"]].iloc[4].round(3).head().tolist())

plt.plot(e2["s_11"], label = "s_11",linewidth = 0.5)
plt.plot(e2["ma5"], label = "ma5", linewidth = 2)
plt.legend()
plt.show()