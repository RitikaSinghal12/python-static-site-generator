import pathlib
from typing import List
from pathlib import Path
import shutil

class Parser:

    extensions: List[str] = []

    def valid_extension(self, extension):
        if extension in self.extensions:
            return True
        return False
    
    def parse(self, path, source, dest):
        raise NotImplementedError

    def read(self, path):
        with open(path, mode='rt') as f:
            return f

    def write(self, path, dest, content, ext=".html"):
        full_path = self.dest / path.with_suffix(ext).name
        with open(full_path, mode='wt') as file:
            file.write(content)

    def copy(self, path, source, dest):
        shutil.copy2(path, dest / path.relative_to(source))
    


class ResourceParser(Parser):
    extensions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self, path, source, dest):
        super().copy(path, source, dest)
        return super().parse(path, source, dest)

