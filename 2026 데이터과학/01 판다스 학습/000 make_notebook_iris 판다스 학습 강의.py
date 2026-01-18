import json

# 노트북 구조 생성 (메타데이터 및 셀 포함)
notebook_content = {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 🐼 판다스(Pandas) 입문 : 붓꽃 데이터 분석하기\n",
    "\n",
    "안녕하세요! 오늘은 데이터 과학자들의 필수 도구인 **판다스(Pandas)**를 배워보겠습니다.\n",
    "유명한 **'붓꽃(Iris)'** 데이터를 요리조리 다뤄보면서 데이터 분석의 기초를 다져봅시다.\n",
    "\n",
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1차시: 데이터의 집, 데이터프레임(DataFrame) 입주하기\n",
    "\n",
    "> **🕵️‍♀️ 상황 설정:** 여러분이 식물학자가 되어 미지의 섬에 갔습니다. 수첩 대신 파이썬으로 꽃 데이터를 불러와 볼까요?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from sklearn.datasets import load_iris\n",
    "\n",
    "# 1. 사이킷런에서 데이터 로딩\n",
    "iris = load_iris()\n",
    "\n",
    "# 2. 데이터프레임 생성 (데이터와 컬럼명 연결)\n",
    "df = pd.DataFrame(data=iris.data, columns=iris.feature_names)\n",
    "\n",
    "# 3. 품종(Target) 정보 추가 (0, 1, 2로 되어있음)\n",
    "df['species_code'] = iris.target\n",
    "\n",
    "print(\"데이터프레임 생성 완료!\")\n",
    "df  # 데이터의 내용 확인"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2차시: 데이터 훑어보기 (탐색적 데이터 분석 기초)\n",
    "\n",
    "> **🩺 상황 설정:** 의사가 환자를 진찰하듯, 데이터의 건강 상태를 체크해봅시다. 빈 값은 없는지, 숫자가 이상하진 않은지 확인합니다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. 상위 5개 행만 살짝 보기\n",
    "print(\"--- 앞부분(Head) ---\")\n",
    "display(df.head())\n",
    "\n",
    "# 2. 데이터 요약 정보 (행 개수, 빈 값 유무, 데이터 타입)\n",
    "print(\"\\n--- 정보(Info) ---\")\n",
    "print(df.info())\n",
    "\n",
    "# 3. 통계적 요약 (평균, 표준편차, 최소/최대값)\n",
    "print(\"\\n--- 통계 요약(Describe) ---\")\n",
    "display(df.describe())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3차시: 원하는 데이터만 쏙! (인덱싱과 슬라이싱)\n",
    "\n",
    "> **✂️ 상황 설정:** \"나는 꽃잎 정보는 필요 없고, 오직 '꽃받침(Sepal)' 정보만 보고 싶어!\" 원하는 부분만 오려내 봅시다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. 하나의 열만 선택 (Series 반환)\n",
    "sepal_length = df['sepal length (cm)']\n",
    "print(\"꽃받침 길이 열:\")\n",
    "print(sepal_length.head())\n",
    "\n",
    "# 2. 여러 열 선택\n",
    "subset = df[['sepal length (cm)', 'species_code']]\n",
    "print(\"\\n두 개 열만 선택:\")\n",
    "display(subset.head())\n",
    "\n",
    "# 3. 행 선택 (iloc: 순서/인덱스 기준)\n",
    "print(\"\\n5번째 행 데이터(iloc):\")\n",
    "print(df.iloc[5])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 4차시: 데이터 탐정 되어보기 (조건 필터링과 정렬)\n",
    "\n",
    "> **🔎 상황 설정:** 상사 왈, \"꽃받침 길이가 7cm 이상인 '대왕 붓꽃'만 찾아와!\" 판다스에게 조건을 걸어봅시다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. 조건 필터링 (꽃받침 길이가 7.0보다 큰 데이터)\n",
    "large_flowers = df[df['sepal length (cm)'] > 7.0]\n",
    "\n",
    "print(f\"7cm보다 큰 꽃은 총 {len(large_flowers)}송이 입니다.\")\n",
    "display(large_flowers.head())\n",
    "\n",
    "# 2. 정렬하기 (꽃잎 너비가 넓은 순서대로 내림차순)\n",
    "sorted_df = df.sort_values(by='petal width (cm)', ascending=False)\n",
    "\n",
    "print(\"\\n꽃잎이 가장 넓은 꽃 Top 5:\")\n",
    "display(sorted_df.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 5차시: 그룹으로 묶어 통찰력 얻기 (그룹화와 통계)\n",
    "\n",
    "> **📊 상황 설정:** 품종별(0, 1, 2)로 특징이 다를까요? 그룹을 지어 평균을 비교해 봅시다. 이것이 머신러닝의 기초입니다!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 0, 1, 2로 된 코드를 실제 이름으로 매핑 (더 보기 좋게)\n",
    "species_map = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}\n",
    "df['species_name'] = df['species_code'].map(species_map)\n",
    "\n",
    "# 1. 품종별로 그룹화하여 평균 구하기\n",
    "group_mean = df.groupby('species_name').mean()\n",
    "\n",
    "print(\"--- 품종별 평균 데이터 ---\")\n",
    "display(group_mean)\n",
    "\n",
    "# 해석: virginica 품종이 꽃잎(petal) 길이와 너비가 가장 크다는 것을 알 수 있습니다."
   ]
  }
 ],
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

# 파일 쓰기
file_name = "pandas_iris_lesson.ipynb"
with open(file_name, 'w', encoding='utf-8') as f:
    json.dump(notebook_content, f, indent=1, ensure_ascii=False)

print(f"✅ '{file_name}' 파일이 성공적으로 생성되었습니다!")