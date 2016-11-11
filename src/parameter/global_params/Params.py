import os
import json

class GlobalParameters:
    """
    Provide a mapping dictionary from user keywords to internal keywords
    and a mapping from internal keywords to default values
    """

    def __init__(self):
        pwd = os.path.dirname(os.path.realpath(__file__))
        file = os.path.join(pwd, "db", "all.json")
        
        with open(file, "r") as IN:
            _params = json.loads(IN.read())

        self._convention_ = {}
        self._default_ = {}

        for k, v in _params.items():
            user_keyword = k
            internal_keyword = v[0]
            options = v[1]
            self._convention_[user_keyword] = internal_keyword
            self._default_[internal_keyword] = options[0]

    def get_convention(self):
        return self._convention_

    def get_default(self):
        return self._default_.copy()

