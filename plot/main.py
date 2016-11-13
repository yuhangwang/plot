"""
Plot executable
AUTHOR: YUHANG(STEVEN) WANG
DATE: 13-11-2016
Usage: plot my.json  or plot my.yaml
"""
import sys
from plot.io.input import parse
from plot.run import run


def main():
    user_config_file = sys.argv[1]
    if len(sys.argv) > 2 and sys.argv[2] == "--no-preview":
        preview = False
    else:
        preview = True

    params = parse(user_config_file)
    if len(params.keys()) == 0:
        print(
            "ERROR HINT: invalid input "
            "configuration file {}".format(user_config_file)
            )
        exit()
    run(params, preview)
