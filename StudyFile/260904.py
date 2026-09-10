# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import koreanfont as kf

# kf.set_korean_font()

# data_file = "StudyFile/Data/01-02_원료_전처리와_제선_제선조업_223_260904_Question_2.csv"

# df = pd.read_csv(data_file)

# sensor_cols = [col for col in df.columns if col.startswith("s_")]
# sensor_cols = [col for col in sensor_cols if df[col].std() > 1e-8]

# baseline = df[df["time_cycles"] <= 100]
# baseline_mean = baseline[sensor_cols].mean()
# baseline_std = baseline[sensor_cols].std()

# for sensor in sensor_cols:
#     df[f"z_{sensor}"] = (df[sensor] - baseline_mean[sensor]) / baseline_std[sensor]

# sensor = "s_12"
# z_sensor = f"z_{sensor}"

# unit_df = df[df["unit_nr"] == 1]
# plt.figure(figsize=(12, 5))
# plt.plot(unit_df["time_cycles"], unit_df[z_sensor], label=f"{sensor} Z-score", color="blue")

# plt.axhline(0, color="black", linestyle="--", label="Average")
# plt.axhline(3, color="red", linestyle="--", label="+3 threshold")
# plt.axhline(-3, color="red", linestyle="--", label="-3 threshold")

# plt.title(f"Unit 1 - {sensor} Z-score Over Time")
# plt.xlabel("Time Cycles")
# plt.ylabel("Z-score")
# plt.legend()
# plt.grid(True, alpha=0.3)
# plt.tight_layout()
# plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanfont as kf

kf.set_korean_font()

data_file = "StudyFile/Data/01-02_원료_전처리와_제선_제선조업_223_260904_Question_2.csv"

df = pd.read_csv(data_file)
df["timestamp"] = pd.to_datetime(df["timestamp"])

#timestamp,
# blast_flow_nm3min, 송풍량
# blast_pressure_kpa, 송풍압력
# top_pressure_kpa, 상부압력
# hot_blast_temp_c, 열풍온도
# blower_vib_mms 송풍기 진동

sensors = ["blast_flow_nm3min", "blast_pressure_kpa", "top_pressure_kpa",
           "hot_blast_temp_c", "blower_vib_mms"]

corr = df[sensors].corr()

plt.figure(figsize=(7, 6))
plt.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)

plt.xticks(range(len(sensors)), sensors, rotation=45, ha="right")
plt.yticks(range(len(sensors)), sensors)

for i in range(len(sensors)):
    for j in range(len(sensors)):
        plt.text(j, i, f"{corr.iloc[i, j]:.2f}", ha="center", va="center")

plt.title("제선 센서 상관행렬")
plt.colorbar(label="상관계수")
plt.tight_layout()
plt.show()

fig, axes = plt.subplots(len(sensors), 1, figsize=(13, 10), sharex=True)

for ax, col in zip(axes, sensors):
    ax.plot(df["timestamp"], df[col], lw=0.8)
    ax.set_ylabel(col, fontsize=9)
    ax.grid(alpha=0.3)

axes[-1].set_xlabel("시간")
fig.suptitle("시간에 따른 제선 센서값 변화")
plt.tight_layout()
plt.show()

before = df[df["timestamp"].dt.hour < 13]
after = df[df["timestamp"].dt.hour >= 13]

compare = pd.DataFrame({
    "전반(06~13시)": before[sensors].mean(),
    "후반(13시~)": after[sensors].mean(),
})
compare["차이"] = compare["후반(13시~)"] - compare["전반(06~13시)"]
compare["변화율%"] = compare["차이"] / compare["전반(06~13시)"] * 100

plt.figure(figsize=(8, 4))
plt.bar(sensors, compare["변화율%"], color="teal")
plt.axhline(0, color="black", lw=0.8)
plt.ylabel("변화율 %")
plt.title("전반(06~13시) 대비 후반(13시~) 평균 변화율")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

