import json

# 노트북 구조 정의
notebook_content = {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# [실습] 파이썬 문자열 핵심 메서드 10제\n",
    "\n",
    "앞서 학습한 문자열의 주요 기능들을 복습하는 시간입니다.\n",
    "각 문제의 주석(**TODO**) 아래에 코드를 작성하여 문제를 해결해 보세요.\n",
    "\n",
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Q1. 문자열 슬라이싱\n",
    "주민등록번호 `990120-1234567`에서 생년월일(`990120`)만 추출하여 출력하세요."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "jumin = \"990120-1234567\"\n",
    "\n",
    "# TODO: 생년월일 추출\n",
    "birth_date = \n",
    "print(birth_date)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Q2. 소문자 변환 및 공백 제거\n",
    "사용자가 입력한 아이디 `  PytHoNUser  `를 처리하기 쉽도록 **양쪽 공백을 제거**하고 **모두 소문자**로 변환하세요."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "user_id = \"  PytHoNUser  \"\n",
    "\n",
    "# TODO: 공백 제거 및 소문자 변환\n",
    "clean_id = \n",
    "print(clean_id)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Q3. 문자열 교체 (비밀번호 가리기)\n",
    "전화번호 `010-1234-5678`의 가운데 자리 `1234`를 `****`로 변경하여 출력하세요. (`replace` 사용)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "phone = \"010-1234-5678\"\n",
    "\n",
    "# TODO: 가운데 번호 마스킹\n",
    "secure_phone = \n",
    "print(secure_phone)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Q4. 문자열 분리 (Split)\n",
    "태그들이 하나의 문자열 `python,coding,test`로 묶여 있습니다. 콤마(`,`)를 기준으로 나누어 리스트 형태로 만드세요."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "tags = \"python,coding,test\"\n",
    "\n",
    "# TODO: 콤마 기준 분리\n",
    "tag_list = \n",
    "print(tag_list)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Q5. 문자열 합치기 (Join)\n",
    "리스트 `['2023', '12', '25']`에 들어있는 날짜 정보를 하이픈(`-`)으로 연결하여 `2023-12-25` 형태의 문자열로 만드세요."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "date_parts = ['2023', '12', '25']\n",
    "\n",
    "# TODO: 하이픈으로 연결\n",
    "full_date = \n",
    "print(full_date)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Q6. 특정 단어 개수 세기 (Count)\n",
    "문장 `\"tomato spaghetti is made of tomato\"`에서 `tomato`라는 단어가 몇 번 등장하는지 세어보세요."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "sentence = \"tomato spaghetti is made of tomato\"\n",
    "\n",
    "# TODO: tomato 개수 확인\n",
    "count = \n",
    "print(count)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Q7. 파일 확장자 확인 (Endswith)\n",
    "파일 이름 리스트에서 `.png`로 끝나는 이미지 파일만 찾아서 출력하세요.\n",
    "파일 리스트: `['report.doc', 'profile.png', 'data.csv', 'icon.png']`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "files = ['report.doc', 'profile.png', 'data.csv', 'icon.png']\n",
    "\n",
    "for file in files:\n",
    "    # TODO: .png로 끝나는지 확인\n",
    "    if :\n",
    "        print(file)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Q8. 위치 찾기 (Find)\n",
    "이메일 주소 `admin@google.com`에서 `@` 기호가 몇 번째 인덱스에 있는지 찾으세요."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "email = \"admin@google.com\"\n",
    "\n",
    "# TODO: @ 위치 찾기\n",
    "at_index = \n",
    "print(at_index)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Q9. f-string 포매팅\n",
    "변수 `name=\"철수\"`, `age=20`을 사용하여 `\"제 이름은 철수이고, 20살입니다.\"`라는 문자열을 출력하세요."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "name = \"철수\"\n",
    "age = 20\n",
    "\n",
    "# TODO: f-string 사용\n",
    "intro = \n",
    "print(intro)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Q10. 종합 응용 (체이닝)\n",
    "지저분한 데이터 `\"  $5,000  \"`를 받았습니다. \n",
    "1. 양쪽 공백 제거\n",
    "2. `$` 기호 제거\n",
    "3. `,` 콤마 제거\n",
    "위 과정을 거쳐 숫자 `5000` (문자열 상태)만 남겨 출력하세요. (메서드 체이닝을 활용해보세요)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "raw_price = \"  $5,000  \"\n",
    "\n",
    "# TODO: 메서드 체이닝으로 정제\n",
    "clean_price = \n",
    "print(clean_price)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "--- \n",
    "## 💡 정답 (스스로 푼 뒤 확인하세요)\n",
    "\n",
    "1. `jumin[:6]`\n",
    "2. `user_id.strip().lower()`\n",
    "3. `phone.replace(\"1234\", \"****\")`\n",
    "4. `tags.split(\",\")`\n",
    "5. `\"-\".join(date_parts)`\n",
    "6. `sentence.count(\"tomato\")`\n",
    "7. `if file.endswith(\".png\"):`\n",
    "8. `email.find(\"@\")`\n",
    "9. `f\"제 이름은 {name}이고, {age}살입니다.\"`\n",
    "10. `raw_price.strip().replace(\"$\", \"\").replace(\",\", \"\")`"
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

# 파일 저장
file_name = "002 학습자료 문자열 메서드 python_string_workbook.ipynb"
with open(file_name, 'w', encoding='utf-8') as f:
    json.dump(notebook_content, f, ensure_ascii=False, indent=2)

print(f"{file_name} 파일이 성공적으로 생성되었습니다!")