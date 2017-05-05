#/usr/local/bin/python3
'''
TODO:
    [] neovim should be installed if needed
    [] add comments
    [] clean up a bit
    [] additional plugin requirements
'''

import os

def setup_neovim():
    user_home = os.path.expanduser("~")
    neovim_init_out = user_home + "/.config/nvim/init.vim"
    neovim_init_in = "./init.vim"
    os.makedirs(os.path.dirname(neovim_init_out), exist_ok=True)
    with open(neovim_init_in, "r") as fi:
        with open(neovim_init_out, "w") as fo:
            fo.write(fi.read())
    



setup_neovim()
print("dun")



