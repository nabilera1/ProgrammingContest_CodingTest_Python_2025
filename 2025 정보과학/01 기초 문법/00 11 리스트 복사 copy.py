from copy import copy

# 원본 리스트
original_list = [1, 2, 3, 4, 5]

# 리스트 복사
copied_list = copy(original_list) #copy 모듈 사용
copied_list1 = original_list.copy() #리스트 타입의 내장 메서드 사용

# 복사된 리스트 출력
print("원본 리스트:", original_list)
print("복사된 리스트:", copied_list)
print("복사된 리스트1:", copied_list1)

copied_list[1] = 7

print(f'original_list : {original_list}')
print(f'copied_list : {copied_list}')
print(f'copied_list1 : {copied_list1}')

new_list = original_list
new_list[2] = 8
print(f'original_list : {original_list}')
print(f'new_list : {new_list}')
'''
원본 리스트: [1, 2, 3, 4, 5]
복사된 리스트: [1, 2, 3, 4, 5]
복사된 리스트1: [1, 2, 3, 4, 5]
original_list : [1, 2, 3, 4, 5]
copied_list : [1, 7, 3, 4, 5]
copied_list1 : [1, 2, 3, 4, 5]
'''