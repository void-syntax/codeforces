import sys

input = sys.stdin.readline

def main():
    s = input().strip()
    flag = False
    counterforrepeated = 0
    counterforrepeated1 = 0
    for ch in s:
        if ch == "1":
            counterforrepeated += 1
        else:
            counterforrepeated = 0

        if ch == "0":
            counterforrepeated1 += 1
        else:
            counterforrepeated1 = 0

        if counterforrepeated >= 7 or counterforrepeated1 >= 7:
            flag = True 
            break
        else:
            flag = False
    if flag:
        print("YES")
    else:
        print("NO")
main()
