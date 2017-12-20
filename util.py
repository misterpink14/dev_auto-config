from typing import List, Dict
from types import FunctionType

def get_command(cmd):
    if type(cmd) == List[str]:
        return " && ".join(cmd)
    return cmd

def check_in_dict_failback(key: any, dict_: Dict[any, any], failback: any=None):
    if key in dict_:
        return dict_[key]
    return failback

def append_or_merge(list_: List[any], value: any or List[any]):
    if isinstance(value, List):
        return list_ + value
    list_.append(value)
    return list_
