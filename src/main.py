"""
Plot executable
AUTHOR: YUHANG(STEVEN) WANG
DATE: 10-11-2016
Usage: plot my.json 
    or plot my.yaml
"""
import sys
import re
import os
from mpa import plot
import mpa.mpa_toolkit as MpaTK

def parse(user_config_file):
    if re.match(".*\.json", user_config_file):
        import json
        parser = json.loads
    elif re.match(".*\.yaml", user_config_file):
        import yaml
        parser = yaml.load
    else:
        return dict()

    with open(user_config_file, "r") as IN:
            return MpaTK.lowercase_keys(parser(IN.read()))

def main():
    user_config_file = sys.argv[1]
    if len(sys.argv) > 2 and sys.argv[2] == "--no-preview":
        preview = False
    else:
        preview = True

    user_config_dict = parse(user_config_file)
    if len(user_config_dict.keys()) == 0:
    	print("ERROR HINT: invalid input configuration file {}".format(user_config_file))
    	exit()
    plot(user_config_dict, preview)
