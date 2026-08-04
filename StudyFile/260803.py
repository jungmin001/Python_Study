import os
import csv

file_location = "StudyFile/Data/08_press.csv"

# with open(file_location, "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# f = open(file_location, "r", encoding="utf-8")

# print(f.readline())
# f.seek(0)
# print(f.readline())
# f.close()

# machine_id = set()

# with open(file_location, "r", encoding="utf-8") as f:
#     for line in f:
#         list_id = line.split(",")
#         machine_id.add(list_id[0])

# print(len(machine_id), machine_id)

# textfile_location = "StudyFile/Data/TestData.txt"

# with open(textfile_location, "r", encoding="utf-8") as f:
#     print(f.read())

# with open(textfile_location, "w", encoding="utf-8") as f:
#     f.write('std::cout << "Hello World!" << std::endl;')

# with open(textfile_location, "r", encoding="utf-8") as f:
#     print(f.read())

Update_file_location = "StudyFile/Data/08_press_update.csv"

# with open(Update_file_location, "w", encoding="utf-8") as f:
#     f.write("""
#     나랏말싸미 듕귁에달아 문자와로 서로 사맛디 아니할쌔 이런 젼차로 어린 백셩이 니르고져 홀배 이르고져 할따라미니라
#     내 이랄 위하여 어엿비 너겨 새로 스믈여듧믄 글자를 맹가노니 사람마다 수비니겨 날로 쑤메 뼌한킈 하고져 할따라미니라
#     """)

# with open(Update_file_location, "r", encoding="utf-8") as f:
#     print(f.read())

# with open(Update_file_location, "a", encoding="utf-8") as f:
#     f.write(
#         "날짜, 공휴일\n26.07.27, True\n26.07.28, True\n26.07.29, True\n26.07.30, True\n26.07.31, True\n26.08.01, False\n26.08.02, False\n26.08.03, True"
#     )
# with open(Update_file_location, "r", encoding="utf-8") as f:
#     print(f.read())

new_set = set()

# with open(Update_file_location, "r", encoding="utf-8") as f:
#     reader = csv.reader(f)
#     next(reader)
#     for row in reader:
#         new_set.add(row[0])
# new_set = sorted(new_set)
# print(new_set)

# with open(file_location, "a", encoding="utf-8", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(
#         ["PRESS-13", "2022-07-17 10:53:53.540", "-0.0489", "-0.0071", "195.5033", "1"]
#     )

# with open(file_location, "r", encoding="utf-8") as f:
#     print(f.read())

# new_file = "StudyFile/Data/08_press_new2.csv"

# with open(new_file, "w", encoding="utf-8", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["설비ID", "상태"])
#     writer.writerow(["PRESS-13", 1])
#     writer.writerow(["PRESS-14", 0])

# new_slot = []
# Category = []
# with open(Update_file_location, "r", encoding="utf-8") as f:
#     reader = csv.reader(f)
#     Category = next(reader)

#     for line in reader:
#         if line[4] <= "90":
#             current = float(line[4])
#         if current >= 90:
#             new_slot.append(line)

# with open(Update_file_location, "w", encoding="utf-8", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(Category)
#     writer.writerows(new_slot)

# import csv

# fails = []
# with open(Update_file_location, "r", encoding="utf-8") as f:
#     reader = csv.reader(f)
#     header = next(reader)
#     for row in reader:
#         if row[5] == "1":
#             fails.append(row)

# with open(Update_file_location, "w", encoding="utf-8", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(header)
#     for row in fails:
#         writer.writerow(row)
