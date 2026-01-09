import json

# 1. 노트북의 기본 구조 정의
notebook = {
    "cells": [],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.8.5"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

# 2. 셀 추가 함수 정의
def add_markdown_cell(content):
    notebook["cells"].append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [line + "\n" for line in content.split("\n")]
    })

def add_code_cell(code):
    notebook["cells"].append({
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [line + "\n" for line in code.split("\n")]
    })

# 3. 콘텐츠 생성

# [헤더]
add_markdown_cell("# 🏆 캐글 대비 파이썬/판다스 중급 학습 문제 20제\n\n**작성자: 대구과학고등학교 김동균**\n\n---\n\n이 노트북은 캐글(Kaggle) 데이터 분석 문제를 풀기 위한 필수 스킬을 연습하기 위해 제작되었습니다.\n각 셀의 문제를 읽고 코드를 작성하여 실행해 보세요.")

# [라이브러리 임포트]
add_code_cell("import pandas as pd\nimport numpy as np\n\nprint('실습 준비 완료! (배경: 흰색)')")

# [문제 데이터베이스]
problems = [
    {
        "title": "문제 1: Multi-Index 데이터프레임 인덱스 초기화",
        "desc": "Multi-Index 데이터프레임을 생성하고 인덱스 레벨을 초기화하여 일반 컬럼으로 변환하시오.",
        "setup": "data = {'A': [1, 2], 'B': [3, 4], 'C': [5, 6]}\nindex = pd.MultiIndex.from_tuples([('G1', 'S1'), ('G2', 'S2')], names=['Group', 'Subgroup'])\ndf = pd.DataFrame(data, index=index)\n\n# df를 확인해보세요\nprint(df)\nprint('-'*20)",
        "hint": "reset_index() 메서드를 사용해보세요.",
        "solution": "df_reset = df.reset_index()\nprint(df_reset)",
        "explanation": "reset_index()는 인덱스를 일반 컬럼으로 이동시키고, 정수형 인덱스를 새로 생성합니다."
    },
    {
        "title": "문제 2: 결측치(NaN) 처리 - 중앙값 대체",
        "desc": "'Age' 컬럼의 결측치(NaN)를 해당 컬럼의 **중앙값(Median)**으로 대체하시오.",
        "setup": "data = {'Age': [25, 30, None, 45, 30, None, 22], 'Fare': [10, 20, 15, 30, 10, 5, 12]}\ndf = pd.DataFrame(data)",
        "hint": "fillna() 메서드와 median() 메서드를 결합하여 사용하세요.",
        "solution": "median_age = df['Age'].median()\ndf['Age'].fillna(median_age, inplace=True)\nprint(df['Age'])",
        "explanation": "중앙값은 이상치(outlier)에 덜 민감하여 평균보다 결측치 대체값으로 선호되는 경우가 많습니다."
    },
    {
        "title": "문제 3: 조건부 선택 및 값 변경 (loc 사용)",
        "desc": "'Score' 컬럼의 값이 80 이상인 행에 대해 'Grade' 컬럼의 값을 'A'로 설정하시오. (loc 사용)",
        "setup": "df = pd.DataFrame({'Score': [75, 85, 90, 65, 80], 'Grade': ['C', 'B', 'A', 'D', 'B']})",
        "hint": "df.loc[조건, '컬럼명'] 형식을 사용하세요.",
        "solution": "df.loc[df['Score'] >= 80, 'Grade'] = 'A'\nprint(df)",
        "explanation": "데이터프레임의 값 변경 시 SettingWithCopyWarning을 피하기 위해 **.loc**를 사용하는 것이 안전합니다."
    },
    {
        "title": "문제 4: One-Hot Encoding (get_dummies)",
        "desc": "'Color' 컬럼에 대해 One-Hot Encoding을 수행하시오.",
        "setup": "df = pd.DataFrame({'Fruit': ['Apple', 'Banana', 'Apple', 'Orange'], 'Color': ['Red', 'Yellow', 'Green', 'Orange']})",
        "hint": "pd.get_dummies() 함수를 사용하세요.",
        "solution": "df_encoded = pd.get_dummies(df, columns=['Color'], prefix='Color')\nprint(df_encoded)",
        "explanation": "범주형 변수를 머신러닝 모델이 이해할 수 있는 수치형(0, 1)으로 변환합니다."
    },
    {
        "title": "문제 5: 그룹별 집계 (groupby)",
        "desc": "'City'별 'Sales'의 **합계**와 **평균**을 동시에 계산하시오.",
        "setup": "data = {'City': ['Seoul', 'Busan', 'Seoul', 'Busan', 'Seoul'], 'Sales': [100, 150, 120, 200, 80]}\ndf = pd.DataFrame(data)",
        "hint": "groupby() 후 agg(['sum', 'mean'])을 사용하세요.",
        "solution": "result = df.groupby('City')['Sales'].agg(['sum', 'mean'])\nprint(result)",
        "explanation": "agg() 메서드를 사용하면 여러 집계 함수를 한 번에 적용할 수 있습니다."
    },
    {
        "title": "문제 6: apply를 이용한 로그 변환 (LaTeX 적용)",
        "desc": "'Price' 컬럼의 값들에 대해 **$\\text{log}(x+1)$ 변환**을 적용하시오.",
        "setup": "df = pd.DataFrame({'Price': [10, 50, 100, 5, 200]})",
        "hint": "np.log1p 함수를 apply()와 함께 사용하세요.",
        "solution": "df['Log_Price'] = df['Price'].apply(np.log1p)\nprint(df)",
        "explanation": "np.log1p는 $x$가 0에 가까울 때 정밀도를 높여 **$\\text{log}(x+1)$**를 계산합니다. 데이터의 스케일을 줄일 때 유용합니다."
    },
    {
        "title": "문제 7: 데이터프레임 병합 (Inner Join)",
        "desc": "'ID'를 기준으로 두 데이터프레임을 이너 조인(Inner Join)하시오.",
        "setup": "df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['A', 'B', 'C']})\ndf2 = pd.DataFrame({'ID': [2, 3, 4], 'Salary': [500, 600, 700]})",
        "hint": "pd.merge() 함수와 how='inner' 옵션을 사용하세요.",
        "solution": "merged_df = pd.merge(df1, df2, on='ID', how='inner')\nprint(merged_df)",
        "explanation": "Inner Join은 양쪽 데이터프레임에 모두 존재하는 키 값에 대해서만 데이터를 병합합니다."
    },
    {
        "title": "문제 8: 이상치 제거 (IQR 활용)",
        "desc": "'Value' 컬럼에 대해 IQR 방법을 사용하여 이상치를 제거하시오. (Q1-1.5*IQR ~ Q3+1.5*IQR)",
        "setup": "df = pd.DataFrame({'Value': [10, 12, 15, 18, 20, 100, 11]})",
        "hint": "quantile()로 Q1, Q3를 구하고 범위를 설정하여 필터링하세요.",
        "solution": "Q1 = df['Value'].quantile(0.25)\nQ3 = df['Value'].quantile(0.75)\nIQR = Q3 - Q1\nlower_bound = Q1 - 1.5 * IQR\nupper_bound = Q3 + 1.5 * IQR\n\ndf_filtered = df[(df['Value'] >= lower_bound) & (df['Value'] <= upper_bound)]\nprint(df_filtered)",
        "explanation": "IQR 방식은 데이터의 분포를 기반으로 통계적으로 이상치를 탐지하는 일반적인 방법입니다."
    },
    {
        "title": "문제 9: Lambda와 apply를 이용한 조건부 컬럼 생성",
        "desc": "'A'와 'B'의 합이 100 이상이면 'High', 아니면 'Low'인 'Level' 컬럼을 생성하시오.",
        "setup": "df = pd.DataFrame({'A': [50, 40, 60, 70], 'B': [60, 50, 30, 20]})",
        "hint": "apply(lambda row: ..., axis=1)을 사용하세요.",
        "solution": "df['Level'] = df.apply(lambda row: 'High' if (row['A'] + row['B']) >= 100 else 'Low', axis=1)\nprint(df)",
        "explanation": "axis=1을 주어 행 단위로 데이터를 처리할 수 있습니다."
    },
    {
        "title": "문제 10: Pivot Table 생성",
        "desc": "'Product'를 인덱스, 'Region'을 컬럼, 'Sales'의 평균을 값으로 하는 피벗 테이블을 만드시오.",
        "setup": "data = {'Product': ['A', 'B', 'A', 'B', 'A'], 'Region': ['East', 'West', 'East', 'West', 'West'], 'Sales': [10, 20, 15, 25, 30]}\ndf = pd.DataFrame(data)",
        "hint": "pd.pivot_table() 함수를 사용하세요.",
        "solution": "pivot = pd.pivot_table(df, values='Sales', index='Product', columns='Region', aggfunc='mean')\nprint(pivot)",
        "explanation": "피벗 테이블은 데이터를 구조적으로 요약하여 볼 때 매우 강력한 도구입니다."
    },
    {
        "title": "문제 11: 문자열 처리 (str.split)",
        "desc": "'Name' 컬럼에서 쉼표 뒤의 'Surname'(이름)만 추출하시오.",
        "setup": "df = pd.DataFrame({'Name': ['Kim, Jisoo', 'Park, Minho', 'Lee, Sena']})",
        "hint": ".str.split() 후 인덱싱을 사용하세요.",
        "solution": "df['Surname'] = df['Name'].str.split(', ').str[0]\nprint(df)",
        "explanation": "판다스의 문자열 메서드는 **.str** 접근자를 통해 사용할 수 있습니다."
    },
    {
        "title": "문제 12: 데이터 타입 변환 (astype)",
        "desc": "'Count' 컬럼을 실수형(float)으로 변환하시오.",
        "setup": "df = pd.DataFrame({'Count': [10, 20, 30], 'Price': [1.5, 2.5, 3.5]})",
        "hint": "astype(float)을 사용하세요.",
        "solution": "df['Count'] = df['Count'].astype(float)\nprint(df.dtypes)",
        "explanation": "데이터 분석 전 올바른 데이터 타입(Type)을 맞추는 것은 필수적입니다."
    },
    {
        "title": "문제 13: 시계열 데이터 (Datetime)",
        "desc": "'Date' 컬럼을 datetime으로 변환하고 'Year'를 추출하시오.",
        "setup": "df = pd.DataFrame({'Date': ['2023-01-01', '2024-03 파일 입출력-15', '2023-12-31']})",
        "hint": "pd.to_datetime() 변환 후 **.dt** 접근자를 사용하세요.",
        "solution": "df['Date'] = pd.to_datetime(df['Date'])\ndf['Year'] = df['Date'].dt.year\nprint(df)",
        "explanation": ".dt 접근자를 통해 년, 월, 일, 요일 등 날짜 정보를 쉽게 추출할 수 있습니다."
    },
    {
        "title": "문제 14: 상대 빈도수 계산 (normalize)",
        "desc": "'Category' 컬럼의 각 고유값의 비율(상대 빈도)을 계산하시오.",
        "setup": "df = pd.DataFrame({'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'A']})",
        "hint": "value_counts(normalize=True) 옵션을 사용하세요.",
        "solution": "print(df['Category'].value_counts(normalize=True))",
        "explanation": "빈도수만 볼 때는 normalize=False(기본값), **비율**을 볼 때는 True를 사용합니다."
    },
    {
        "title": "문제 15: 구간 나누기 (qcut)",
        "desc": "'Age'를 4개의 동일한 빈도 그룹으로 나누고 라벨을 붙이시오.",
        "setup": "df = pd.DataFrame({'Age': [15, 25, 30, 45, 55, 60, 20, 35]})",
        "hint": "pd.qcut() 함수를 사용하세요.",
        "solution": "labels = ['Young', 'Mid', 'Old', 'Senior']\ndf['Age_Group'] = pd.qcut(df['Age'], q=4, labels=labels)\nprint(df)",
        "explanation": "qcut은 데이터의 개수가 각 구간마다 같아지도록 나눕니다. (Quantile-based Discretization)"
    },
    {
        "title": "문제 16: Map을 이용한 인코딩",
        "desc": "'Gender' 컬럼의 M을 0, F를 1로 매핑하시오.",
        "setup": "df = pd.DataFrame({'Gender': ['M', 'F', 'F', 'M', 'F']})",
        "hint": "딕셔너리와 map() 메서드를 사용하세요.",
        "solution": "mapping = {'M': 0, 'F': 1}\ndf['Encoded'] = df['Gender'].map(mapping)\nprint(df)",
        "explanation": "두 개의 클래스를 가진 이진 분류 문제에서 간단한 라벨 인코딩에 자주 쓰입니다."
    },
    {
        "title": "문제 17: Multi-Index 레벨 삭제",
        "desc": "Multi-Index에서 'Subgroup' 레벨을 삭제하시오.",
        "setup": "index = pd.MultiIndex.from_tuples([('G1', 'S1'), ('G2', 'S2')], names=['Group', 'Subgroup'])\ndf = pd.DataFrame({'Data': [10, 20]}, index=index)",
        "hint": "droplevel() 메서드를 사용하세요.",
        "solution": "df_dropped = df.droplevel('Subgroup')\nprint(df_dropped)",
        "explanation": "불필요하게 복잡한 인덱스 계층을 단순화할 때 사용합니다."
    },
    {
        "title": "문제 18: 인덱스 설정 (set_index)",
        "desc": "'City' 컬럼을 인덱스로 설정하시오.",
        "setup": "df = pd.DataFrame({'City': ['Seoul', 'Busan', 'Incheon'], 'Population': [1000, 350, 250]})",
        "hint": "set_index() 메서드를 사용하세요.",
        "solution": "df = df.set_index('City')\nprint(df)",
        "explanation": "특정 컬럼을 조회나 병합의 키(Key)로 사용하고 싶을 때 인덱스로 변환합니다."
    },
    {
        "title": "문제 19: 문자열 포함 여부 필터링",
        "desc": "'Text' 컬럼에서 'Python' 또는 'R'을 포함하는 행을 찾으시오.",
        "setup": "df = pd.DataFrame({'Text': ['I love Python', 'I love SQL', 'I love R', 'I love Java']})",
        "hint": ".str.contains()와 'Python|R' 패턴을 사용하세요.",
        "solution": "filtered = df[df['Text'].str.contains('Python|R')]\nprint(filtered)",
        "explanation": "정규표현식의 파이프(|) 기호는 **OR 연산**을 수행합니다."
    },
    {
        "title": "문제 20: 다중 조건 정렬",
        "desc": "'Sales'는 내림차순, 'Profit'은 오름차순으로 정렬하시오.",
        "setup": "df = pd.DataFrame({'Sales': [100, 100, 50, 200], 'Profit': [10, 5, 20, 15]})",
        "hint": "sort_values()의 ascending 인자에 리스트를 전달하세요.",
        "solution": "sorted_df = df.sort_values(by=['Sales', 'Profit'], ascending=[False, True])\nprint(sorted_df)",
        "explanation": "여러 컬럼을 기준으로 정렬할 때 각각의 정렬 방향을 다르게 지정할 수 있습니다."
    }
]

# [셀 생성 루프]
for i, problem in enumerate(problems):
    # 1. 문제 설명 (Markdown) - 정답은 <details> 태그로 숨김 처리
    # 배경 흰색(#ffffff) 적용을 위해 style="background-color: #ffffff;" 추가
    markdown_content = f"""### {problem['title']}
{problem['desc']}

> **힌트:** {problem['hint']}

<details style="background-color: #ffffff;">
<summary><strong>👉 정답 및 해설 보기 (클릭)</strong></summary>

```python
{problem['solution']}