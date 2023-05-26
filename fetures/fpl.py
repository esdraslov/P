import argparse

parse = argparse.ArgumentParser()
action_help = """
commands:\n
-i install - install a feture\n
-u upgrade - install a upgrade for a feture\n
"""
action = parse.add_argument('action', help=action_help)
args = parse.parse_args()