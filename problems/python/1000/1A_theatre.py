import sys

input = sys.stdin.readline

def main():
    a, b, c = map(int, input().split())

    rows = a // c + (1 if a % c != 0 else 0)
    cols = b // c + (1 if b % c != 0 else 0)

    print(rows * cols)
if __name__ == "__main__":
    main()