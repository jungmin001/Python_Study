# =============================================================================
#  기초 다지기 드릴 52제 ― 정답과 해설  (처음부터 05_01까지)
# -----------------------------------------------------------------------------
#  결과만 같으면 다른 방법으로 풀어도 맞습니다.
#  [예측] 문제는 "왜 그 결과가 나오는지"의 해설을 꼭 읽어보세요.
# =============================================================================


print("=" * 12, "PART A. 출력과 변수 (01_02 · 02_01)", "=" * 12)

print("[1]")
print("안녕하세요")                # → 안녕하세요   글자는 따옴표로
print(27)                         # → 27          숫자는 따옴표 없이

print("[2]")
temp = 25
print(temp)                       # → 25     변수의 '값'
print("temp")                     # → temp   따옴표가 있으면 그냥 '글자'
# 따옴표 유무가 값과 글자를 가른다!

print("[3]")
score = 10
score = 50                        # 재할당 → 마지막에 저장한 값만 남는다
print(score)                      # → 50

print("[4]")
x = 10
x = x + 5                         # 지금 x(10) + 5 = 15 를 다시 x에
x = x * 2                         # 지금 x(15) * 2 = 30 을 다시 x에
print(x)                          # → 30
# = 는 '같다'가 아니라 '저장'. 오른쪽을 먼저 계산해 왼쪽에 담는다.

print("[5]")
a = 100
b = a                             # 그 순간의 값(100)을 '복사'
a = 999                           # a만 바뀜
print(a, b)                       # → 999 100
# b = a 는 두 변수를 묶는 게 아니다. 이후 a가 바뀌어도 b는 그대로!

print("[6]")
# 오류 이유: 따옴표가 없어서 파이썬이 '설비'라는 이름의 변수를 찾는데,
#           만든 적이 없으므로 NameError.
print("설비 시작")                 # → 설비 시작   (따옴표를 붙이면 글자)


print()
print("=" * 12, "PART B. 자료형과 연산자 (02_02 ~ 02_04)", "=" * 12)

print("[7]")
count = 3                         # int   (따옴표·소수점 없음)
temp = 25.5                       # float (소수점 있음)
name = "센서A"                     # str   (따옴표)
ok = True                         # bool  (True/False, 첫 글자 대문자)
print(count, type(count))         # → 3 <class 'int'>
print(temp, type(temp))           # → 25.5 <class 'float'>
print(name, type(name))           # → 센서A <class 'str'>
print(ok, type(ok))               # → True <class 'bool'>

print("[8]")
print(3 + 5)                      # → 8    숫자끼리는 '계산'
print("3" + "5")                  # → 35   글자끼리는 '이어 붙이기'
# 같은 + 라도 자료형이 동작을 결정한다.

print("[9]")
minutes = 200
print(minutes // 60, "시간", minutes % 60, "분")   # → 3 시간 20 분
# //(몫)이 시간, %(나머지)가 분

print("[10]")
print(10 / 2)                     # → 5.0
print(type(10 / 2))               # → <class 'float'>
# 나눗셈(/)은 딱 떨어져도 결과가 항상 실수(float)!

print("[11]")
temp = 85
print(60 <= temp and temp <= 90)  # → True   (60 이상 '그리고' 90 이하)
# print(60 <= temp <= 90) 연쇄 비교로 써도 같은 뜻

print("[12]")
age_text = "25"
# age_text + 1 은 TypeError: 글자("25")와 숫자(1)는 직접 더할 수 없다.
age = int(age_text)               # 글자 → 숫자 변환(형변환)이 먼저!
print(age + 1)                    # → 26


print()
print("=" * 12, "PART C. 문자열 (03_01 ~ 03_06)", "=" * 12)

print("[13]")
word = "SENSOR"
print(word[0])                    # → S   첫 글자는 0번!
print(word[-1])                   # → R   마지막은 -1

print("[14]")
print(word[:3])                   # → SEN   앞 세 글자 (0,1,2번 — 3 제외)
print(word[-3:])                  # → SOR   뒤 세 글자

print("[15]")
word = "PYTHON"
print(word[1:4])                  # → YTH      1,2,3번 (4번은 '제외'!)
print(word[::-1])                 # → NOHTYP   [::-1] = 뒤집기 공식

print("[16]")
fname = "pump_log.csv"
print(len(fname))                 # → 12     글자 수 (밑줄·점도 한 글자)
print(fname.count("_"))           # → 1      밑줄 개수
print("log" in fname)             # → True   포함 여부는 in

print("[17]")
raw = "  WARNING  "
clean = raw.strip().lower()       # 공백 제거 → 소문자 (체이닝)
print("[" + clean + "]")          # → [warning]
# 입력값 정리의 표준 순서: strip() 먼저, lower() 다음

print("[18]")
s = "alarm"
s.upper()                         # 결과를 안 받으면 그냥 버려진다!
print(s)                          # → alarm   (대문자가 안 됐다!)
# 문자열 메서드는 원본을 안 바꾼다. s = s.upper() 로 다시 받아야 한다.
# (참고: 리스트 메서드는 반대로 원본을 바꾼다 — [30]번과 비교!)

print("[19]")
phone = "010-1234-5678"
date = "2026-07-27"
print(phone.replace("-", ""))     # → 01012345678       replace 로 제거
print(date.split("-"))            # → ['2026', '07', '27']   split 은 리스트로

print("[20]")
name = "펌프A"
temp = 85.678
print(f"설비 {name}, 온도 {temp:.1f}도")    # → 설비 펌프A, 온도 85.7도
# 따옴표 앞의 f, 변수는 {중괄호}, 소수점 1자리는 :.1f (자동 반올림)


print()
print("=" * 12, "PART D. 리스트 (04_01)", "=" * 12)

print("[21]")
lucky = [7, 13, 21]               # 대괄호 + 쉼표. 값은 자유
print(lucky)                      # → [7, 13, 21]

print("[22]")
print(len(lucky))                 # → 3
# len 은 '몇 개 담겼나'. 리스트에도 문자열에도 쓰는 같은 도구.

print("[23]")
temps = [22, 25, 27, 24, 26]
print(temps[0])                   # → 22   첫 번째는 0번!
print(temps[-1])                  # → 26   마지막은 -1
# temps[4] 로 써도 되지만, 개수가 바뀌면 틀리므로 [-1] 이 안전.

print("[24]")
print(temps[-1])                  # → 26
print(temps[-3])                  # → 27   뒤에서 세 번째
# 음수는 뒤에서부터: -1(26), -2(24), -3(27)

print("[25]")
temps = [22, 25, 27, 24, 26]
print(temps[1])                   # → 25   (0번이 22, 1번이 25 — 0부터 센다!)
print(temps[-2])                  # → 24   (뒤에서 둘째)
# 흔한 실수: temps[1] 을 '첫 번째'로 착각. 첫 번째는 [0]!

print("[26]")
temps[0] = 20                     # 등호 왼쪽에 인덱스 = 그 자리만 교체
print(temps)                      # → [20, 25, 27, 24, 26]

print("[27]")
scores = []                       # 빈 리스트로 시작
scores.append(80)
scores.append(90)
scores.append(70)
print(scores)                     # → [80, 90, 70]   append 는 항상 '끝'에 추가

print("[28]")
x = [1, 2, 3]
x.remove(2)                       # '값' 2를 제거 (1번 위치가 아니라!)
print(x)                          # → [1, 3]
y = x.pop(0)                      # '0번 위치'의 값을 꺼내며 제거
print(y)                          # → 1    (꺼낸 값이 y 에 담김)
print(x)                          # → [3]
# remove(2) 를 "2번 인덱스 제거"로 착각하기 쉽다. remove 는 값, pop 은 위치!

print("[29]")
nums = [5, 2, 9, 1]
nums.sort()                       # 원본이 정렬됨
print(nums)                       # → [1, 2, 5, 9]
print(nums[0], nums[-1])          # → 1 9   정렬 후 첫 값=최소, 끝 값=최대

print("[30]")
t = [3, 1, 2]
r = t.sort()
print(r)                          # → None       ← sort 는 돌려주는 게 없다!
print(t)                          # → [1, 2, 3]  ← 정렬은 원본 t 에 이미 반영됨
# 리스트 메서드는 원본을 직접 바꾼다 ([18]번 문자열과 정반대!).
# t = t.sort() 라고 쓰면 t 가 None 이 되는 대형 사고!


print()
print("=" * 12, "PART E. 조건문 (04_02)", "=" * 12)

print("[31]")
temp = 85
if temp > 80:                     # 콜론(:) 잊지 말기
    print("주의")                  # → 주의   (들여쓰기 = 조건에 속한 블록)

print("[32]")
temp = 75
if temp > 80:                     # 75 > 80 → 거짓
    print("주의")                  # (블록 안 → 건너뜀)
print("검사 끝")                   # → 검사 끝   (블록 밖 → 항상 실행)
# "주의"는 안 나오고 "검사 끝"만 나온다. 들여쓰기가 실행 여부를 가른다!

print("[33]")
n = 10
if n % 2 == 0:                    # 2로 나눈 나머지가 0 = 짝수
    print("짝수")                  # → 짝수
else:
    print("홀수")

print("[34]")
age = 19
if age >= 19:                     # '이상' = >= (경계값 19 포함!)
    print("성인입니다")            # → 성인입니다
else:
    print("미성년자입니다")
# age > 19 로 쓰면 정확히 19살이 미성년자가 된다. 이상/초과 구분!

print("[35]")
score = 73
if score >= 90:                   # 높은 기준부터 위에서 아래로
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:                 # 73 >= 70 → 참
    print("C")                    # → C
else:
    print("F")

print("[36]")
score = 95
if score >= 60:                   # 95도 60 이상 → 여기서 걸림!
    print("통과")                  # → 통과
elif score >= 90:
    print("우수")                  # 도달 못 함
# 95점인데 "우수"가 안 나온다! 위에서부터 검사해 '처음 참인 곳 하나만' 실행되므로,
# 넓은 조건(60 이상)이 위에 있으면 좁은 조건은 영영 검사되지 않는다.
# 오류도 안 나서 발견하기 어렵다 → 높은(좁은) 기준을 항상 위에!

print("[37]")
temp = 45
if 20 <= temp <= 60:              # 연쇄 비교 (= temp >= 20 and temp <= 60)
    print("정상")                  # → 정상

print("[38]")
user = "root"
if user == "admin" or user == "root":     # 하나라도 참이면
    print("관리자")                # → 관리자
# 주의: user == "admin" or "root" 라고 쓰면 안 된다! 비교를 각각 완성할 것.

print("[39]")
is_on = False
if not is_on:                     # not False → True
    print("꺼짐 상태")             # → 꺼짐 상태

print("[40]")
# 문제점: if x = 10:  → SyntaxError
#   = 는 '대입'(값 담기)이고, 같은지 '비교'는 == 를 써야 한다.
x = 10
if x == 10:                       # == 로 고침
    print("십입니다")              # → 십입니다


print()
print("=" * 12, "PART F. for 반복문 (05_01)", "=" * 12)

print("[41]")
for i in range(3):
    print("파이팅")                # → 파이팅 (3줄)

print("[42]")
for i in range(4):
    print(i)                      # → 0 1 2 3
# range(4)는 0부터 시작해서 4는 '포함하지 않는다'. 총 4개(0,1,2,3).

print("[43]")
for i in range(1, 8):             # 7을 포함하려면 끝은 7+1 = 8
    print(i)                      # → 1 2 3 4 5 6 7
# range(1, 7) 로 쓰면 6까지만 나온다. "끝 미포함" 규칙!

print("[44]")
for i in range(5, 0, -1):         # 증가값 -1 = 거꾸로
    print(i)                      # → 5 4 3 2 1

print("[45]")
for i in range(1, 11, 2):         # 1부터 2칸씩 = 홀수
    print(i)                      # → 1 3 5 7 9

print("[46]")
for i in range(2):
    print("A")                    # 들여쓰기 안 → 반복됨 (2번)
print("B")                        # 들여쓰기 밖 → 반복 끝나고 1번
# → A A B.  들여쓰기가 "몇 번 실행되는가"를 결정한다.

print("[47]")
total = 0                         # 누적 변수는 반복 '밖'에서 0으로
for i in range(1, 101):           # 100 포함 → 끝은 101
    total += i
print(total)                      # → 5050

print("[48]")
for i in range(1, 4):
    total = 0                     # ← 매 바퀴 0으로 리셋!
    total += i
print(total)                      # → 3
# 6이 아닌 이유: total = 0 이 반복 '안'에 있어서 매 바퀴 지워지고
# 마지막 바퀴(i=3)의 0+3 만 남는다. 누적 변수 초기화는 반드시 반복 밖에!

print("[49]")
count = 0
for i in range(1, 21):
    if i % 3 == 0:                # 3의 배수만
        count += 1
print(count)                      # → 6   (3,6,9,12,15,18)

print("[50]")
for i in range(1, 10):            # 1~9
    print("7 x", i, "=", 7 * i)   # → 7 x 1 = 7  ...  7 x 9 = 63

print("[51]")
for i in range(1, 6):             # i = 1~5
    print("*" * i)                # 문자열 반복(02_03) x 반복 변수
# → *
# → **
# → ***
# → ****
# → *****

print("[52]")
total = 0
count = 0
for i in range(1, 6):             # 1~5
    total += i                    # 합계 누적 (15)
    count += 1                    # 개수 누적 (5)
print(total / count)              # → 3.0


print()
print("정답 확인 완료 - 헷갈렸던 문제는 꼭 다시 한 번 직접 쳐 보세요!")
