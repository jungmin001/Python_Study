import csv
import numpy as np

file_location = "StudyFile/Data/10_mct_tool.csv"

# ===========================================================
# ========================| 실습 1 |==========================
# ===========================================================

# new_data = []

# with open(file_location, "r", encoding="utf-8") as f:
#     reader = csv.reader(f)
#     next(reader)

#     for i in reader:
#         if len(new_data) < 12:
#             new_data.append(i[1])
#         else:
#             continue

#     new_data_1 = np.array(new_data)
#     print(new_data_1.reshape(3, 4))
#     print(new_data_1.flatten())

# ===========================================================
# ========================| 실습 2 |==========================
# ===========================================================

# body = []

# with open(file_location, "r", encoding="utf-8") as f:
#     reader = csv.reader(f)
#     header = next(reader)

#     for row in reader:
#         body.append(row)

# body = np.array(body)

# rpm = body[:10, 4].astype(int)

# print("맨 앞:", rpm[0])
# print("맨 뒤:", rpm[-1])
# print(rpm[1:4])
# print(rpm[::2])

# ===========================================================
# ========================| 실습 3 |==========================
# ===========================================================

answer = []
list_scores = [61, 78, 59, 20, 83]
# arr_scores = np.array(list_scores)
# print(arr_scores >= 60)

# for i in list_scores:
#     answer.append(i >= 60)

# print(answer)
