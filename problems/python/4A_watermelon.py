import sys
input = sys.stdin.read

def main():
    number = int(input().strip())
    if number % 2 == 0 and number > 2:
        print("YES")
    else:
        print("NO")
main()