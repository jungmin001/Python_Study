# =============================================================================
#  실력 다지기 응용 20제 ― 정답과 해설
# -----------------------------------------------------------------------------
#  결과만 같으면 다른 방법으로 풀어도 맞습니다.
#  각 문제의 "조합 포인트"(어떤 개념들이 만나는지)를 눈여겨보세요.
# =============================================================================


print("[1]")
line = "PUMP,MOTOR,FAN"
machines = line.split(",")            # 문자열 → 리스트
print(len(machines))                  # → 3

n = 1                                 # 번호는 1부터 (카운트 변수)
for name in machines:
    print(f"{n}번: {name}")           # → 1번: PUMP / 2번: MOTOR / 3번: FAN
    n += 1
# 조합: split(03_05) + 값 반복(05_03) + 카운트 변수(05_01) + f-string(03_06)


print("[2]")
words = ["a", "b", "c"]
print(words[1])                       # → b       인덱싱 = '값 하나'
print(words[1:2])                     # → ['b']   슬라이싱 = 항상 '리스트'
# 같은 b 라도 종류가 다르다! 콜론이 있으면 결과는 무조건 리스트.


print("[3]")
texts = ["72", "85", "91"]
nums = []
total = 0
for t in texts:
    value = int(t)                    # 글자 → 숫자 변환이 핵심
    nums.append(value)
    total += value
print(nums)                           # → [72, 85, 91]
print(total)                          # → 248
# 조합: int 형변환(02_04) + 빈 리스트 append(05_03) + 누적(05_01)


print("[4]")
files = ["log.csv", "memo.txt", "data.CSV", "temp.csv"]
count = 0
for f in files:
    if f.lower().endswith(".csv"):    # lower 로 통일해야 "data.CSV" 도 잡힘!
        print(f)                      # → log.csv / data.CSV / temp.csv
        count += 1
print(count, "개")                    # → 3 개
# 조합: lower(03_04) + endswith(03_03) + for+if(05_03)
# f.endswith(".csv") 만 쓰면 대문자 .CSV 를 놓친다 — 정리 후 검사!


print("[5]")
result = ""
letters = ["A", "B", "C"]
for ch in letters:
    result = ch + result              # 새 글자를 '앞'에 붙인다
print(result)                         # → CBA
# 추적: "" → "A" → "B"+"A"="BA" → "C"+"BA"="CBA"  (앞에 붙이면 뒤집힌다!)
# result = result + ch 였다면 "ABC". 붙이는 방향이 순서를 결정한다.


print("[6]")
evens = []
odds = []
for i in range(1, 11):
    if i % 2 == 0:
        evens.append(i)
    else:
        odds.append(i)
print(evens)                          # → [2, 4, 6, 8, 10]
print(odds)                           # → [1, 3, 5, 7, 9]
# 조합: range(05_01) + 홀짝 %(02_03) + if/else(04_02) + 두 개의 그릇(05_03)


print("[7]")
temps = [22, 35, 19, 28, 41, 25]
bad = []
for t in temps:
    if not (20 <= t <= 30):           # 정상 범위의 '반대' = 벗어남
        bad.append(t)
print(bad)                            # → [35, 19, 41]
print(f"{len(temps)}개 중 {len(bad)}개 이상")   # → 6개 중 3개 이상
# t < 20 or t > 30 으로 써도 같은 뜻. not(정상) = 이상.


print("[8]")
money = 0
count = 0
while money < 10000:                  # 10000원 '미만'인 동안 반복
    money += 3000
    count += 1
print(f"{count}회, {money}원")         # → 4회, 12000원
# 추적: 3000(1) → 6000(2) → 9000(3) → 12000(4) → 12000은 10000 이상 → 종료
# 9000원에서 멈추지 않는 이유: 9000 < 10000 이라 조건이 아직 참이기 때문!


print("[9]")
for i in range(1, 6):
    print(i)                          # print 가 먼저 실행되고
    if i == 3:
        break                         # 그 다음 검사 → 3까지 '출력된 뒤' 중단
# → 1 2 3
# 기초 드릴에서는 break 가 print 보다 위에 있어서 1 2 만 나왔다.
# 같은 break 라도 '어디에 있느냐'가 결과를 바꾼다!


print("[10]")
temps = [72, 91, 85, 78]
best = temps[0]
best_i = 0
for i in range(len(temps)):           # 인덱스로 돌아야 '위치'를 알 수 있다
    if temps[i] > best:
        best = temps[i]               # 값과
        best_i = i                    # 위치를 함께 갱신!
print(f"최대 {best} (인덱스 {best_i})")     # → 최대 91 (인덱스 1)
# for t in temps 로는 값만 얻는다. 위치가 필요하면 range(len(...)) 로!


print("[11]")
names = ["펌프", "모터", "팬"]
temps = [72, 91, 65]
for i in range(len(names)):           # 같은 i 로 두 리스트를 나란히 접근
    if temps[i] > 80:
        print(f"{names[i]}: {temps[i]}도 (주의)")
    else:
        print(f"{names[i]}: {temps[i]}도")
# → 펌프: 72도
# → 모터: 91도 (주의)
# → 팬: 65도
# 짝을 이루는 두 리스트는 '같은 인덱스'로 묶는다.


print("[12]")
for i in range(2):
    for j in range(3):
        print(i, j)
# → 0 0
# → 0 1
# → 0 2
# → 1 0
# → 1 1
# → 1 2
# 바깥 1바퀴마다 안쪽이 '전부' 돈다. 총 2 x 3 = 6줄.
# 순서 주의: 안쪽(j)이 먼저 다 돌고 나서 바깥(i)이 넘어간다.


print("[13]")
for i in range(9, 0, -1):             # 9부터 1까지 역순
    print("5 x", i, "=", 5 * i)
# → 5 x 9 = 45  ...  5 x 1 = 5


print("[14]")
logs = ["INFO start", "ERROR fan stop", "INFO running", "ERROR temp high"]
errors = []
for log in logs:
    if "ERROR" in log:                # 포함 검사(03_03)로 필터링
        errors.append(log)
print(errors)                         # → ['ERROR fan stop', 'ERROR temp high']
print(len(errors))                    # → 2


print("[15]")
scores = [78, 92, 85, 64, 71]

# ① 1차 반복: 평균 구하기
total = 0
for s in scores:
    total += s
avg = total / len(scores)             # 390 / 5
print(f"평균 {avg}")                   # → 평균 78.0

# ② 2차 반복: 평균 이상만 골라내기
count = 0
for s in scores:
    if s >= avg:                      # ①에서 구한 avg 와 비교
        print(s)                      # → 78 / 92 / 85
        count += 1
print(f"{count}개")                    # → 3개
# 평균을 알아야 비교할 수 있으므로 반복이 두 번 필요하다.
# (한 번의 반복으로는 불가능 — 아직 평균을 모르는 채 비교하게 되므로!)


print("[16]")
t = [30, 10, 20]
t.sort(reverse=True)                  # 내림차순 → [30, 20, 10]
print(t[1])                           # → 20
t.append(5)                           # → [30, 20, 10, 5]
print(t[-2])                          # → 10   (뒤에서 둘째)
# 정렬·추가로 리스트가 '변한 뒤'의 모습을 기준으로 인덱싱해야 한다.


print("[17]")
scores = [95, 82, 67, 74, 88, 91]
a = 0
b = 0
c = 0
f = 0
for s in scores:
    if s >= 90:                       # 높은 기준부터!
        a += 1
    elif s >= 80:
        b += 1
    elif s >= 70:
        c += 1
    else:
        f += 1
print(f"A {a} / B {b} / C {c} / F {f}")    # → A 2 / B 2 / C 1 / F 1
# 판정(elif 사다리)과 집계(카운트 변수 4개)의 결합.
# 95,91 → A / 82,88 → B / 74 → C / 67 → F


print("[18]")
n = 12345
count = 0
while n > 0:                          # 0이 될 때까지
    n = n // 10                       # 몫으로 한 자리씩 떼어낸다
    count += 1
print(count)                          # → 5
# 추적: 12345 → 1234(1) → 123(2) → 12(3) → 1(4) → 0(5) → 종료
# while 3점검: 시작값 n / 종료 조건 n>0 / 갱신 n//10 — 모두 갖춰져 안전!


print("[19]")
raw = "  85, 91 ,72,  88  "
parts = raw.strip().split(",")        # 앞뒤 정리 → 쉼표 분리
nums = []
for p in parts:
    nums.append(int(p.strip()))       # 조각마다 공백 정리 후 숫자로
print(nums)                           # → [85, 91, 72, 88]

best = nums[0]                        # 갱신 패턴으로 최댓값
for v in nums:
    if v > best:
        best = v
print(best)                           # → 91
# 문자열 정리(03장) → 리스트 변환(05_03) → 갱신 패턴(05_02) 총동원


print("[20]")
temps = [70, 72, 75, 73, 78]
count = 0
for i in range(1, len(temps)):        # 1부터! (0번은 '직전'이 없으므로)
    if temps[i] > temps[i - 1]:       # 현재와 직전을 비교
        count += 1
print(count)                          # → 3
# 70→72 상승 / 72→75 상승 / 75→73 하락 / 73→78 상승
# i 를 0부터 돌리면 temps[-1](마지막 값!)과 비교하게 되어 틀린다.
# '직전 값과 비교'는 뒤에서 배울 시계열 분석(변화량)의 핵심 아이디어!


print()
print("정답 확인 완료 - 조합 포인트 해설을 읽고 비슷한 문제를 스스로 변형해 보세요")
