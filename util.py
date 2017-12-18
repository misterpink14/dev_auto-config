from typing import List
from types import FunctionType

def get_command(cmd):
    if type(cmd) == List[str]:
        return " && ".join(cmd)
    return cmd

def as_list_or_expected(val: List[any] or any, action: FunctionType):
    if isinstance(template_config, List):
        as_list(val, action)
    action(val)

def as_list(list_: List[any], action: FunctionType):
    for item in list_:
        action(item)
