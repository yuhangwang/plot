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
    user_dict = tk.dictTK.wrap_value(fn_parser1(readAll(user_config_file)))
    default_dict = tk.dictTK.default(fn_parser2(readAll(default_config_file)))
    ooo = {}
    print(user_dict)
    def transform(d1, d2): 
        return tk.dictTK.convert_to_internal(
            tk.dictTK.update(d1, d2))

    for k in ['global', 'local', 'data']:
        if k in user_dict:
            if isinstance(user_dict[k]['v'], list):
                print(k, "is list")
                print(user_dict[k]['v'])
                print(user_dict[k]['v'][0])
                ooo[k] = [transform(user_dict[k]['v'][i], default_dict[k])
                          for i in range(len(user_dict[k]['v']))]
            else:
                print(k, "not a list")
                ooo[k] = transform(user_dict[k], default_dict[k])
        else:
            ooo[k] = tk.dictTK.convert_to_internal(default_dict[k])
    return ooo
