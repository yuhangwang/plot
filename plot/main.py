"""
Plot executable
AUTHOR: YUHANG(STEVEN) WANG
DATE: 13-11-2016
Usage: plot my.json  or plot my.yaml
"""
import sys
import os
from plot.io.input import parse
from plot.run import run


def main():
    user_config_file = sys.argv[1]

    if len(sys.argv) > 2 and sys.argv[2] == "--no-preview":
        preview = False
    else:
        preview = True

    here = os.path.dirname(os.path.realpath(__file__))
    default_config_file = os.path.join(here, "parameter", "all.json")
    params = parse(user_config_file, default_config_file)
    
    if len(params.keys()) == 0:
        raise Exception(
            "ERROR HINT: invalid input "
            "configuration file {}".format(user_config_file)
            )
        exit()
        
    run(params, preview)
