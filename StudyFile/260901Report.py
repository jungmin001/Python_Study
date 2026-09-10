import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

sensor_file = "StudyFile/Data/02-04_센서_고장_판별_이상구간샘플_210_260901_Question_2.csv"
alarm_file = "StudyFile/Data/02-04_센서_고장_판별_정비알람이력_210_260901_Question_3.csv"

df = pd.read_csv(sensor_file)
alarm = pd.read_csv(alarm_file)

df.columns = df.columns.str.strip()
alarm.columns = alarm.columns.str.strip()

df["timestamp"] = pd.to_datetime(df["timestamp"])
alarm["event_time"] = pd.to_datetime(alarm["event_time"])

df = df.sort_values("timestamp").reset_index(drop=True)
alarm = alarm.sort_values("event_time").reset_index(drop=True)

df["TEMP_DIFF"] = (df["MTR02_TEMP"] - df["MTR02_TEMP_B"]).abs()
df["is_stop"] = ((df["MTR02_RUN"] == 0) & (df["MTR02_CURRENT"] == 0))
df["is_vib_missing"] = df["MTR02_VIB_H"].isna()
df["is_pressure_high"] = (df["HYD02_PRESS_ACC"] >= df["HYD02_PRESS_ACC"].quantile(0.95))
df["is_temp_diff"] = (df["TEMP_DIFF"] >= df["TEMP_DIFF"].quantile(0.95))

def Judgment(value):
    if value["is_stop"]:
        return "조업 정지 또는 운전 중단 영향"

    if value["is_vib_missing"] and value["MTR02_RUN"] == 1:
        return "통신 장애 또는 데이터 수집 문제"

    if value["is_pressure_high"]:
        return "실제 설비 이상"

    if value["is_temp_diff"]:
        return "센서 드리프트 또는 계측 이상"

    return "정상"

df["Judgment"] = df.apply(Judgment, axis=1)
result = df[df["Judgment"] != "정상"].copy()

print(result[
    [
        "timestamp",
        "Judgment",
        "MTR02_RUN",
        "MTR02_CURRENT",
        "MTR02_VIB_H",
        "HYD02_PRESS_ACC",
        "MTR02_TEMP",
        "MTR02_TEMP_B",
        "TEMP_DIFF"
    ]
])

# 이상 구간 : 2026-04-01 18:00~21:00
# 관련 센서 : MTR02_RUN, MTR02_CURRENT, MTR02_VIB_H
# 관찰 사실 : 설비가 멈춘 상태에서 전류와 진동값이 함께 감소함
# 알람 이력 비교 : 정지 및 운전 재개
# 판단 결과 : 조업 정지 또는 운전 중단에 영향
# 근거 및 해석 : 센서 이상이 아니라 설비 정지에 따른 정상적인 변화로 판단

# 이상 구간 : 2026-04-02 06:00~09:00
# 관련 센서 : MTR02_VIB_H
# 관찰 사실 : 진동 데이터가 정상적으로 수집되지 않음
# 알람 이력 비교 : 통신 장애 및 복구
# 판단 결과 : 통신 장애 또는 데이터 수집 문제
# 근거 및 해석 : 진동 설비 이상이 아닌 통신 문제로 판단

# 이상 구간 : 2026-04-02 11:00~13:30
# 관련 센서 : HYD02_PRESS_ACC
# 관찰 사실 : 어큐뮬레이터 압력이 높은 값으로 유지됨
# 알람 이력 비교 : 압력 상한 도달 알람
# 판단 결과 : 실제 설비 이상
# 근거 및 해석 : 알람 이력과 센서값이 일치하므로 유압 계통 이상 가능성이 높음

# 이상 구간 : 2026-04-02 ~
# 관련 센서 : MTR02_TEMP, MTR02_TEMP_B
# 관찰 사실 : 중복 온도 센서가 같은 방향으로 움직이지만 측정값 차이가 발생함
# 알람 이력 비교 : MTR02_TEMP 센서 교정
# 판단 결과 : 센서 드리프트 또는 계측 이상
# 근거 및 해석 : 중복 센서 간 차이가 발생으로 센서 교정, 드레프트 확인 필요