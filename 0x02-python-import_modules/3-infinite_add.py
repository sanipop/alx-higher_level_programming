#!/usr/bin/python3
if __name__ == "__main__":
    import sys, math
    answer = 0
    for i in sys.argv:
        answer += int(i)
        print("{}".format(answer))
