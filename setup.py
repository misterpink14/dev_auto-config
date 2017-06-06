#/usr/local/bin/python3
'''
TODO:
    [] add comments
    [] clean up a bit
    [] add a check for vim-plug
    [] additional plugin requirements
    [] need to add pip install for neovim
pip2 install --user neovim
pip3 install --user neovim
    [] install homebrew
    [] install ripgrep
brew install ripgrep
'''

import os
import subprocess

def has_neovim():
    """Checks to see if nvim is installed
    """
    return subprocess.call(["which", "nvim"]) == 0

def install_neovim():
    """Installs neovim
    """
    subprocess.call(["brew", "install", "neovim/neovim/neovim"])

def setup_neovim():
    """Copys init.vim to nvim config folder
    """
    user_home = os.path.expanduser("~")
    neovim_init_out = user_home + "/.config/nvim/init.vim"
    neovim_init_in = "./init.vim"
    os.makedirs(os.path.dirname(neovim_init_out), exist_ok=True)
    with open(neovim_init_in, "r") as fi:
        with open(neovim_init_out, "w") as fo:
            fo.write(fi.read())

def install_vimplug():
    """Installs vim-plug
    """
    subprocess.call(["curl",
                     "-fLo",
                     "~/.local/share/nvim/site/autoload/plug.vim",
                     "--create-dirs",
                     "https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim"])

def main():
    """Updates nvim config file, installs nvim if it hasn't been yet
    """
    if not has_neovim():
        print("Installing NeoVim")
        install_neovim()
        print("Installing vim-plug")
        install_vimplug()
    print("Setting up NeoVim")
    setup_neovim()
    print("dun")


if __name__ == "__main__":
    main()

