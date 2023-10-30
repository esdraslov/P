import argparse

parse = argparse.ArgumentParser()
parse.add_argument('file', help='the file name')
args = parse.parse_args()
fn = args.file

try:
    f = open(fn, "r")
    new_f = open("compiled.pc", "w")
    text: str = f.read()
    new_f.write(text)
except:
    print("the file doens't exist in local")
