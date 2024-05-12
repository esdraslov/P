import argparse
import sys

parse = argparse.ArgumentParser()
parse.add_argument("file", help="the compiled file, must be encoded") # must NOT be encoded
args = parse.parse_args()

try:
    compiled = open(args.file, "r")
    lines: list = compiled.readlines()
    E = False

    INLOOP = False # The variable to check if it's in a loop or not
    INIF = False  # The variable used to check if it's in a IF/ELSe 
    LOOPOINT = 0 # the start of a loop
    for i, line in enumerate(lines):
        kw = line.split(" ") # Every single keyword
        number = 0b00000000 # P works in 1 byte every number of bits
        RAMA = [] # RAM (arrays is the RAM, because array is directed separeted in RAM)
        SETV = number # Number for some actions (multi-parameters)
        PNTV = "" # The pointer of SETV, RAMA or themself
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
                    if INLOOP:
                        INLOOP = False # Exit of the loop
                    if INIF:
                        INIF = False # Exit of the if
                    if not INIF or not INLOOP:
                        sys.exit(0) # Exit of the program
                    if number != 0:
                        sys.exit(1) # Exit of the program, with error
                elif act == "GET":
                    if number >= len(RAMA): # Check if is out of index
                        print("Error [P::RAMIndex]: out of index")
                        E = True
                        sys.exit(1)
                    else:
                        print(RAMA[number]) # print an integer from RAM (broken)
                elif act == "oRAM":
                    RAMA.pop(int(number)) # remove an integer from RAM
                elif act == "PNT":
                    if SETV == 0b00000000:
                        PNTV = "" # Point to themself
                    elif SETV == 0b00000001:
                        PNTV = "RAMA" # Point to RAMA
                    else:
                        PNTV = "SETV" # Point to SETV
                elif act == "sPNT":
                    if PNTV == "RAMA":
                        RAMA.insert(number, SETV)
                    if PNTV == "SETV":
                        SETV = number
                    if PNTV == "":
                        PNTV == number
                elif act == "kPNT":
                    PNTV = number
                elif act == "LOOP":
                    INLOOP =  True
                    LOOPOINT = i
                    if number > 5:
                        i -= 1 # start loop from back to simple make a bigger loop
                elif act == "RESETTO":
                    if number == 0 and INLOOP:
                        i = LOOPOINT
                else:
                    raise Exception(f"Unknown action [{act}], please check the code and try again, remember, all actions is uppercase written")
            else:
                act = k
except Exception as error:
    if not E:
        print("Error [P::Exeception]: %s" % error)
    sys.exit(1)
except:
    if not E:
        print("Error [P::UnknownOrKnown]")
    sys.exit(1)
