# integer_Variable = int("문자") # 숫자형태 문자가 아님 : ValueError
# Value = 10 / 0  # 제로디비전 오류 : ZeroDivisionError
# print(네이밍 오류) # 인자 매칭 오류 : NameError

# 1. int 정수 형태 자료형 변환 시 string 형태 "숫자" 형태만 변환 가능
# 2. 10을 0으로 나누는 연산은 정의되지 않음 -> 0으로 나누는짓은 하지 않는다
# 3. 문자를 출력 시 따옴표로 감싸 string형태 자료형을 알려야함

# ====================================================================================
# ====================================================================================


# def inputvalue():

#     try:
#         value = float(input("온도를 입력하세요 :"))

#         print(
#             f"{"=" * 30} \n 현재 온도는 {value}도 입니다 \n 프로그램 종료. \n{"=" * 30}"
#         )
#     except ValueError:
#         print("숫자만 입력하세요")
#         inputvalue()
#     except NameError:
#         print("숫자를 입력 하세요")
#         inputvalue()
#     except Exception:
#         print("알 수 없는 오류가 발생했습니다 \n 프로그램을 종료합니다.")


# inputvalue()

# ====================================================================================
# ====================================================================================


# import os
# import csv

# Sample_file_location = "StudyFile/Data/09_ict_inspection.csv"
# Sample_file_location_update = "StudyFile/Data/09_ict_inspection_update.csv"
# count = 0
# try:
#     f = open(Sample_file_location, "r", encoding="utf-8")
#     n = open(Sample_file_location_update, "w", encoding="utf-8")

# except FileNotFoundError:
#     print("파일이 존재하지 않습니다.")
# else:
#     f.seek(0)

#     reader = csv.reader(f)
#     writer = csv.writer(n)

#     header = next(reader)
#     writer.writerow(header)

#     for row in reader:
#         if len(row) <= 2 or row[2].strip() == "":
#             continue

#         measurement = float(row[2])

#         if measurement != 0:
#             writer.writerow(row)
#         count += 1
# finally:
#     print(f"검사한 횟수: {count}")
#     print("종료")
#     f.close()
#     n.close()

# ====================================================================================
# ====================================================================================
# Sample_file_location = "StudyFile/Data/09_ict_inspection.csv"

# with open(Sample_file_location, "r", encoding="utf-8") as f:
#     rows = f.readlines()
# total = 0.0
# skipped = 0
# for line in rows[1:]:  # 헤더 제외
#     cols = line.strip().split(",")
#     try:
#         total += float(cols[2])  # 측정값(2열)
#     except (ValueError, IndexError):
#         skipped += 1
#     continue  # 불량 줄은 건너뜀
# print("합계:", round(total, 1), "건너뜀:", skipped)


