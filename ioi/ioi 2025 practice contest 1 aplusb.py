# https://ioi2025.bo/tasks

'''
The IOI 2025 tasks are published under the Creative Commons Attribution license (CC-BY) license.

Practice Contest
aplusb (A + B Queries)
Statement: Official English
Test data and supplementary material


3
2 1 3
0 7 8
2
0 1
2 2
출력:
9
11

'''

# from typing import List
#
# # 전역으로 보관(채점기/드라이버가 함수만 호출한다고 가정)
# _A: List[int] = []
# _B: List[int] = []
#
# def initialize(A: List[int], B: List[int]) -> None:
#     """
#     케추아 사람들이 준 두 배열을 저장.
#     호출: 각 테스트케이스마다 정확히 1번
#     시간복잡도: O(N)
#     """
#     global _A, _B
#     _A = A
#     _B = B
#
# def answer_question(i: int, j: int) -> int:
#     """
#     질의 (i, j)에 대해 A[i] + B[j]를 반환.
#     호출: 총 Q번
#     시간복잡도: O(1)
#     """
#     return _A[i] + _B[j]

#
# import sys
#
# def initialize(A, B):
#     # 필요 시 전처리 가능하지만, 이 문제는 저장만 하면 됨.
#     return A, B
#
# def answer_question(A, B, i, j):
#     return A[i] + B[j]
#
# def main():
#     data = sys.stdin.read().strip().split() #ctrl + D, EOF 입력까지
#     it = iter(data)
#
#     N = int(next(it))
#     A = [int(next(it)) for _ in range(N)]
#     B = [int(next(it)) for _ in range(N)]
#
#     A, B = initialize(A, B)
#
#     Q = int(next(it))
#     out_lines = []
#     for _ in range(Q):
#         i = int(next(it))
#         j = int(next(it))
#         out_lines.append(str(answer_question(A, B, i, j)))
#
#     sys.stdout.write("\n".join(out_lines))
#
# if __name__ == "__main__":
#     main()


arrA = []
arrB = []
def initialize(A, B):
    global arrA, arrB
    arrA = A
    arrB = B

def answer_question(i, j):
    return arrA[i] + arrB[j]

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    initialize(A, B)

    Q = int(input())
    ans = []
    for _ in range(Q):
        i, j = map(int, input().split())
        ans.append(answer_question(i, j))
    print(ans)
    print('\n'.join(map(str,ans)))