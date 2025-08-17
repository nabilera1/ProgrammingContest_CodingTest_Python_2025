# N = 3
#
# shallow  = [[0]*3]*N
# shallow[0][0] = 1
# shallow[1][1] = 2
# print("shallow =", shallow)
#
# deep = [[0]*3 for _ in range(N)]
# deep[0][0] = 1
# deep[1][1] = 2
# print("deep =", deep)

'''
shallow = [[1, 2, 0], [1, 2, 0], [1, 2, 0]]
deep = [[1, 0, 0], [0, 2, 0], [0, 0, 0]]
'''


# demo_shallow_vs_listcomp.py
# N=4, 각 행 길이=3 예시

def show(title, dp):
    print("\n" + "="*70)
    print(title)
    print("- pointer map (row object ids are shown to reveal aliasing) -")
    for i, row in enumerate(dp):
        print(f"dp[{i}] -> id={id(row)}  {row}")
    uniq = {id(r) for r in dp}
    print(f"unique row ids: {len(uniq)}  ({'ALL SAME' if len(uniq)==1 else 'ALL DIFFERENT'})")
    print("="*70 + "\n")

def demo_case(label, dp):
    show(f"{label} : BEFORE mutate", dp)
    print("mutate: dp[0][0] = 1\n")
    dp[0][0] = 1
    show(f"{label} : AFTER  mutate", dp)

def main():
    N, W = 4, 3

    # Case A) 얕은 복사 패턴: 같은 행(list) 객체를 N번 참조
    dp_bad  = [[0]*W]*N
    demo_case("Case A  [[0]*3]*N (shallow / shared rows)", dp_bad)

    # Case B) 리스트 내포: 매 행을 새 리스트로 생성 (독립)
    dp_good = [[0]*W for _ in range(N)]
    demo_case("Case B  [[0]*3 for _ in range(N)] (independent rows)", dp_good)

    # ASCII 요약
    print("\nASCII summary")
    print(r"""
Case A) [[0]*3]*N     (shallow)
dp[0]   \
dp[1] ---+--> row*  [1, 0, 0]   <-- all rows point to the SAME inner list
dp[2]   /
dp[3]  /
(print shows identical row ids)

Case B) [[0]*3 for _ in range(N)]   (independent)
dp[0] --> rowA [1, 0, 0]
dp[1] --> rowB [0, 0, 0]
dp[2] --> rowC [0, 0, 0]
dp[3] --> rowD [0, 0, 0]
(print shows different row ids)
""")

if __name__ == "__main__":
    main()
