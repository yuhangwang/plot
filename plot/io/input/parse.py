"""
Parse the user input configuration file,
update the default configuration dictionary
with the user-defined values and
return the updated dictionary.
"""
from typing import Dict, AnyStr
from .parser import parser
from .readAll import readAll
from ... import tk


def parse(user_config_file, default_config_file):
    # type: (AnyStr, AnyStr) -> (Dict)
    """Return an updated configuration file

    Read a user configuration file and
    a default configuration file.
    Use the values in the user configuration
    file to update the default configuration file.
    Finally return an updated configuration dictionary.

    Args:
        user_config_file (str): user configuration file

    Returns:
        an updated configuration dictionary
    """
    fn_parser1 = parser(user_config_file)
    fn_parser2 = parser(default_config_file)
    updated_dict = tk.dictTK.update(
            fn_parser1(readAll(user_config_file)),
            fn_parser2(readAll(default_config_file))
        )
    return tk.dictTK.convert_to_internal(updated_dict)
