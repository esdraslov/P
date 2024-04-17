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
        for i, k in enumerate(kw):
            if i % 2 == 1: # 2 % 2 != 0 so then ins't a keyword; 4 % 2 == 0 so then it's a keyword
                number = int(k, base=2)
            else:
                if k == "SET":
                    SETV = number
                if k == "RAM":
                    RAMA.append(number)
                if k == "PUT":
                    print(SETV)
                if k == "EXIT":
                    sys.exit(0)
                if k == "GET":
                    print(RAMA[int(number, base=0)])
                if k == "oRAM":
                    RAMA.pop(int(number, base=0))
except:
    print("a error happens while uncoding the file")
finally:
    print("the action/program ended")
