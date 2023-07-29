import argparse

parse = argparse.ArgumentParser()
parse.add_argument('file', help='the file name')
args = parse.parse_args()
fn = args.file

try:
    f = open(fn, "r")
    new_f = open(fn.replace('.p', '.cs'), "w")
    text: str
    if f.readlines().__contains__('console.write'):
        text = f.readlines().replace('console.write','Console.Write')
    new_f.write(text)
except:
    print("the file doens't exist in local")
