import argparse
import sys

parse = argparse.ArgumentParser()
parse.add_argument("file", help="the compiled file, must be encoded") # must NOT be encoded
args = parse.parse_args()

try:
    compiled = open(args.file, "r")
    lines: list = compiled.readlines()

    for line in lines:
        kw = line.split(" ") # Every single keyword
        number = 0b00000000 # P works in 1 byte every number of bits
        RAMA = [] # RAM (arrays is the RAM, because array is directed separeted in RAM)
        SETV = number # Number for some actions (multi-parameters)
        act = "" # action
        for i, k in enumerate(kw):
            if i % 2 == 1: # 2 % 2 != 0 so then ins't a keyword; 4 % 2 == 0 so then it's a keyword
                number = int(k, base=2) # the number passed as parameter
                if act == "SET":
                    SETV = number # set a number for some actions
                elif act == "RAM":
                    RAMA.append(number) # add number to RAM
                elif act == "PUT":
                    print(SETV) # Aways need to be 00000000 (0) bits as parameter
                elif act == "EXIT":
                    sys.exit(0) # Exit successfully
                elif act == "GET":
                    print(RAMA[number]) # print an integer from RAM
                elif act == "oRAM":
                    RAMA.pop(int(number)) # remove an integer from RAM
                else:
                    raise Exception(f"Unknown action [{act}], please check the code and try again, remember, all actions is uppercase written")
            else:
                act = k
except Exception as error:
    print("Error [P::Exeception]: %s" % error)
    sys.exit(1)
except:
    print("Error [Unknown]")
    sys.exit(1)
