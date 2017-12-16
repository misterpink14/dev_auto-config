from typing import List

def get_command(cmd):
    if type(cmd) == List[str]:
        return " && ".join(cmd)
    return cmd
