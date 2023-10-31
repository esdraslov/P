import argparse

parse = argparse.ArgumentParser()
parse.add_argument("file", help="the compiled file, must be encoded")
args = parse.parse_args()

try:
    compiled = open(args.file, "r")
    lines: list = compiled.readlines()

    for line in lines:
        pass
except:
    print("a error happens while uncoding the file")
finally:
    print("the action/program ended")
