path = './beatles.png'

from PIL import Image

# 1) 이미지 파일 열기
img = Image.open(path)

# 2) 이미지 정보 확인
print(img.format)   # PNG
print(img.size)     # (가로, 세로)
print(img.mode)     # RGB

# 3) 이미지 화면에 표시
img.show()