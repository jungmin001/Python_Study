# =============================================================================
#  종합 실습 2 ― 정답  (하루치 센서 로그 분석)
# -----------------------------------------------------------------------------
#  정답은 '하나'가 아닙니다. 결과만 같으면 다른 방법도 맞습니다.
#  미션이 서로 이어지므로 파일 전체를 실행하면 마지막에 리포트가 완성됩니다.
# =============================================================================

logs = [
    "  PUMP-A , 72.5 ",
    " PUMP-A ,  85.0",
    "PUMP-A , 999.0 ",
    " PUMP-A , 91.2 ",
    "  PUMP-A , 66.8",
    " PUMP-A , 88.4 ",
]


print("========== [1] 워밍업 ― 반복문 오류 3개 고치기 ==========")

# 오류 1: for i in range(3)     → SyntaxError        (콜론 빠짐)
# 오류 2: 다음 줄 들여쓰기 없음    → IndentationError   (블록이 없음)
# 오류 3: total 초기화 없이 +=   → NameError          (누적 변수는 밖에서 0으로 시작)

for i in range(3):                 # 콜론 추가
    print(i)                       # → 0 1 2

for i in range(3):
    print(i)                       # 들여쓰기 추가 → 0 1 2

total = 0                          # 반복 밖에서 초기화
for i in range(3):
    total += i
print(total)                       # → 3   (0+1+2)


print()
print("========== [2] 로그 확인 ― 개수와 값 반복 ==========")

print(len(logs))                   # → 6

for log in logs:                   # 값 반복: log 에 한 줄씩 담김
    print(log)
# → "  PUMP-A , 72.5 " 같은 지저분한 원본 6줄이 그대로 출력됨


print()
print("========== [3] 로그 한 줄 해부 ==========")

parts = logs[0].strip().split(",")     # 앞뒤 공백 제거 후 쉼표로 분리
print(parts)                           # → ['PUMP-A ', ' 72.5']
#   나눈 조각 안에는 아직 공백이 남아 있다!

name = parts[0].strip()
print("[" + name + "]")                # → [PUMP-A]

value = float(parts[1].strip())        # 조각 정리 후 숫자로 변환
print(value, type(value))              # → 72.5 <class 'float'>


print()
print("========== [4] 반복으로 전체 변환 ==========")

temps = []                             # 빈 그릇은 반복 '밖'에서!
for log in logs:
    parts = log.strip().split(",")     # [3]의 해부 과정을
    value = float(parts[1].strip())    # 모든 로그에 반복 적용
    temps.append(value)

print(temps)                           # → [72.5, 85.0, 999.0, 91.2, 66.8, 88.4]
print(len(temps))                      # → 6


print()
print("========== [5] 오류값 제거 ==========")

if 999.0 in temps:                     # 있는지 확인하고
    temps.remove(999.0)                # 값 기준으로 제거

print(temps)                           # → [72.5, 85.0, 91.2, 66.8, 88.4]
print(len(temps))                      # → 5


print()
print("========== [6] 평균 구하기 ― 누적 패턴 ==========")

total = 0                              # ① 밖에서 0으로
for t in temps:                        # ② 반복하며
    total += t                         # ③ 누적
avg = total / len(temps)               # 403.9 / 5
print(f"평균 {avg:.1f}도")              # → 평균 80.8도


print()
print("========== [7] 최고·최저 ― 갱신 패턴 ==========")

high = temps[0]                        # 첫 값(72.5)을 기준으로
low = temps[0]
for t in temps:
    if t > high:
        high = t                       # 더 크면 갱신: 72.5 → 85.0 → 91.2
    if t < low:
        low = t                        # 더 작으면 갱신: 72.5 → 66.8
print("최고", high)                     # → 최고 91.2
print("최저", low)                      # → 최저 66.8


print()
print("========== [8] 기준 초과만 골라내기 ― 필터링 ==========")

hot = []
for t in temps:
    if t > 80:
        hot.append(t)
print(hot)                             # → [85.0, 91.2, 88.4]
print(len(hot))                        # → 3


print()
print("========== [9] 값마다 판정 라벨 붙이기 ==========")

for t in temps:
    if t > 90:                         # 좁은(높은) 조건을 위에!
        print(f"{t}도 - 위험")
    elif t > 80:
        print(f"{t}도 - 주의")
    else:
        print(f"{t}도 - 정상")
# → 72.5도 - 정상
# → 85.0도 - 주의
# → 91.2도 - 위험
# → 66.8도 - 정상
# → 88.4도 - 주의


print()
print("========== [10] 판정 개수 세기 ==========")

danger = 0
warn = 0
normal = 0
for t in temps:
    if t > 90:
        danger += 1
    elif t > 80:
        warn += 1
    else:
        normal += 1
print("위험", danger, "/ 주의", warn, "/ 정상", normal)   # → 위험 1 / 주의 2 / 정상 2


print()
print("========== [11] 90도 초과 검색 ― 플래그 + break ==========")

found = False
first_over = 0
for t in temps:
    if t > 90:
        first_over = t                 # 찾은 값을 기억하고
        found = True                   # 플래그를 켠 뒤
        break                          # 더 볼 필요 없으니 중단
print(found)                           # → True
print(first_over)                      # → 91.2


print()
print("========== [12] 최종 리포트 ==========")

print("=" * 34)
print("PUMP-A 일일 측정 리포트")
print("-" * 34)
print(f"유효 측정 : {len(temps)}회 (오류값 1건 제외)")
print(f"평균 : {avg:.1f}도")
print(f"최저 / 최고 : {low}도 / {high}도")
print(f"기준(80) 초과 : {len(hot)}회 - {hot}")
print(f"판정 : 위험 {danger} / 주의 {warn} / 정상 {normal}")
print(f"90도 초과 발생 : {found} (첫 발생 {first_over}도)")
print("=" * 34)

# → ==================================
# → PUMP-A 일일 측정 리포트
# → ----------------------------------
# → 유효 측정 : 5회 (오류값 1건 제외)
# → 평균 : 80.8도
# → 최저 / 최고 : 66.8도 / 91.2도
# → 기준(80) 초과 : 3회 - [85.0, 91.2, 88.4]
# → 판정 : 위험 1 / 주의 2 / 정상 2
# → 90도 초과 발생 : True (첫 발생 91.2도)
# → ==================================


print()
print("========== [도전] 냉각 시뮬레이션 ― while ==========")

temp = 91                              # ① 시작값
count = 0
while temp > 70:                       # ② 종료 조건: 70 이하가 되면 멈춤
    temp -= 5                          # ③ 갱신: 거짓 방향(내려가는 쪽)으로
    count += 1
    print(f"냉각 {count}회 -> {temp}도")
print(f"총 {count}회 냉각, 최종 {temp}도")
# → 냉각 1회 -> 86도
# → 냉각 2회 -> 81도
# → 냉각 3회 -> 76도
# → 냉각 4회 -> 71도
# → 냉각 5회 -> 66도
# → 총 5회 냉각, 최종 66도

# 추적: 91 → 86 → 81 → 76 → 71 (아직 70 초과!) → 66 (70 이하 → 종료)


print()
print("정답 확인 완료 - 틀린 미션은 해당 단원 복습 파일을 다시 보세요")
