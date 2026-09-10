# import pandas as pd
# import matplotlib.pyplot as plt
# import platform

# # Korean Input Settings
# if platform.system() == "Windows":
#     plt.rcParams["font.family"] = "Malgun Gothic"
#     print("LogTemp.Warning : Korean input is available (Windows)")
# elif platform.system() == "Darwin":
#     plt.rcParams["font.family"] = "AppleGothic"
#     print("LogTemp.Warning : Korean input is available (Mac)")
# else:
#     print("LogTemp.Error : Unable to enter Korean")

# plt.rcParams["axes.unicode_minus"] = False

# # X axis
# Day = [1, 2, 3, 4, 5]

# # Y axis
# Past_Temperature = [58, 60, 63, 61, 16]
# Current_Temperature = [52, 30, 43, 31, 66]

# plt.plot(Day, Past_Temperature, color="black", linestyle=":", marker="x")
# plt.plot(Day, Current_Temperature, color="red", linestyle="-", marker="s")
# plt.legend()
# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt
# import platform

# # Korean Input Settings
# if platform.system() == "Windows":
#     plt.rcParams["font.family"] = "Malgun Gothic"
#     print("LogTemp.Warning : Korean input is available (Windows)")
# elif platform.system() == "Darwin":
#     plt.rcParams["font.family"] = "AppleGothic"
#     print("LogTemp.Warning : Korean input is available (Mac)")
# else:
#     print("LogTemp.Error : Unable to enter Korean")

# plt.rcParams["axes.unicode_minus"] = False

# df = pd.read_csv("Data/설비센서_샘플.csv")

# A = df[df["설비명"] == "A호기"]

# plt.plot(
#     A["일자"],
#     A["온도"],
#     color="red",
#     linestyle="--",
#     marker="o",
#     label="설비센서 샘플",
# )

# plt.title("설비 센서 온도 변화")
# plt.xlabel("일자")
# plt.ylabel("온\n도", rotation = 0, labelpad=10)

# plt.legend()
# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt
# import platform

# # Korean Input Settings
# if platform.system() == "Windows":
#     plt.rcParams["font.family"] = "Malgun Gothic"
#     print("LogTemp.Warning : Korean input is available (Windows)")
# elif platform.system() == "Darwin":
#     plt.rcParams["font.family"] = "AppleGothic"
#     print("LogTemp.Warning : Korean input is available (Mac)")
# else:
#     print("LogTemp.Error : Unable to enter Korean")

# plt.rcParams["axes.unicode_minus"] = False

# df = pd.read_csv("Data/설비센서_샘플.csv")

# A = df[df["설비명"] == "A호기"]
# C = df[df["설비명"] == "C호기"]

# plt.figure(figsize=(10, 4))

# plt.plot(
#     A["일자"],
#     A["온도"],
#     color="blue",
#     linestyle="--",
#     linewidth=1,
#     marker="o",
#     label="A호기 설비센서 샘플",
# )
# plt.plot(
#     C["일자"],
#     C["온도"],
#     color="red",
#     linestyle=":",
#     linewidth=1,
#     marker="s",
#     label="C호기 설비센서 샘플",
# )

# plt.grid(True, alpha=0.3)
# plt.title("A호기 vs C호기 온도 변화")
# plt.xlabel("일자")
# plt.ylabel("온\n도", rotation = 0, labelpad=10)
# plt.xticks(
#     [1, 2, 3, 4, 5, 6, 7],
#     ["월", "화", "수", "목", "금", "토", "일"]
# )

# plt.legend(loc = 'upper left')
# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt
# import platform

# # Korean Input Settings
# if platform.system() == "Windows":
#     plt.rcParams["font.family"] = "Malgun Gothic"
#     print("LogTemp.Warning : Korean input is available (Windows)")
# elif platform.system() == "Darwin":
#     plt.rcParams["font.family"] = "AppleGothic"
#     print("LogTemp.Warning : Korean input is available (Mac)")
# else:
#     print("LogTemp.Error : Unable to enter Korean")

# plt.rcParams["axes.unicode_minus"] = False

# df = pd.read_csv("Data/설비센서_샘플.csv")

# plt.figure(figsize=(10, 4))

# for Name, Color in [("A호기", "red"), ("B호기", "blue"), ("C호기", "green")]:
#     Machine = df[df["설비명"] == Name]
#     plt.plot(Machine["일자"], Machine["온도"], linewidth=1, label=Name +"데이터 샘플", color=Color)

# plt.grid(True, alpha=0.3)
# plt.title("A호기 vs C호기 온도 변화")
# plt.xlabel("일자")
# plt.ylabel("온\n도", rotation = 0, labelpad=10)
# plt.xticks(
#     [1, 2, 3, 4, 5, 6, 7],
#     ["월", "화", "수", "목", "금", "토", "일"]
# )

# plt.legend(loc = 'upper left')
# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt
# import platform

# # Korean Input Settings
# if platform.system() == "Windows":
#     plt.rcParams["font.family"] = "Malgun Gothic"
#     print("LogTemp.Warning : Korean input is available (Windows)")
# elif platform.system() == "Darwin":
#     plt.rcParams["font.family"] = "AppleGothic"
#     print("LogTemp.Warning : Korean input is available (Mac)")
# else:
#     print("LogTemp.Error : Unable to enter Korean")

# plt.rcParams["axes.unicode_minus"] = False

# df = pd.read_csv("Data/설비센서_샘플.csv")

# plt.figure(figsize=(10, 4))

# C = df[df["설비명"] == "C호기"]

# for Category in ["온도", "진동", "소음"]:

#     if Category == "진동":
#         plt.plot(
#             C["일자"],
#             C[Category] * 20,
#             label=Category,
#             linewidth=1,
#             linestyle="-",
#             marker="s"
#         )

#     elif Category == "온도":
#         plt.plot(
#             C["일자"],
#             C[Category],
#             label=Category,
#             linewidth=1,
#             linestyle="-",
#             marker="o"
#         )

#     else:
#         plt.plot(
#             C["일자"],
#             C[Category],
#             label=Category,
#             linewidth=1,
#             linestyle="-",
#             marker="^"
#         )

# plt.legend()
# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt
# import platform

# # Korean Input Settings
# if platform.system() == "Windows":
#     plt.rcParams["font.family"] = "Malgun Gothic"
#     print("LogTemp.Warning : Korean input is available (Windows)")
# elif platform.system() == "Darwin":
#     plt.rcParams["font.family"] = "AppleGothic"
#     print("LogTemp.Warning : Korean input is available (Mac)")
# else:
#     print("LogTemp.Error : Unable to enter Korean")

# plt.rcParams["axes.unicode_minus"] = False

# plt.bar(["1호기", "2호기", "3호기"],
#         [64, 70, 77],
#         color=["blue", "red", "green"],
#         width=1)
# plt.barh(["1호기", "2호기", "3호기"],
#          [64, 70, 77],
#          color=["blue", "red", "green"],
#          height=1)

# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt
# import platform

# # Korean Input Settings
# if platform.system() == "Windows":
#     plt.rcParams["font.family"] = "Malgun Gothic"
#     print("LogTemp.Warning : Korean input is available (Windows)")
# elif platform.system() == "Darwin":
#     plt.rcParams["font.family"] = "AppleGothic"
#     print("LogTemp.Warning : Korean input is available (Mac)")
# else:
#     print("LogTemp.Error : Unable to enter Korean")

# plt.rcParams["axes.unicode_minus"] = False

# df = pd.read_csv("Data/설비센서_샘플.csv")

# Machine = df.groupby("설비명")["온도"].mean()

# plt.bar(Machine.index, Machine.values)
# plt.title("설비별 평균 온도")
# plt.ylabel("온\n도", rotation=0)
# plt.show()

# plt.bar(
#     Machine.index,
#     Machine.values,
#     color=["blue", "blue", "red"],
#     width=0.5
# )
# plt.title("설비별 평균 온도")
# plt.ylabel("온\n도", rotation=0)
# plt.show()

# plt.barh(
#     Machine.index,
#     Machine.values,
#     color=["blue", "blue", "red"],
#     height=0.5
# )
# plt.title("설비별 평균 온도")
# plt.ylabel("온\n도", rotation=0)
# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt
# import platform

# # Korean Input Settings
# if platform.system() == "Windows":
#     plt.rcParams["font.family"] = "Malgun Gothic"
#     print("LogTemp.Warning : Korean input is available (Windows)")
# elif platform.system() == "Darwin":
#     plt.rcParams["font.family"] = "AppleGothic"
#     print("LogTemp.Warning : Korean input is available (Mac)")
# else:
#     print("LogTemp.Error : Unable to enter Korean")

# plt.rcParams["axes.unicode_minus"] = False

# df = pd.read_csv("Data/설비센서_샘플.csv")

# Stat = df["상태"].value_counts()

# plt.bar(Stat.index, Stat.values)
# plt.show()

# plt.figure(figsize=(10, 4))

# Zone = df.groupby("구역")["진동"].mean()

# plt.bar(Zone.index, Zone.values)

# plt.title("구역별 평균 진동")
# plt.ylabel("진동\n(mm/s)", rotation=0, labelpad=20)
# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt
# import platform

# # Korean Input Settings
# if platform.system() == "Windows":
#     plt.rcParams["font.family"] = "Malgun Gothic"
#     print("LogTemp.Warning : Korean input is available (Windows)")
# elif platform.system() == "Darwin":
#     plt.rcParams["font.family"] = "AppleGothic"
#     print("LogTemp.Warning : Korean input is available (Mac)")
# else:
#     print("LogTemp.Error : Unable to enter Korean")

# plt.rcParams["axes.unicode_minus"] = False

# df = pd.read_csv("Data/설비센서_샘플.csv")

# plt.hist(df["온도"], bins=20)
# plt.xlabel("온도")
# plt.ylabel("측정 횟수")
# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt
# import platform

# # Korean Input Settings
# if platform.system() == "Windows":
#     plt.rcParams["font.family"] = "Malgun Gothic"
#     print("LogTemp.Warning : Korean input is available (Windows)")
# elif platform.system() == "Darwin":
#     plt.rcParams["font.family"] = "AppleGothic"
#     print("LogTemp.Warning : Korean input is available (Mac)")
# else:
#     print("LogTemp.Error : Unable to enter Korean")

# plt.rcParams["axes.unicode_minus"] = False

# df = pd.read_csv("Data/설비센서_샘플.csv")

# plt.hist(df["온도"], bins=5)
# plt.show()

# plt.hist(df["온도"], bins=20)
# plt.title("온도 분포")
# plt.xlabel("온 도")
# plt.ylabel("개\n수", rotation=0, labelpad=20)
# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt
# import platform

# # Korean Input Settings
# if platform.system() == "Windows":
#     plt.rcParams["font.family"] = "Malgun Gothic"
#     print("LogTemp.Warning : Korean input is available (Windows)")
# elif platform.system() == "Darwin":
#     plt.rcParams["font.family"] = "AppleGothic"
#     print("LogTemp.Warning : Korean input is available (Mac)")
# else:
#     print("LogTemp.Error : Unable to enter Korean")

# plt.rcParams["axes.unicode_minus"] = False

# df = pd.read_csv("Data/설비센서_샘플.csv")

# plt.hist(df["온도"], bins=8)

# High_temperature = df[df["온도"] >= 78]

# print("Average_temperature : ", round(df["온도"].mean(), 1))
# print("Standard_temperature : ", round(df["온도"].std(), 1))
# print(len(High_temperature))

# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt
# import platform

# # Korean Input Settings
# if platform.system() == "Windows":
#     plt.rcParams["font.family"] = "Malgun Gothic"
#     print("LogTemp.Warning : Korean input is available (Windows)")
# elif platform.system() == "Darwin":
#     plt.rcParams["font.family"] = "AppleGothic"
#     print("LogTemp.Warning : Korean input is available (Mac)")
# else:
#     print("LogTemp.Error : Unable to enter Korean")

# plt.rcParams["axes.unicode_minus"] = False

# df = pd.read_csv("Data/설비센서_샘플.csv")

# plt.scatter(df["온도"], 
#             df["진동"], 
#             color="red", 
#             s=100,
#             alpha=0.3)
# plt.xlabel("온  도")
# plt.ylabel("진\n\n동", rotation=0, labelpad=10)
# plt.show()



# import pandas as pd
# import matplotlib.pyplot as plt
# import platform

# # Korean Input Settings
# if platform.system() == "Windows":
#     plt.rcParams["font.family"] = "Malgun Gothic"
#     print("LogTemp.Warning : Korean input is available (Windows)")
# elif platform.system() == "Darwin":
#     plt.rcParams["font.family"] = "AppleGothic"
#     print("LogTemp.Warning : Korean input is available (Mac)")
# else:
#     print("LogTemp.Error : Unable to enter Korean")

# plt.rcParams["axes.unicode_minus"] = False

# df = pd.read_csv("Data/설비센서_샘플.csv")

# plt.scatter(df["온도"], 
#             df["진동"], 
#             color="red", 
#             s=100,
#             alpha=0.3)

# plt.axhline(y = 4.0, color = "red", linestyle= "--")
# plt.axvline(x = 75.0, color = "red", linestyle= "--")
# plt.xlabel("온  도")
# plt.ylabel("진\n\n동", rotation=0, labelpad=10)

# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt
# import platform

# # Korean Input Settings
# if platform.system() == "Windows":
#     plt.rcParams["font.family"] = "Malgun Gothic"
#     print("LogTemp.Warning : Korean input is available (Windows)")
# elif platform.system() == "Darwin":
#     plt.rcParams["font.family"] = "AppleGothic"
#     print("LogTemp.Warning : Korean input is available (Mac)")
# else:
#     print("LogTemp.Error : Unable to enter Korean")

# plt.rcParams["axes.unicode_minus"] = False

# df = pd.read_csv("Data/설비센서_샘플.csv")

# plt.scatter(df["온도"], df["진동"])
# plt.show()

# Color = df["상태"].map({
#     "정상": "blue",
#     "점검": "red"
# })

# plt.scatter(
#     df["온도"],
#     df["진동"],
#     color=Color,
#     s=70, 
#     alpha=0.3
# )

# plt.axhline(
#     y=4.0,
#     color="red",
#     linestyle="--",
#     linewidth=1
# )

# plt.title("온도와 진동의 관계")
# plt.xlabel("온  도")
# plt.ylabel("진\n\n동", rotation=0, labelpad=10)
# plt.show()



# import pandas as pd
# import matplotlib.pyplot as plt
# import platform

# # Korean Input Settings
# if platform.system() == "Windows":
#     plt.rcParams["font.family"] = "Malgun Gothic"
#     print("LogTemp.Warning : Korean input is available (Windows)")
# elif platform.system() == "Darwin":
#     plt.rcParams["font.family"] = "AppleGothic"
#     print("LogTemp.Warning : Korean input is available (Mac)")
# else:
#     print("LogTemp.Error : Unable to enter Korean")

# plt.rcParams["axes.unicode_minus"] = False

# df = pd.read_csv("Data/설비센서_샘플.csv")

# plt.scatter(
#     df["가동시간"],
#     df["진동"],
#     alpha=0.6
# )

# plt.title("가동시간과 진동의 관계")
# plt.xlabel("가동시간")
# plt.ylabel("진\n\n동", rotation=0, labelpad=10)
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import platform

# Korean Input Settings
if platform.system() == "Windows":
    plt.rcParams["font.family"] = "Malgun Gothic"
    print("LogTemp.Warning : Korean input is available (Windows)")
elif platform.system() == "Darwin":
    plt.rcParams["font.family"] = "AppleGothic"
    print("LogTemp.Warning : Korean input is available (Mac)")
else:
    print("LogTemp.Error : Unable to enter Korean")

plt.rcParams["axes.unicode_minus"] = False

Age = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
Study = [8, 12, 10, 15, 9, 5, 4, 4, 2, 5, 6]

plt.plot(Age, Study)
plt.show()