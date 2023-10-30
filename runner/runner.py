import argparse

parse = argparse.ArgumentParser()
parse.add_argument("file", help="the compiled file, must be encoded")
args = parse.parse_args()

try:
    compiled = open(args.file, "w")
except:
    print("a error happens while uncoding the file")
finally:
    print("the action/program ended")
