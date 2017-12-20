from typing import List, Dict
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

def check_in_dict_failback(key: any, dict_: Dict[any, any], failback: any=None):
    if key in dict_:
        return dict_[key]
    return failback
