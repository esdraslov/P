import argparse

parse = argparse.ArgumentParser()
parse.add_argument('file', help='the file name')
args = parse.parse_args()
fn = args.file

try:
    f = open(fn, "r")
except:
    print("the file doens't exist in local")