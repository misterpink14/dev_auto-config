from json import load
from typing import Dict, List

class BrewConfig:
    def __init__(self, dependencies, taps, casks):
        self.dependencies = dependencies
        self.taps = taps
        self.casks = casks

        
class Config:
    FILE = "./config.json"

    def __init__(self, 
            templates: List[str or Dict[str, str or List[str]]], 
            dependencies: List[str or Dict[str, str or List[str]]],
            homebrew: BrewConfig):
        self.templates = templates
        self.dependencies = dependencies
        self.homebrew = homebrew

    @staticmethod
    def load():
        config = None
        with open(Config.FILE) as f:
            json_config = load(f)
            config = Config(
                json_config['templates'],
                json_config['dependencies'],
                json_config['homebrew'])
        return config


