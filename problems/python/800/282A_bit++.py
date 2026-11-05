import sys
 
input = sys.stdin.readline
 
def main():
    n = int(input())
    counter = 0
    for _ in range(n):
        a = input().strip()
        if a == "++X" or a == "X++":
            counter += 1
        elif a == "--X" or a == "X--":
            counter -= 1
    print(counter)
main()