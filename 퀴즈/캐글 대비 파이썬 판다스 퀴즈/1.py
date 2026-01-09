# ==============================================================================
# 캐글 대비 파이썬/판다스 중급 학습 문제 20제 (실습용)
# 작성자: 대구과학고등학교 김동균
# ==============================================================================

import pandas as pd
import numpy as np

print("Google Colab 실습을 시작합니다! 아래 문제를 풀고 답안 코드와 비교해보세요.")
print("-" * 50)

# --- 문제 1: 데이터프레임 생성 및 인덱스 재설정 ---
print("## 문제 1: Multi-Index 데이터프레임 인덱스 초기화")
data = {'A': [1, 2], 'B': [3, 4], 'C': [5, 6]}
index = pd.MultiIndex.from_tuples([('G1', 'S1'), ('G2', 'S2')], names=['Group', 'Subgroup'])
df1 = pd.DataFrame(data, index=index)
print("원본 DataFrame:\n", df1)
# [여기에 문제 1 풀이 코드를 작성하세요]


# --- 문제 2: 결측치(NaN) 처리 - 중앙값 대체 ---
print("\n" + "=" * 30 + "\n## 문제 2: 결측치 중앙값 대체")
data = {'Age': [25, 30, None, 45, 30, None, 22], 'Fare': [10, 20, 15, 30, 10, 5, 12]}
df2 = pd.DataFrame(data)
print("원본 DataFrame:\n", df2)
# [여기에 문제 2 풀이 코드를 작성하세요]


# --- 문제 3: 조건부 선택 및 값 변경 (loc 사용) ---
print("\n" + "=" * 30 + "\n## 문제 3: loc를 사용한 조건부 값 변경")
df3 = pd.DataFrame({'Score': [75, 85, 90, 65, 80], 'Grade': ['C', 'B', 'A', 'D', 'B']})
print("원본 DataFrame:\n", df3)
# [여기에 문제 3 풀이 코드를 작성하세요]


# --- 문제 4: Categorical Feature Encoding (get_dummies) ---
print("\n" + "=" * 30 + "\n## 문제 4: One-Hot Encoding (get_dummies)")
df4 = pd.DataFrame({'Fruit': ['Apple', 'Banana', 'Apple', 'Orange'], 'Color': ['Red', 'Yellow', 'Green', 'Orange']})
print("원본 DataFrame:\n", df4)
# [여기에 문제 4 풀이 코드를 작성하세요]


# --- 문제 5: 그룹별 집계 (groupby) ---
print("\n" + "=" * 30 + "\n## 문제 5: Groupby와 agg를 사용한 다중 집계")
data = {'City': ['Seoul', 'Busan', 'Seoul', 'Busan', 'Seoul'], 'Sales': [100, 150, 120, 200, 80]}
df5 = pd.DataFrame(data)
print("원본 DataFrame:\n", df5)
# [여기에 문제 5 풀이 코드를 작성하세요]


# --- 문제 6: Series의 apply를 이용한 데이터 변환 ---
print("\n" + "=" * 30 + "\n## 문제 6: log(x+1) 변환 적용")
df6 = pd.DataFrame({'Price': [10, 50, 100, 5, 200]})
print("원본 DataFrame:\n", df6)
# [여기에 문제 6 풀이 코드를 작성하세요]


# --- 문제 7: 데이터프레임 병합 (merge) ---
print("\n" + "=" * 30 + "\n## 문제 7: Inner Join 병합")
df7_1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['A', 'B', 'C']})
df7_2 = pd.DataFrame({'ID': [2, 3, 4], 'Salary': [500, 600, 700]})
print("DF1:\n", df7_1)
print("DF2:\n", df7_2)
# [여기에 문제 7 풀이 코드를 작성하세요]


# --- 문제 8: 이상치 제거 (IQR 활용) ---
print("\n" + "=" * 30 + "\n## 문제 8: IQR 기반 이상치 제거")
df8 = pd.DataFrame({'Value': [10, 12, 15, 18, 20, 100, 11]})
print("원본 DataFrame:\n", df8)
# [여기에 문제 8 풀이 코드를 작성하세요]


# --- 문제 9: lambda를 이용한 새 컬럼 생성 (apply) ---
print("\n" + "=" * 30 + "\n## 문제 9: apply(axis=1)을 이용한 조건부 컬럼 생성")
df9 = pd.DataFrame({'A': [50, 40, 60, 70], 'B': [60, 50, 30, 20]})
print("원본 DataFrame:\n", df9)
# [여기에 문제 9 풀이 코드를 작성하세요]


# --- 문제 10: Pivot Table 생성 ---
print("\n" + "=" * 30 + "\n## 문제 10: 피벗 테이블 생성")
data = {'Product': ['A', 'B', 'A', 'B', 'A'], 'Region': ['East', 'West', 'East', 'West', 'West'], 'Sales': [10, 20, 15, 25, 30]}
df10 = pd.DataFrame(data)
print("원본 DataFrame:\n", df10)
# [여기에 문제 10 풀이 코드를 작성하세요]


# --- 문제 11: 문자열 처리 (str.split) ---
print("\n" + "=" * 30 + "\n## 문제 11: 문자열 분리 후 요소 추출")
df11 = pd.DataFrame({'Name': ['Kim, Jisoo', 'Park, Minho', 'Lee, Sena']})
print("원본 DataFrame:\n", df11)
# [여기에 문제 11 풀이 코드를 작성하세요]


# --- 문제 12: 데이터 타입 변환 (astype) ---
print("\n" + "=" * 30 + "\n## 문제 12: astype()을 이용한 타입 변환")
df12 = pd.DataFrame({'Count': [10, 20, 30], 'Price': [1.5, 2.5, 3.5]})
print("원본 DataFrame:\n", df12)
# [여기에 문제 12 풀이 코드를 작성하세요]


# --- 문제 13: Time Series (datetime) - 날짜 구성요소 추출 ---
print("\n" + "=" * 30 + "\n## 문제 13: 날짜 타입 변환 및 년도 추출")
df13 = pd.DataFrame({'Date': ['2023-01-01', '2024-03 파일 입출력-15', '2023-12-31']})
print("원본 DataFrame:\n", df13)
# [여기에 문제 13 풀이 코드를 작성하세요]


# --- 문제 14: Value Count를 이용한 빈도수 확인 및 정규화 ---
print("\n" + "=" * 30 + "\n## 문제 14: 상대 빈도수 계산")
df14 = pd.DataFrame({'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'A']})
print("원본 DataFrame:\n", df14)
# [여기에 문제 14 풀이 코드를 작성하세요]


# --- 문제 15: Binning/Discretization (qcut) ---
print("\n" + "=" * 30 + "\n## 문제 15: qcut을 사용한 동일 빈도 그룹화")
df15 = pd.DataFrame({'Age': [15, 25, 30, 45, 55, 60, 20, 35]})
print("원본 DataFrame:\n", df15)
# [여기에 문제 15 풀이 코드를 작성하세요]


# --- 문제 16: Lambda와 Map을 이용한 값 매핑 ---
print("\n" + "=" * 30 + "\n## 문제 16: map()을 사용한 Label Encoding")
df16 = pd.DataFrame({'Gender': ['M', 'F', 'F', 'M', 'F']})
print("원본 DataFrame:\n", df16)
# [여기에 문제 16 풀이 코드를 작성하세요]


# --- 문제 17: Multi-Index에서 특정 레벨 드롭 ---
print("\n" + "=" * 30 + "\n## 문제 17: Multi-Index 레벨 삭제")
index = pd.MultiIndex.from_tuples([('G1', 'S1'), ('G2', 'S2')], names=['Group', 'Subgroup'])
df17 = pd.DataFrame({'Data': [10, 20]}, index=index)
print("원본 DataFrame:\n", df17)
# [여기에 문제 17 풀이 코드를 작성하세요]


# --- 문제 18: 조건부 인덱스 변경 (set_index) ---
print("\n" + "=" * 30 + "\n## 문제 18: 컬럼을 인덱스로 설정")
df18 = pd.DataFrame({'City': ['Seoul', 'Busan', 'Incheon'], 'Population': [1000, 350, 250]})
print("원본 DataFrame:\n", df18)
# [여기에 문제 18 풀이 코드를 작성하세요]


# --- 문제 19: 문자열 포함 여부 확인 (str.contains) ---
print("\n" + "=" * 30 + "\n## 문제 19: 정규표현식을 사용한 조건부 필터링")
df19 = pd.DataFrame({'Text': ['I love Python', 'I love SQL', 'I love R', 'I love Java']})
print("원본 DataFrame:\n", df19)
# [여기에 문제 19 풀이 코드를 작성하세요]


# --- 문제 20: 데이터프레임 정렬 (sort_values) ---
print("\n" + "=" * 30 + "\n## 문제 20: 다중 조건 정렬")
df20 = pd.DataFrame({'Sales': [100, 100, 50, 200], 'Profit': [10, 5, 20, 15]})
print("원본 DataFrame:\n", df20)
# [여기에 문제 20 풀이 코드를 작성하세요]