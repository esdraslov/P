import argparse

parse = argparse.ArgumentParser()
action_help = """
commands:\n
 install - install a feature\n
 upgrade - install a upgrade for a feature\n
"""
action = parse.add_argument('action', help=action_help)
package = parse.add_argument('package', help="the package to be installed")
args = parse.parse_args()