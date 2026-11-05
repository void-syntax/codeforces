import sys
 
input = sys.stdin.readline
 
def main():
    t = int(input())
    lst = []                      # создаём один раз, до цикла
    for _ in range(t):
        n = int(input())
        s = input().strip()
        seen = set()              # а это должно быть внутри, для каждого теста своё
        counter = 0
        for ch in s:
            if ch in seen:
                counter += 1
            else:
                counter += 2
                seen.add(ch)
        lst.append(counter)
 
    for val in lst:
        print(val)
 
main()