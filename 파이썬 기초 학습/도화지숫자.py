#도화지 수 구하기
#색종이를 도화지에 붙이려고 한다.
#색종이 개수 n, 
#한 장의 도화지에 붙일 수 있는 색종이 수 m
#필요한 도화지 수를 구하라.
#20 7
#3
#17 8
#3
n, m=input().split()
n=int(n)
m=int(m)
page, r=divmod(n,m)#몫과 나머지
page+=bool(r)#r이 0이 아니면 1 증가
print(page)


