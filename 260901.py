# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import matplotlib.pyplot as plt

# sns.set_theme(style="whitegrid")

# file_location = "StudyFile/Data/20_cmapss_fd001_sample_65_260831.csv"
# file_location2 = "StudyFile/Data/21_cmapss_fd001_sample_70_260901_2.csv"
# file_location3 = "StudyFile/Data/21_engine1_timestamp_sample_70_260901_3.csv"

# df = pd.read_csv(file_location)

# e1 = df[df['unit_nr'] == 1].sort_values('time_cycles')

# e1["s_4_diff"] = e1["s_4"].diff()

# print(e1["s_4_diff"].round(2).head().tolist)
# print("최대 변화량 :", round(e1["s_4_diff"].abs().max(), 2))



# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import matplotlib.pyplot as plt

# sns.set_theme(style="whitegrid")

# file_location = "StudyFile/Data/20_cmapss_fd001_sample_65_260831.csv"
# file_location2 = "StudyFile/Data/21_cmapss_fd001_sample_70_260901_2.csv"
# file_location3 = "StudyFile/Data/21_engine1_timestamp_sample_70_260901_3.csv"

# df = pd.read_csv(file_location)

# e1 = df[df['unit_nr'] == 1].sort_values('time_cycles')

# e1 = e1.sort_values("time_cycles")
# e1 = e1.reset_index(drop = True)

# e1["s_4_diff"] = e1["s_4"].diff()
# e1["s_4_rate"] = e1["s_4"].pct_change()*100

# result = e1[["time_cycles", "s_4", "s_4_diff", "s_4_rate"]].head()

# print(result)




# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import matplotlib.pyplot as plt

# sns.set_theme(style="whitegrid")

# file_location = "StudyFile/Data/20_cmapss_fd001_sample_65_260831.csv"
# file_location2 = "StudyFile/Data/21_cmapss_fd001_sample_70_260901_2.csv"
# file_location3 = "StudyFile/Data/21_engine1_timestamp_sample_70_260901_3.csv"

# df = pd.read_csv(file_location)

# e2 = df[df['unit_nr'] == 2].sort_values('time_cycles')

# e2['diff'] = e2['s_12'].diff()
# print(e2['diff'].head(4).round(2).tolist())
# idx = e2['diff'].abs().idxmax()
# print('최대 변화량:', round(e2['diff'].abs().max(), 2),
# '/ cycle:', int(e2['time_cycles'].iloc[idx]))
# print('변화율 평균(%):', round(e2['s_12'].pct_change().mean() * 100, 4))



# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import matplotlib.pyplot as plt

# sns.set_theme(style="whitegrid")

# file_location = "StudyFile/Data/20_cmapss_fd001_sample_65_260831.csv"
# file_location2 = "StudyFile/Data/21_cmapss_fd001_sample_70_260901_2.csv"
# file_location3 = "StudyFile/Data/21_engine1_timestamp_sample_70_260901_3.csv"

# df = pd.read_csv(file_location)

# e2 = df[df['unit_nr'] == 2].sort_values('time_cycles')

# sensors = ["s_2", "s_3", "s_4", "s_7", "s_11"]

# corr = df[sensors].corr()

# result = corr.round(2)
# print(result)

# print("s_4 - s_7:", round(corr.loc["s_4", "s_7"], 2))
# print("s_4 - s_11", round(corr.loc["s_4", "s_11"], 2))



# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import matplotlib.pyplot as plt

# sns.set_theme(style="whitegrid")

# file_location = "StudyFile/Data/20_cmapss_fd001_sample_65_260831.csv"
# file_location2 = "StudyFile/Data/21_cmapss_fd001_sample_70_260901_2.csv"
# file_location3 = "StudyFile/Data/21_engine1_timestamp_sample_70_260901_3.csv"

# df = pd.read_csv(file_location)

# e2 = df[df['unit_nr'] == 2].sort_values('time_cycles')

# cand = [f"s_[i]" for i in range(1, 22)]

# sensors = [c for c in cand if df[c].std() > 0.01]
# corr = df[sensors].corr()
# print(corr["s_11"].drop("s_11").sort_values(ascending = False).head(3).round(3))
# print(corr["s_11"].sort_values().head(3).round(3))



# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.set_theme(style="whitegrid")

# file_location = "StudyFile/Data/20_cmapss_fd001_sample_65_260831.csv"
# file_location2 = "StudyFile/Data/21_cmapss_fd001_sample_70_260901_2.csv"
# file_location3 = "StudyFile/Data/21_engine1_timestamp_sample_70_260901_3.csv"

# df = pd.read_csv(file_location2)

# sensors = ["s_2", "s_3", "s_4", "s_7", "s_11"]
# corr = df[sensors].corr()
# plt.figure(figsize=(10,8))
# sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', center=0)
# plt.title('Sensor Correlation'); 
# plt.tight_layout()
# plt.show()




# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.set_theme(style="whitegrid")

# file_location = "StudyFile/Data/20_cmapss_fd001_sample_65_260831.csv"
# file_location2 = "StudyFile/Data/21_cmapss_fd001_sample_70_260901_2.csv"
# file_location3 = "StudyFile/Data/21_engine1_timestamp_sample_70_260901_3.csv"

# df = pd.read_csv(file_location)

# e2 = df[df['unit_nr'] == 2].sort_values('time_cycles')

# for col in ['s_11', 's_12', 's_3']:
#     ma = e2[col].rolling(5).mean()
#     tr = '상승' if ma.dropna().iloc[-1] > ma.dropna().iloc[0] else '하강'
#     s = e2[col].rolling(5).std(); h = len(e2) // 2
#     vol = '증가' if s.iloc[h:].mean() > s.iloc[:h].mean() else '감소'
#     print(col, '추세', tr, '변동성', vol)



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

file_location = "StudyFile/Data/20_cmapss_fd001_sample_65_260831.csv"
file_location2 = "StudyFile/Data/21_cmapss_fd001_sample_70_260901_2.csv"
file_location3 = "StudyFile/Data/21_engine1_timestamp_sample_70_260901_3.csv"

df = pd.read_csv(file_location)

e2 = df[df['unit_nr'] == 2].sort_values('time_cycles')

report_df = e2.copy()

report_df["std5"] = report_df["s_11"].rolling(5).std()

threshold = report_df["std5"].mean() + report_df["std5"].std()

suspect = report_df[report_df["std5"] > threshold]

print(f"의심 cycle 개수: {len(suspect)}")
print(f"cycle 범위: {suspect["time_cycles"].min()} ~ {suspect["time_cycles"].max()}")
print(
    f"엔진번호 2 || 전체 cycle수 {len(report_df)} || "
    f"의심개수 {len(suspect)} || "
    f"권장 행동: 점검 {'필요' if len(suspect) > suspect["time_cycles"].min() & len(suspect) < suspect["time_cycles"].max() else '불필요'}"
)
