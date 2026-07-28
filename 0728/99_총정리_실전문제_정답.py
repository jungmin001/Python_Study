# =============================================================================
#  총정리 실전 15제 ― 정답과 해설
# -----------------------------------------------------------------------------
#  결과만 같으면 다른 방법으로 풀어도 맞습니다.
#  각 문제가 어떤 단원의 조합인지 해설에 적어 두었습니다.
# =============================================================================


print("[1]")
name = "PUMP-A"                    # str
temp = 82.5                        # float
hours = 1250                       # int
ok = True                          # bool
print(f"설비: {name} (가동 {hours}시간)")
print(f"온도: {temp}도 / 정상: {ok}")
# → 설비: PUMP-A (가동 1250시간)
# → 온도: 82.5도 / 정상: True
# [변수·자료형(02장) + f-string(03_06)]


print("[2]")
total_sec = 3725
h = total_sec // 3600              # 3725 // 3600 = 1 (시간)
rest = total_sec % 3600            # 3725 % 3600 = 125 (남은 초)
m = rest // 60                     # 125 // 60 = 2 (분)
s = rest % 60                      # 125 % 60 = 5 (초)
print(f"{h}시간 {m}분 {s}초")        # → 1시간 2분 5초
# [몫·나머지(02_03)를 2단계로 — '나머지에서 다시 몫'이 핵심]


print("[3]")
code = "EQP-2026-A07"
parts = code.split("-")            # ['EQP', '2026', 'A07']
kind = parts[0]
year = int(parts[1])               # 글자 '2026' → 숫자 (형변환)
num = parts[2]
print(f"종류 {kind} / {year}년 / 번호 {num}")
print("정식 코드:", code.startswith("EQP"))
# → 종류 EQP / 2026년 / 번호 A07
# → 정식 코드: True
# [split(03_05) + 인덱싱(04_01) + int(02_04) + startswith(03_03)]


print("[4]")
email = "student@school.kr"
at = email.find("@")               # 7
user_id = email[:at]               # "student"
domain = email[at + 1:]            # "school.kr"
masked = user_id[0] + "*" * (len(user_id) - 1)   # "s" + "*"x6
print(f"{masked}@{domain}")        # → s******@school.kr
# [find(03_03) + 슬라이싱(03_02) + len + 문자열 반복(02_03) + f-string]


print("[5]")
pw = "abc12"
if len(pw) < 6:                    # '미만' = <
    print(f"너무 짧음 ({len(pw)}자)")     # → 너무 짧음 (5자)
else:
    print("사용 가능")
# [len(03_03) + if/else(04_02) + f-string]


print("[6]")
scores = [88, 92, 79, 95, 84]
scores.sort()                      # [79, 84, 88, 92, 95]
middle = scores[1:-1]              # 맨 앞(최저)·맨 뒤(최고) 제외 → [84, 88, 92]
total = 0
for s in middle:
    total += s                     # 264
print(f"최고·최저 제외 평균: {total / len(middle)}")
# → 최고·최저 제외 평균: 88.0
# [sort(04_01) + 슬라이싱 [1:-1] + 누적(05_01)]
# 정렬하면 최저가 [0], 최고가 [-1]에 오므로 [1:-1] 한 번으로 둘 다 제외!


print("[7]")
stock = 100
orders = [30, -20, 50, -40, 25]
for order in orders:
    stock += order                 # 음수를 더하면 자동으로 출고가 된다
    print(f"주문 {order} -> 재고 {stock}")
print(f"최종 재고: {stock}")
# → 주문 30 -> 재고 130 / -20 -> 110 / 50 -> 160 / -40 -> 120 / 25 -> 145
# → 최종 재고: 145
# [값 반복(05_03) + 누적(05_01) — 누적 변수가 0이 아니라 100에서 시작하는 변형]


print("[8]")
names = ["펌프", "모터", "팬", "밸브"]
target1 = "팬"
target2 = "히터"

if target1 in names:               # 먼저 있는지 확인하고
    print(f"{target1}: {names.index(target1)}번 인덱스")
else:
    print(f"{target1}: 없음")

if target2 in names:
    print(f"{target2}: {names.index(target2)}번 인덱스")
else:
    print(f"{target2}: 없음")
# → 팬: 2번 인덱스
# → 히터: 없음
# [in + index(04_01) + if/else]
# in 확인 없이 index("히터") 를 부르면 ValueError! — 확인 후 사용이 안전


print("[9]")
launch = 10                        # ① 시작값
while launch > 0:                  # ② 종료 조건
    print(launch)                  # → 10 7 4 1
    launch -= 3                    # ③ 갱신
print("발사!")                      # → 발사!
# [while 3점검(05_02)]  추적: 10 → 7 → 4 → 1 → -2(조건 거짓, 출력 안 됨)


print("[10]")
answer = "1234"
attempts = ["1111", "1234", "0000"]
n = 0
for pw in attempts:
    n += 1                         # 몇 번째 시도인지 세면서
    if pw == answer:
        print(f"성공 ({n}번째 시도)")
        break                      # 찾았으니 그만 — "0000"은 검사 안 함
    else:
        print("실패")
# → 실패
# → 성공 (2번째 시도)
# [값 반복 + 카운트(05_01) + == 비교 + break(05_02)]


print("[11]")
temps = [70, 72, 71, 80, 79]
count = 0
for i in range(1, len(temps)):     # 1부터! (0번은 '직전'이 없다)
    if temps[i] - temps[i - 1] >= 5:      # 직전 대비 5도 이상 상승
        print(f"경보: {temps[i - 1]} -> {temps[i]}")
        count += 1
print(f"급상승 {count}회")
# → 경보: 71 -> 80
# → 급상승 1회
# [인덱스 반복 + i-1 비교(실력다지기 [20] 심화) + 카운트]
# 변화: +2, -1, +9(경보!), -1


print("[12]")
sentence = "the quick fox the lazy dog the end"
words = sentence.split()           # 공백 기준 → 단어 리스트 (8개)
print(f"단어 {len(words)}개")        # → 단어 8개
print(f"the {words.count('the')}번")     # → the 3번

longest = words[0]                 # 갱신 패턴 — 첫 단어를 기준으로
for w in words:
    if len(w) > len(longest):      # '길이'를 비교!
        longest = w
print(f"가장 긴 단어: {longest}")     # → 가장 긴 단어: quick
# [split(03_05) + len/count(04_01) + 갱신 패턴(05_02) — 값이 아닌 len 비교 변형]


print("[13]")
scores = [72, 95, 88, 60, 79]
my_score = 88
scores.sort(reverse=True)          # 내림차순 → [95, 88, 79, 72, 60]
rank = scores.index(my_score) + 1  # 인덱스 1 → 2등 (0부터 세니까 +1!)
print(f"{len(scores)}명 중 {rank}등")     # → 5명 중 2등
# [sort(reverse=True) + index(04_01) + '0부터 세기' 보정]


print("[14]")
results = ["  OK ", "fail", " OK", "FAIL ", "ok"]
ok_count = 0
fail_count = 0
for r in results:
    clean = r.strip().lower()      # 공백 제거 + 소문자 통일이 먼저!
    if clean == "ok":
        ok_count += 1
    else:
        fail_count += 1
print(f"ok {ok_count}개 / fail {fail_count}개")       # → ok 3개 / fail 2개
print(f"합격률 {ok_count / len(results) * 100:.1f}%")  # → 합격률 60.0%
# [strip·lower(03_04) + 카운트(05_01) + f-string :.1f]
# 정리 없이 == "ok" 로 비교하면 "  OK " 는 전부 fail 로 잘못 집계된다!


print("[15]")
sensors = [["펌프", 72], ["모터", 91], ["팬", 65], ["압축기", 88]]

total = 0
warning = []
for s in sensors:                  # s 는 [이름, 온도] 묶음
    total += s[1]                  # s[1] = 온도
    if s[1] > 80:
        warning.append(s[0])       # s[0] = 이름만 담기!

avg = total / len(sensors)         # 316 / 4

print("=" * 6 + " 관제 리포트 " + "=" * 6)
print(f"감시 설비: {len(sensors)}대")
print(f"평균 온도: {avg}도")
print(f"경고 설비: {len(warning)}대 - {warning}")
print("=" * 24)
# → ====== 관제 리포트 ======
# → 감시 설비: 4대
# → 평균 온도: 79.0도
# → 경고 설비: 2대 - ['모터', '압축기']
# → ========================
# [이중 리스트(05_03 맛보기) + 누적 + 필터링 + f-string 총동원]
# 온도(s[1])로 판단하고 이름(s[0])을 담는 것이 포인트 — 판단 기준과
# 수집 대상이 다른 문제는 실무 데이터 처리의 기본 형태다!


print()
print("정답 확인 완료 - 전부 스스로 풀었다면 기초 과정 완주!")
