import sys
input = sys.stdin.readline

def main():

    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        best = 0
        cur = 0
        for x in a:
            if x == 0:
                cur += 1
                best = max(best, cur)
            else:
                cur = 0
        print(best)
main()