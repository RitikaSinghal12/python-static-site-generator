import re
from yaml import FullLoader,load
from collections.abc import Mapping

class Content(Mapping):
    __delimeter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimeter, re.MULTILINE)

    @classmethod
    def load(cls, string):
        _,fm, content= cls.__regex.split(string, 2)
        load(fm, Loader=FullLoader)
        return cls(metadata, content)

    def __init__(metadata, content):
        data = metadata
        self.data["content"] = content

