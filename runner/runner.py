import argparse
import sys

parse = argparse.ArgumentParser()
parse.add_argument("file", help="the compiled file, must be encoded")
args = parse.parse_args()

try:
    compiled = open(args.file, "r")
    lines: list = compiled.readlines()

    for line in lines:
        kw = line.split(" ")
        l1 = 2
        number = 0b00000000 # P works in 1 byte every number of bits
        RAMA = []
        SETV = number
        act = ""
        for i, k in enumerate(kw):
            if i % 2 == 1: # 2 % 2 != 0 so then ins't a keyword; 4 % 2 == 0 so then it's a keyword
                number = int(k, base=2)
                if act == "SET":
                    SETV = number
                if act == "RAM":
                    print(RAMA[0])
                if act == "PUT":
                    print(SETV)
                if act == "EXIT":
                    sys.exit(0)
                if act == "GET":
                    print(RAMA[number])
                if act == "oRAM":
                    RAMA.pop(int(number))
            else:
                act = k
except:
    print("Error")
    sys.exit(1)
