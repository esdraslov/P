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
                    print(RAMA[int(number)])
                if k == "oRAM":
                    RAMA.pop(int(number))
except Exception as e:
    raise f"P: [Expection] Exception: {e}"
except TypeError as te:
    raise f"P: [TypeError] TypeError: {te}"
except EOFError as eofe:
    raise f"P: [EOFError] Exception: {eofe}"
except:
    raise "P: [Unknow exception] Unknow: Check your code, just it is possible to fix"
