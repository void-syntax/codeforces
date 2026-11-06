import sys
 
input = sys.stdin.readline
 
def main():
    string = input()
    a = set(list(string))
    if len(a) % 2 == 1:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")
main()
