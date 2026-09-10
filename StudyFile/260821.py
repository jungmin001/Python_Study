# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import koreanfont as ks

# sns.set_theme(style="whitegrid")
# ks.set_korean_font()

# df = pd.read_csv("Data/18_equipment_sensor_61_260821.csv", encoding="utf-8-sig")

# sns.histplot(data=df, x="전류")

# plt.title("전류 분포")
# plt.xlabel("전류(A)")
# plt.ylabel("개수")

# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import koreanfont as ks

# sns.set_theme(style="whitegrid")
# ks.set_korean_font()

# df = pd.read_csv("Data/18_equipment_sensor_61_260821.csv", encoding="utf-8-sig")

# sns.histplot(data=df, x="온도", bins=20, kde=True)
# plt.title("온도 분포 (곡선 포함)")
# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import koreanfont as ks

# sns.set_theme(style="whitegrid")
# ks.set_korean_font()

# df = pd.read_csv("Data/18_equipment_sensor_61_260821.csv", encoding="utf-8-sig")

# for b in [10, 20, 40]:
#     sns.histplot(
#         data=df,
#         x="전류",
#         bins=b,
#         kde=True
#     )

# plt.title(f"전류 분포 bins={b}")
# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import koreanfont as ks

# sns.set_theme(style="whitegrid")
# ks.set_korean_font()

# df = pd.read_csv("Data/18_equipment_sensor_61_260821.csv", encoding="utf-8-sig")

# sns.histplot(data=df, x="진동", hue="판정", kde=1)
# plt.title("판정별 진동 분포")
# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import koreanfont as ks

# sns.set_theme(style="whitegrid")
# ks.set_korean_font()

# df = pd.read_csv("Data/18_equipment_sensor_61_260821.csv", encoding="utf-8-sig")

# for col, unit in [("온도", "C"), ("진동", "mm/s"), ("전류", "A")]:
#     sns.histplot(
#         data=df,
#         x=col,
#         bins=20,
#         kde=True
#     )

#     plt.title(f"{col} 분포")
#     plt.xlabel(f"{col}({unit})")
#     plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import koreanfont as ks

# sns.set_theme(style="whitegrid")
# ks.set_korean_font()

# df = pd.read_csv("Data/18_equipment_sensor_61_260821.csv", encoding="utf-8-sig")

# sns.boxplot(data=df, y="전류")
# plt.title("전류 박스플롯")
# plt.ylabel("전류(A)")
# plt.show()



# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import koreanfont as ks

# sns.set_theme(style="whitegrid")
# ks.set_korean_font()

# df = pd.read_csv("Data/18_equipment_sensor_61_260821.csv", encoding="utf-8-sig")

# sns.boxplot(data=df, x="설비라인", y="진동", hue="판정")
# plt.title("라인별 진동 분포")
# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import koreanfont as ks

# sns.set_theme(style="whitegrid")
# ks.set_korean_font()

# df = pd.read_csv("Data/18_equipment_sensor_61_260821.csv", encoding="utf-8-sig")

# sns.boxplot(data=df, x="설비라인", y="온도")
# plt.title("라인별 온도 분포")
# plt.show()

# sns.boxplot(data=df, x="설비라인", y="온도", hue="판정")
# plt.title("라인별 판정별 온도 비교")
# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import koreanfont as ks

# sns.set_theme(style="whitegrid")
# ks.set_korean_font()

# df = pd.read_csv("Data/18_equipment_sensor_61_260821.csv", encoding="utf-8-sig")

# sns.countplot(data=df, x="설비라인", hue="판정")
# plt.title("라인별 데이터 개수")
# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import koreanfont as ks

# sns.set_theme(style="whitegrid")
# ks.set_korean_font()

# df = pd.read_csv("Data/18_equipment_sensor_61_260821.csv", encoding="utf-8-sig")

# sns.countplot(data=df, x="설비라인", hue="설비라인", palette="Set2", legend=False)
# plt.title("라인별 데이터 개수")
# plt.show()

# sns.barplot(data=df, x="설비라인", y="전류", hue="설비라인", palette="pastel", legend=False)
# plt.title("라인별 평균 전류")
# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import koreanfont as ks

# sns.set_theme(style="whitegrid")
# ks.set_korean_font()

# df = pd.read_csv("Data/18_equipment_sensor_61_260821.csv", encoding="utf-8-sig")

# sns.countplot(data=df, x="설비라인", hue="판정")
# plt.title("라인별 양품·불량 개수")
# plt.show()

# 표 = df.groupby(["설비라인", "판정"], observed=True).size().unstack(fill_value=0)

# print(표)

# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import koreanfont as ks

# sns.set_theme(style="whitegrid")
# ks.set_korean_font()

# df = pd.read_csv("Data/18_equipment_sensor_61_260821.csv", encoding="utf-8-sig")

# sns.scatterplot(data=df, x="온도", y="진동")
# plt.title("온도와 진동의 관계")
# plt.show()



# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import koreanfont as ks

# sns.set_theme(style="whitegrid")
# ks.set_korean_font()

# df = pd.read_csv("Data/18_equipment_sensor_61_260821.csv", encoding="utf-8-sig")

# sns.scatterplot(data=df, x="온도", y="압력", alpha=0.5)
# plt.title("온도와 압력의 관계")
# plt.xlabel("온도(°C)")
# plt.ylabel("압력")
# plt.show()




# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import koreanfont as ks

# sns.set_theme(style="whitegrid")
# ks.set_korean_font()

# df = pd.read_csv("Data/18_equipment_sensor_61_260821.csv", encoding="utf-8-sig")

# sns.scatterplot(data=df, x="온도", y="전류", hue="판정")
# plt.title("판정별 온도-전류 관계")
# plt.xlabel("온도(C)")
# plt.ylabel("전류(A)")
# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import koreanfont as ks

# sns.set_theme(style="whitegrid")
# ks.set_korean_font()

# df = pd.read_csv("Data/18_equipment_sensor_61_260821.csv", encoding="utf-8-sig")

# corr = df.corr(numeric_only=True)
# plt.figure(figsize=(8, 6))

# sns.heatmap(
#     corr,
#     annot=True,
#     fmt=".2f",
#     cmap="coolwarm",
#     center=0
# )

# plt.title("센서 상관관계")
# plt.show()

# print(corr.loc["온도", "전류"])
# print(corr.loc["온도", "진동"])
# print(corr.loc["온도", "압력"])

# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import koreanfont as ks

# sns.set_theme(style="whitegrid")
# ks.set_korean_font()

# df = pd.read_csv("Data/18_equipment_sensor_61_260821.csv", encoding="utf-8-sig")

# fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# sns.countplot(data=df, x="설비라인", ax=axes[0])
# axes[0].set_title("라인별 데이터 개수")
# sns.histplot(data=df, x="온도", bins=20, kde=True, ax=axes[1])
# axes[1].set_title("온도 분포")
# sns.boxplot(data=df, y="진동", ax=axes[2])
# axes[2].set_title("진동 박스플롯")
# plt.tight_layout()
# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import koreanfont as ks

# sns.set_theme(style="whitegrid")
# ks.set_korean_font()

# df = pd.read_csv("Data/18_equipment_sensor_61_260821.csv", encoding="utf-8-sig")

# fig, axes = plt.subplots(1, 2, figsize=(14, 5))
# sns.scatterplot(data=df, x="온도", y="전류", hue="판정", ax=axes[0])
# axes[0].set_title("판정별 온도-전류 관계")
# corr = df.corr(numeric_only=True)
# sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", center=0, ax=axes[1])
# axes[1].set_title("센서 상관관계")
# plt.tight_layout()
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import koreanfont as ks

sns.set_theme(style="whitegrid")
ks.set_korean_font()

df = pd.read_csv("Data/18_equipment_sensor_61_260821.csv", encoding="utf-8-sig")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

sns.histplot(data=df, x="온도", bins=20, kde=True, ax=axes[0, 0])
axes[0, 0].set_title("온도 분포")

sns.boxplot(data=df, x="설비라인", y="진동", ax=axes[0, 1])
axes[0, 1].set_title("라인별 진동 분포")

sns.scatterplot(data=df, x="온도", y="전류", hue="판정", ax=axes[1, 0])
axes[1, 0].set_title("판정별 온도-전류 관계")

corr = df.corr(numeric_only=True)

sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", center=0, ax=axes[1, 1])
axes[1, 1].set_title("센서 상관관계")

plt.tight_layout()

plt.savefig("시각화_리포트.png", dpi=150, bbox_inches="tight")

plt.show()