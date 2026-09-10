# import numpy as np
# import pandas as pd

# data_file = "StudyFile/Data/22_열처리_결측추가2_75_260903_1.csv"

# df = pd.read_csv(data_file)

# norm = df[["제어출력"]].asfreq("10s")
# filled = norm["제어출력"].ffill()

# s = pd.Series([10.0, np.nan, 40.0], index=pd.to_datetime(['2024-03-01 09:00:00', '2024-03-01 09:00:10', '2024-03-01 09:01:00']))
# print('선형:', s.interpolate(method='linear').iloc[1], '시간:', s.interpolate(method='time').iloc[1])
# lin = norm['제어출력'].interpolate()
# tim = norm['제어출력'].interpolate(method='time')
# print('다른 칸 수:', int((lin != tim).sum()))


# import numpy as np
# import pandas as pd

# data_file = "StudyFile/Data/22_열처리_결측추가2_75_260903_1.csv"

# df = pd.read_csv(data_file)

# df["timestamp"] = pd.to_datetime(df["timestamp"])

# df = df.set_index("timestamp").sort_index()

# norm = df[["제어출력"]].asfreq("10s")

# isna = norm["제어출력"].isna()
# grp = (isna != isna.shift()).cumsum()

# gap_len = isna.groupby(grp).sum()
# gap_len = sorted((int(x) for x in gap_len[gap_len > 0]), reverse=True)

# no_limit = int(norm["제어출력"].interpolate().isna().sum())
# limit_2 = int(norm["제어출력"].interpolate(limit=2).isna().sum())

# print(gap_len, "/ 제한없음", no_limit, "/ 두칸 제한", limit_2)


# import numpy as np
# import pandas as pd

# data_file = "StudyFile/Data/22_열처리_결측추가2_75_260903_1.csv"

# def preprocess(path, freq="10s"):
#     df = pd.read_csv(path)

#     df["timestamp"] = pd.to_datetime(df["timestamp"])

#     df = df.set_index("timestamp").sort_index()

#     g = df.asfreq(freq)

#     before = int(g.isna().all(axis=1).sum())

#     clean = g.ffill().bfill()

#     after = int(clean.isna().all(axis=1).sum())

#     print(f"전 {before}칸 / 후 {after}칸")

#     return clean


# preprocess(data_file)


# import numpy as np
# import pandas as pd

# data_file = "StudyFile/Data/22_열처리_결측추가2_75_260903_1.csv"

# df = pd.read_csv(data_file)

# df["timestamp"] = pd.to_datetime(df["timestamp"])

# df = df.set_index("timestamp").sort_index()

# for freq in ["10s", "30s", "1min"]:
#     n = df.asfreq(freq)
#     c = n["제어출력"].interpolate(method="time")

#     rows = len(n)
#     na_before = int(n["제어출력"].isna().sum())
#     na_after = int(c.isna().sum())

#     print(f"{freq} : {rows}행 결측{na_before} / 보간 후 {na_after}")


# import numpy as np
# import pandas as pd

# data_file = "StudyFile/Data/22_열처리_결측추가2_75_260903_1.csv"
# columns = ["10s", "30s", "1min"]

# def compare_freq(file, column):
#     df = pd.read_csv(file)
#     df["timestamp"] = pd.to_datetime(df["timestamp"])

#     df = df.set_index("timestamp").sort_index()

#     for freq in column:
#         n = df.asfreq(freq)
#         c = n["제어출력"].interpolate(method="time")

#         rows = len(n)
#         na_before = int(n["제어출력"].isna().sum())
#         na_after = int(c.isna().sum())

#         print(f"{freq} : {rows}행 결측{na_before} / 보간 후 {na_after}")


# compare_freq(data_file, columns)


# import numpy as np
# import pandas as pd

# data_file = "StudyFile/Data/22_열처리_결측추가2_75_260903_1.csv"

# df = pd.read_csv(data_file)

# df["timestamp"] = pd.to_datetime(df["timestamp"])

# df = df.set_index("timestamp").sort_index()

# clean = df.rolling(window=6, min_periods=1).mean()

# final = clean["제어출력"].iloc[-1]
# change = clean["제어출력"].iloc[-1] - clean["제어출력"].iloc[0]

# if final > 0.55 or change > 0.1:
#     status = "장비 검토 필요"
# elif change > 0.5:
#     status = "주의"
# else:
#     status = "정상"

# print(f"최종 = {final:.3f} / 변화량 = {change:.3f} : {status}")


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanfont as kf

kf.set_korean_font()

data_file = "StudyFile/Data/01-03_제강_연주와_압연_열연조업_222_260903_Question_1.csv"

df = pd.read_csv(data_file)

sensors = [
    "furnace_temp_c",
    "rolling_force_ton",
    "roll_gap_mm",
    "exit_thickness_mm",
    "coiler_tension_kn",
    "motor_current_a",
]

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 20)

coil_mean = df.groupby("coil_id")[sensors].mean()
overall = df[sensors].mean()
z = (coil_mean - overall) / coil_mean.std()

bad = z[(z.abs() >= 2).any(axis=1)]   

print("코일 평균 \n", overall.round(2).to_frame("전체평균").T)
print("\n이상코일 평균", coil_mean.loc[bad.index].round(2))

# 코일 x 센서 z-score 히트맵 (색이 진할수록 전체 평균에서 많이 벗어남)
plt.figure(figsize=(8, 12))
plt.imshow(z.values, cmap="coolwarm", vmin=-3, vmax=3, aspect="auto")

plt.xticks(range(len(sensors)), sensors, rotation=90)
plt.yticks(range(len(coil_mean)), coil_mean.index)

for i in range(z.shape[0]):
    for j in range(z.shape[1]):
        plt.text(j, i, f"{z.values[i, j]:.1f}", ha="center", va="center", fontsize=7)

plt.title("코일별 센서 z-score (전체 평균 대비)")
plt.colorbar(label="z-score")
plt.tight_layout()
plt.savefig("StudyFile/260903_히트맵.png", dpi=120)
print("\n저장: StudyFile/260903_히트맵.png")