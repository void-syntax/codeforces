import sys

input = sys.stdin.read

def main():
    a, b, c = map(int, input().split())
    
    square = a * b
    tile = c * c
    if square % tile == 0:
        print(square // tile)
    else:
        print(square // tile + 1)

if __name__ == "__main__":
    main()
