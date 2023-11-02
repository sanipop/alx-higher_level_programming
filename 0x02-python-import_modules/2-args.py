#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argLen = len(sys.argv)

    if argLen == 1:
        print("No arguments provided.")

    elif argLen == 2:
        print("One argument provided:")

    else:
        print("{} arguments provided:".format(argLen - 1))

    for i in range(1, argLen):
        print("Argument {}: {}".format(i, sys.argv[i]))
