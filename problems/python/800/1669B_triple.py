import sys

input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        cnt = {}
        ans = -1
        for x in a:
            cnt[x] = cnt.get(x, 0) + 1
            if cnt[x] >= 3:
                ans = x
                break
        print(ans)

if __name__ == "__main__":
    main()