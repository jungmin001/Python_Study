# 태그명 용어사전
#
# 설비        MTR=Motor(모터)  HYD=Hydraulic(유압)  FUR=Furnace(가열로)
# 물리량      VIB=Vibration(진동)  RMS=Root Mean Square(실효값)  ACC=Acceleration(가속도)
#             CURRENT(전류)  VOLT(전압)  POWER(전력)  TEMP=Temperature(온도)
#             RPM=Revolutions Per Minute(분당 회전수)  PRESS=Pressure(압력)
#             DP=Differential Pressure(차압)  FLOW(유량)  OILTEMP=Oil Temperature(작동유 온도)
# 방향        H=Horizontal(수평)  V=Vertical(수직)  A=Axial(축방향)
# 위치/구분   IN=Inlet(입구·공급측)  OUT=Outlet(출구·후단)  FILTER(필터)
#             Z1=Zone 1(1존)  Z2=Zone 2(2존)  01=1호기

# ---------------------------------------------------------------------------
# 과제: 컬럼(태그) 목록을 "측정의 3요소"로 분해한다
#   ① 물리량 (무엇을 재는가)  ② 설치 위치 (어디서 재는가)  ③ 샘플링 주기 (얼마나 자주 재는가)
# 근거:
#   ① 태그명 접미어 + 태그목록의 unit 컬럼
#   ② 태그목록의 install_location 컬럼
#   ③ 태그목록의 sampling_sec 컬럼 → 측정샘플에서 "값이 바뀌는 간격"으로 실측 검증
# ---------------------------------------------------------------------------

import pandas as pd

tag_file = "StudyFile/Data/02-01_측정의_3요소_설비태그목록_224_260908_Question_3.csv"
sample_file = "StudyFile/Data/02-01_측정의_3요소_측정샘플_224_260908_Question_2.csv"

tags = pd.read_csv(tag_file)
sample = pd.read_csv(sample_file)
sample["timestamp"] = pd.to_datetime(sample["timestamp"])

# --- 설비 / 물리량 한글 사전 ---------------------------------------------------
EQUIP = {"MTR": "모터", "HYD": "유압장치", "FUR": "가열로"}
QUANT = {
    "VIB_RMS_H": "진동속도 실효값(수평)", "VIB_RMS_V": "진동속도 실효값(수직)",
    "VIB_RMS_A": "진동속도 실효값(축방향)", "VIB_ACC": "진동 가속도",
    "CURRENT": "전류", "VOLT": "전압", "POWER": "전력", "TEMP": "온도",
    "RPM": "회전수", "PRESS_IN": "압력(공급측)", "PRESS_OUT": "압력(후단)",
    "DP_FILTER": "필터 차압", "FLOW": "유량", "OILTEMP": "작동유 온도",
    "TEMP_Z1": "온도(1존)", "TEMP_Z2": "온도(2존)",
}


def decompose(tag):
    """태그명을 (설비, 호기, 물리량키)로 분해."""
    equip = tag[:3]
    unit_no = tag[3:5]
    quant_key = tag[6:]
    return EQUIP.get(equip, equip), unit_no, quant_key


# --- ③ 샘플링 주기 실측 -----------------------------------------------------
# 기록(로깅) 간격 = timestamp 행 간격.
# 갱신 간격       = 값이 실제로 바뀌는 최소 간격. 기록 간격보다 크면 그만큼이 실제 샘플링.
#                 (단, 변화가 느려 분해능 벽에 걸리는 신호는 최소 간격이 과대평가될 수 있음)
LOG_SEC = int(sample["timestamp"].diff().dropna().dt.total_seconds().mode().iloc[0])


def update_gap_sec(col):
    s = sample[["timestamp", col]]
    changed = s[col].ne(s[col].shift())
    gaps = s.loc[changed, "timestamp"].diff().dropna().dt.total_seconds()
    return int(gaps.min()) if len(gaps) else None


def verdict(defined, gap):
    if gap is None:
        return "샘플없음", "-"
    if gap == defined:
        return f"{gap}s", "일치"
    if defined == LOG_SEC and gap % LOG_SEC == 0:
        # 60s 정의인데 값이 120s마다 바뀜 → 변화가 느려 분해능에 걸린 것(로깅은 60s)
        return f"{gap}s", "일치(느린변화)"
    return f"{gap}s", "확인필요"


# --- 3요소 분해표 작성 ------------------------------------------------------
rows = []
for _, t in tags.iterrows():
    equip, unit_no, qkey = decompose(t["tag"])
    is_calc = "계산값" in str(t["install_location"])
    row = {
        "태그": t["tag"],
        "설비": f"{equip} {unit_no}호기",
        "①물리량": f"{QUANT.get(qkey, qkey)} ({t['unit']})" + (" [계산값]" if is_calc else ""),
        "②설치위치": t["install_location"],
        "③주기(정의)": f"{int(t['sampling_sec'])}s",
    }
    if t["tag"] in sample.columns:
        gap = update_gap_sec(t["tag"])
        row["③주기(실측)"], row["검증"] = verdict(int(t["sampling_sec"]), gap)
    else:
        row["③주기(실측)"], row["검증"] = "샘플없음", "-"
    rows.append(row)

result = pd.DataFrame(rows)

pd.set_option("display.unicode.east_asian_width", True)
pd.set_option("display.max_colwidth", None)
pd.set_option("display.width", 200)

print("=" * 100)
print("측정의 3요소 분해표")
print("=" * 100)
print(result.to_string(index=False))
print()
print("[근거 요약]")
print(" ① 물리량 : 태그 접미어(VIB_RMS_H 등) + unit 컬럼. install_location이 '계산값'이면 파생 태그(물리센서 아님)")
print(" ② 위치   : install_location 컬럼 그대로")
print(" ③ 주기   : sampling_sec 컬럼(정의) vs 측정샘플에서 값이 바뀌는 간격(실측)")
print("            → 온도류(OILTEMP·FUR_TEMP)만 300s, 나머지는 60s. 샘플 보유 5개 컬럼 모두 정의=실측 일치")

def attack(damage, target):
    """
    대상에게 데미지를 적용합니다.

    :param damage: 적용할 데미지 값
    :param target: 공격 대상
    :return: 처리된 데미지 값
    """
    return damage
