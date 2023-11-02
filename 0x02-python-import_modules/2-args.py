#!/usr/bin/python3
if __name__ == "__main__":
    import sys
   lengh = len(sys.argv)
    if lengh == 1:
        print("{} arguments.".format(lengh - 1))
    elif lengh == 2:
        print("{} argument:".format(lengh - 1))
    else:
        print("{} arguments:".format(lengh - 1))
    for i in range(1, lengh):
        print("{}: {}".format(i, sys.argv[i]))
