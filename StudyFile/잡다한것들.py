# # # Number = {1, 2, 2, 3, 3, 3}
# # # print(Number)

# # # Sensor = ("모터온도", 78, "C")
# # # print(Sensor)
# # # print(Sensor[0])
# # # print(Sensor[-1])

# # # Sensor = ("모터온도", 78)
# # # print(Sensor[0])
# # # print(Sensor[1])
# # # A, B = Sensor
# # # print(A, B)

# # # Pump = [("A", 80), ("B", 90), ("C", 100)]

# # # for A, B in Pump:
# # #     print(A, B)
# # #     if B > 90:
# # #         print("경고")


# # # sensors = [("모터온도", 78, (3, 5)), ("베어링진동", 0.5, (7, 2)), ("펌프압력", 95, (4, 8)),]
# # # for name, value, pos in sensors:
# # #     x, y = pos
# # #     print(name, "위치:", x, y)
# # # for name, value, pos in sensors:
# # #     x, y = pos
# # # if x <= 5:
# # #     print(name, "1구역")

# # # line_a = {"S01", "S02", "S03"}
# # # line_b = {"S03", "S04"}
# # # all_s = line_a.union(line_b)
# # # print(all_s)

# # # line_a = {"S01", "S02", "S03"}
# # # line_b = {"S03", "S04"}
# # # common = line_a.intersection(line_b)
# # # print(common)

# # # line_a = {"S01", "S02", "S03"}
# # # line_b = {"S03", "S04"}
# # # print(line_a.difference(line_b))
# # # print(line_b.difference(line_a))

# # logs = ["S01", "S02", "S01", "S03", "S02"]
# # print(set(logs), "\n",len(set(logs)))

# # # line_a = {"S01", "S02", "S03", "S05"}
# # # line_b = {"S03", "S04", "S05"}
# # # print(f"{line_a.union(line_b)} \n {line_a.intersection(line_b)} \n {line_a.difference(line_b)} \n {line_b.difference(line_a)}")


# # error_log01 = {("S01", "정상"), ("S02", "경고"), ("S03", "경고")}
# # error_log02 = {("S01", "정상"), ("S02", "경고"), ("S03", "정상"), ("S04", "경고")}
# # error_type = {"경고", "정상"}

# # warning_log01 = {sensor_id for sensor_id, status in error_log01 if status == "경고"}
# # warning_log02 = {sensor_id for sensor_id, status in error_log02 if status == "경고"}

# # new_warnings = warning_log02 - warning_log01
# # continuing_warnings = warning_log02 & warning_log01

# # print("신규 경고:", new_warnings)
# # print("지속 경고:", continuing_warnings)

# # print("================================")

# # orders = [("A01", "연필"), ("A02", "공책"), ("A03", "연필"), ("A04", "지우개"), ("A05", "공책")]
# # items = {"연필", "공책", "지우개"}

# # ordered_items = [product for order_id, product in orders]
# # all_ordered_items = set(ordered_items)
# # repeated_items = {product for product in all_ordered_items if ordered_items.count(product) >= 2}
# # unregistered_items = all_ordered_items - items

# # print("전체 주문 상품:", all_ordered_items)
# # print("두 번 이상 주문된 상품:", repeated_items)
# # print("등록되지 않은 상품:", unregistered_items)

# # list = {"S01", "S02"}
# # list |= {"S03", "S01"}
# # print(list)

# # sensors = {"모터온도": 78, "진동": 0.5, "압력": 95}
# # print(len(sensors))
# # if len(sensors) < 5:
# #     print("센서 데이터 누락 확인 필요")

# # values = {"모터온도": 95, "압력": 88}
# # limits = {"모터온도": 90, "압력": 90}
# # for name, value in values.items():
# #     if value > limits[name]:
# #         print(name, "경고")

# # sensors = {"모터온도": 78, "진동": 0.5}
# # new_data = {"모터온도": 80, "유량": 42}
# # sensors.update(new_data)
# # print(sensors)

# # names = ["모터온도", "진동", "압력"]
# # values = [78, 0.5, 95]
# # sensors = dict(zip(names, values))
# # print(sensors)

# # sensors = {"모터온도": [78, 79, 80]}
# # temps = sensors["모터온도"]
# # print(sum(temps) / len(temps))
# # print(max(temps))

# # sensors = {"모터온도": 78, "진동": 0.5}
# # new_data = {"모터온도": 81, "압력": 95}

# # sensors.update(new_data)
# # del sensors["압력"]
# # print(f"갱신된 딕셔너리 : {sensors} \n 갱신된 딕셔너리 길이 : {len(sensors)}")

# # sensors = {"온도": 80, "진동": 55, "압력": 95}
# # print(f" 평균 : {int(sum(sensors.values()) / len(sensors))} \n  최대값 센서 : {min(sensors.items())}")

# # names = ["온도", "진동", "압력"]
# # values = [78, 0.5, 95]
# # Values = dict(zip(names, values))
# # print(Values)
# # for i in Values.items():
# #     print(i)

# # values = {"온도": 95, "진동": 0.5, "압력": 88}
# # limits = {"온도": 90, "진동": 1.0, "압력": 90}

# # for i in values.keys():
# #     if values[i] > limits[i]:
# #         print(f"{i} 경고")

# # plant = {
# # "1번모터": {"온도": 78, "상태": "정상"},
# # "2번펌프": {"압력": 95, "상태": "경고"},
# # }
# # print(plant["2번펌프"]["압력"])
# # for i, j in plant.items():
# #     if j["상태"] == "경고":
# #         print(i, "점검 필요")

# # User_Name = input("이름을 입력하세요: ")

# # def greet(name):
# #     print(f"안녕하세요 {name}님 :D")

# # greet(User_Name)

# OnDamage = input("손상 정도를 입력하세요 (1~5): ")
# Health = 100
# MaxHealth = Health

# def OnTakeDamage(Damage):
#     if Damage == 1:
#         Health -= 20
#     elif Damage == 2:
#         Health -= 40
#     elif Damage == 3:
#         Health -= 60
#     elif Damage == 4:
#         Health -= 80
#     else:
#         Health -= 100

#     print(f"{MaxHealth - Health}만큼 손상되었습니다. 현재 체력: {Health}")

# print(f"최대 체력: {MaxHealth}")
# OnTakeDamage(OnDamage)

# Name = ""

# def Input_MachineNames():
#     print("장비 목록: \n 1. 압축기A \n 2. 펌프1 \n 3. 믹서B")
#     Name = input("장비를 선택하세요 : ")

# Input_MachineNames()

# if str(Name) not in ["1", "2", "3"]:
#     print("잘못된 입력입니다. 1, 2, 3 중 하나를 선택하세요.")
#     Input_MachineNames()

# if Name == "1":
#     Name = "압축기A"
# elif Name == "2":
#     Name = "펌프1"
# elif Name == "3":
#     Name = "믹서B"

# def MachineStatus(MachineNames):
#     print(f"{MachineNames} \n 점검을 시작 합니다. \n 안정 장비를 확인하세요 \n 기록을 준비하세요")

# MachineStatus(Name)


# # def StartMachine_Log():
# #     print("=" * 20)
# #     print("점검을 시작합니다")
# #     print("=" * 20)
# #     print("기록을 준비하세요")


# # StartMachine_Log()


# def Start_Inspection():
#     print("""[점검 시작]
# 보호 장비를 확인하세요.
# 점검 기록지를 준비하세요.""")

# Start_Inspection()
# Start_Inspection()

# [제어실] 점검준비
# [제어실] 펌프 호출
# 펌프 1: 압력 완료
# 펌프 1: 기록 완료
# [제어실]다음 설비로 이동

# def check_pump_safety():
#     print("펌프 안전 점검을 시작합니다.")

# check_pump_safety()


# def show_inspection_notice():
#     print("안전모와 장갑을 착용하세요.")
#     print("점검 결과를 기록하세요")


# show_inspection_notice()
# show_inspection_notice()
# show_inspection_notice()


# def show_check_guide():
#     MachineName = ""
#     i = 1
#     while i <= 3:
#         if i == 1:
#             MachineName = "압축기 A"
#         elif i == 2:
#             MachineName = "펌프 1"
#         elif i == 3:
#             MachineName = "보일러 3"

#     print(
#         f"{MachineName} \n 점검을 시작합니다. \n 보호 장비를 확인하세요 \n 기록지를 준비하세요."
#     )
#     print()
#     i += 1


# show_check_guide()

# def print_line():
#     print("=" * 20)

# def show_safety_notice():
#     print("안전모와 장갑을 준비하세요")
#     print("기록지를 준비하세요")


# # def inspect_compressor():
# #     print_line()
# #     print("[압축기 A] 점검 시작")
# #     show_safety_notice()
# #     print_line()
# #     print("[펌프 1] 점검 시작")
# #     show_safety_notice()

# # inspect_compressor()


# # def check(name):
# #     print(name + "점검 시작")


# # check("압축기 A")


# def Test_Function(Machines):
#     print(Machines, "점검 시작")


# Test_Function("압축기 A")
# Test_Function("펌프 1")


# def start_check():
#     print("점검을 시작합니다")
#     print("안전 장비를 확인하세요")
#     print("기록을 준비하세요")


# start_check()
# start_check()

# def Machine_Status(name, value):
#     print(f"{name : 78} \n {name : 92}")


# def calc_average(a, b):
#     return (a + b) / 2


# avg = calc_average(10, 20)
# print(avg)

#################################################


# def check(temp):
#     return temp
#     print("실행 X")

# print(check(70))


# def calculating_machine(num_1, num_2):
#     answer = (num_1 + num_2) / 2
#     return answer


# print(calculating_machine(80, 90))
# print(calculating_machine(80, 90) + 5)


# def min_max(values):
#     return min(values), max(values)


# result = min_max([75.3, 88, 49])
# print(result)

# 실습5
answer = 0


# def check(Value):
#     return min(Value), max(Value)

#     a = answer / len(range(Value))
#     b = max(Value)
#     c = min(Value)

#     print(a, b, c)

#     low, high = check(75.3, 88, 48.1)

# 냉각기A 상태 기록
# 냉각기B 상태 기록

# 연습문제4
# def report_tmperature(equipment, temperature):
#     print(equipment, temperature, "도")


# report_tmperature("모터", 78)
# report_tmperature("펌프", 92)


# def report_vibration(equipment, vibration):
#     print(equipment, "진동", vibration)


# report_vibration("송풍기", 4.2)
# report_vibration("펌프", 3.8)


# def sensor_summary(Value_min, Value_Max):
#     a = (Value_min, Value_Max)
#     print(min(a))
#     print(max(a))
#     print((Value_Max + Value_min) / 2)


# sensor_summary(78, 92)


# def report(name, value, unit="도"):
#     print(name + ": ", str(value), unit)


# report("압축기 A", 75, 3)
# report("펌프 1", 7.2, "bar")


# def grade(temp, limit=80):
#     if temp > limit:
#         return "점거필요"
#     return "정상"


# grade(95, 90)


# def status(temp, limit=90):
#     if temp > limit:
#         print("경고")
#     else:
#         print("정상")


# status(78)
# status(95)
# status(50, 40)


# string_variable = "전역변수"


# def Variable_Test():
#     string_variable = "지역변수"


# Variable_Test()
# print("해당 변수는", string_variable, "입니다.")


# def average(a, b):
#     judge((a + b) / 2)
#     return (a + b) / 2


# def judge(value):
#     if 90 < value:
#         print("경고")
#     else:
#         print("정상")


# print(average(80, 90))


# def make_message(equipment):
#     result = equipment + "점검 완료"
#     return result


# result = make_message("모터 A")
# print(result)


# def judge_temperature(value, limit=90):
#     if value > limit:
#         return "경고"
#     else:
#         return "정상"


# def report_result(equipment, result):
#     print(equipment, judge_temperature(result))


# report_result("압축기 A", 95)


# def judge_temperature(value, limit=90):
#     if value > limit:
#         return "경고"
#     else:
#         return "정상"


# def print_report(equipment, value, result):
#     return equipment, value, result


# def run_inspection(equipment, value, limit=90):
#     print(print_report(equipment, value, "도"), judge_temperature(value))


# run_inspection("압축기 A", 85)
# run_inspection("펌프 1", 95)

# import math

# result = math.sqrt(25)
# print(result)

# from math import sqrt

# print(sqrt(25))

# # Default Import
# import math

# print(math.sqrt(16), math.ceil(4.2))

# # From Import
# from math import sqrt, ceil

# print(sqrt(16), ceil(4.2))

# # Variable Import
# import math as m

# print(m.sqrt(16), m.ceil(4.2))

# import math
# import random

# value = random.randint(1, 100)
# print(value)

# random_value = math.sqrt(value)
# print(random_value)

# import os

# cwd = os.getcwd()
# print(cwd)

# import os

# cwd = os.getcwd()
# print(cwd)
# files = os.listdir("StudyFile", "press.csv")
# for name in files:
#     print(name)

# file_path = os.path.join(files)

# import os

# print(os.getcwd())

# files = os.listdir("StudyFile")

# for i in files:
#     if i.endswith(".csv"):
#         print(i)

# import os

# current_path = os.path.dirname(os.path.abspath(__file__))

# path = os.path.join(current_path, "press.csv")

# print("StudyFile", path)

# if os.path.exists(path):
#     print("파일이 있습니다.")
# else:
#     print("파일이 없습니다.")

# import os
# import datetime

# files = os.listdir("StudyFile")
# now = datetime.datetime.now()
# print(f"파일 : {len(files)}개 / 점검 시간 : {now}")

# import os

# data = "StudyFile"
# files = os.listdir(data)
# csvs = []
# for i in files:
#     if i.endswith(".csv"):
#         csvs.append(i)

# path = os.path.join(data, csvs[0])

# for i in csvs:
#     if i.endswith(".csv"):
#         print(f"[CSV] {i} ({path})")

# import os

# f = open("StudyFile/press.csv", "r", encoding="utf-8")
# text = f.read()
# print(text)
# f.close()

f = open("StudyFile/Data/08_press.csv", "r", encoding="utf-8")
print(type(f).__name__)
f.close()
