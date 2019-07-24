from json import load

from os import listdir
from os.path import isfile, join

from typing import Dict, List

class Config:
    PATH = "./configs/"

    def __init__(self,
            templates: List[str or Dict[str, str or List[str]]], 
            dependencies: List[str or Dict[str, str or List[str]]],
            homebrew: Dict[str, List[str or Dict[str, str]]]):
        self.templates = templates
        self.dependencies = dependencies
        self.homebrew = homebrew

    @staticmethod
    def load_configs():
        configs = {}
        for filename in listdir(Config.PATH):
            filepath = join(Config.PATH, filename)
            if isfile(filepath):
                group_parts = filename.split("_")
                group_parts.pop(-1)
                if not group_parts:
                    group = "default"
                else:
                    group = '_'.join(group_parts)
                with open(filepath) as f:
                    json_config = load(f)
                    configs[group] = Config(
                            json_config['templates'],
                            json_config['dependencies'],
                            json_config['homebrew'])
        return configs

