# import pandas as pd

# df = pd.read_csv("StudyFile/Data/15_01_secom_교육샘플 - 복사본.csv")

# print(df)

# import pandas as pd

# ss = pd.read_csv("StudyFile/Data/15_01_secom_교육샘플 - 복사본.csv")

# print(ss.isna().sum())
# print((ss["압력"] == 0).sum())
# print((ss["진동"] == -999).sum())

# import pandas as pd

# df = pd.read_csv("StudyFile/Data/15_01_secom_교육샘플 - 복사본.csv")

# print(df.shape)
# print(df.head(3))
# df.info()
# df.describe()

# import pandas as pd

# data_file_location = "StudyFile/Data/15_01_secom_교육샘플 - 복사본.csv"

# df = pd.read_csv(data_file_location)

# cnt = df.isna().sum()

# ratio = (cnt / len(df) * 100).round(1)

# table = pd.DataFrame({"개수": cnt, "비율": ratio})

# result = table[table["개수"] > 0]

# print(result)

# import pandas as pd

# data_file_location = "StudyFile/Data/15_01_secom_교육샘플 - 복사본.csv"

# df = pd.read_csv(data_file_location)

# cnt = df.isna().sum()

# ratio = (cnt / len(df) * 100).round(1)

# ranking = ratio.sort_values(ascending=False)

# print(ranking.head(3))

# row_missing = df.isna().sum(axis=1)

# print((row_missing == 0).sum())
# print((row_missing >= 1).sum())

# bad_rows = df[row_missing >= 5]

# print(bad_rows.shape)

# import pandas as pd

# data_file_location = "StudyFile/Data/15_01_secom_교육샘플 - 복사본.csv"

# df = pd.read_csv(data_file_location)

# cnt = df.isna().sum()

# ratio = (cnt / len(df) * 100).round(1)

# summary = pd.DataFrame({"개수": cnt, "비율": ratio})

# summary = summary[summary["개수"] > 0].copy()


# def direction(r):
#     if r < 5:
#         return "대체"
#     if r >= 40:
#         return "제거 고민"
#     return "검토"


# summary["처리방향"] = summary["비율"].apply(direction)

# print(summary)

# summary.to_csv("결측요약.csv", encoding="utf-8-sig")

# import pandas as pd

# df = pd.read_csv("StudyFile/Data/15_01_secom_교육샘플 - 복사본.csv")

# print(df.shape)

# clean = df.dropna(axis=1)
# print(clean.shape)

# import pandas as pd

# data_file_location = "StudyFile/Data/15_01_secom_교육샘플 - 복사본.csv"

# df = pd.read_csv(data_file_location)

# print("원본 데이터 :", df.shape)

# print("결측 행 삭제 후 :", df.dropna().shape)

# print("결측 열 삭제 후 :", df.dropna(axis=1).shape)

# import pandas as pd

# data_file_location = "StudyFile/Data/15_01_secom_교육샘플 - 복사본.csv"

# df = pd.read_csv(data_file_location)

# print("원본 데이터 :", df.shape)

# print("모든 값이 결측인 행 삭제 후 :", df.dropna(how="all").shape)

# print("정상값이 20개 이상인 행만 남긴 후 :", df.dropna(thresh=20).shape)

# print("불량여부가 결측인 행 삭제 후 :", df.dropna(subset=["불량여부"]).shape)

# import pandas as pd

# data_file_location = "StudyFile/Data/15_01_secom_교육샘플 - 복사본.csv"

# df = pd.read_csv(data_file_location)

# missing_count = df.isna().sum()

# 비율 = missing_count / len(df)

# 제거 = 비율[비율 > 0.4].index.tolist()

# print(제거)

# df = df.drop(columns=제거)

# print(df.shape)


# import pandas as pd

# data_file_location = "StudyFile/Data/15_01_secom_교육샘플 - 복사본.csv"

# df = pd.read_csv(data_file_location)

# 비교 = pd.DataFrame(
#     {
#         "방식": ["원본", "행삭제", "thresh20"],
#         "행": [len(df), len(df.dropna()), len(df.dropna(thresh=20))],
#     }
# )

# 비교["손실률"] = ((1 - 비교["행"] / len(df)) * 100).round(1)

# print(비교)

import pandas as pd

data_file_location = "StudyFile/Data/15_01_secom_교육샘플 - 복사본.csv"

df = pd.read_csv(data_file_location)

평균 = df["센서17"].mean()
중앙값 = df["센서17"].median()

print(round(평균, 2))
print(round(중앙값, 2))

평균채움 = df["센서17"].fillna(평균)
중앙채움 = df["센서17"].fillna(중앙값)

print(평균채움.isna().sum())
print(중앙채움.isna().sum())
