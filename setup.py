#/usr/local/bin/python3
'''
TODO:
    [] add comments
    [] clean up a bit
    [] add a check for vim-plug
    [] additional plugin requirements
'''

import os
import subprocess

def is_installed(product):
    return subprocess.call(["which", product]) == 0

def has_neovim():
    """Checks to see if nvim is installed
    """
    return is_installed("nvim")

def has_brew():
    """
    """
    return is_installed("brew")

def install_brew():
    subprocess.call(["/usr/bin/ruby", "-e", "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"])

def install_neovim():
    """Installs neovim
    """
    subprocess.call(["brew", "install", "neovim/neovim/neovim"])
    #subprocess.call(["brew", "install", "ripgrep"])

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

def update_brew():
    """Update homebrew and formulas
    """
    subprocess.call(["brew", "update"])
    subprocess.call(["brew", "upgrade"])

def update_installed():
	subprocess.call(["pip3", "install", "--upgrade", "neovim"])

def install_python_dependencies():
    """
    """
    subprocess.call(["pip3", "install", "neovim"]) # deoplete dependency
    subprocess.call(["pip2", "install", "--user", "neovim"])
    subprocess.call(["pip3", "install", "--user", "neovim"])

def main():
    """Updates nvim config file, installs nvim if it hasn't been yet
    """
    if has_brew():
        update_brew()
    else:
        install_brew()
    if not has_neovim():
        print("Installing NeoVim")
        install_neovim()
        print("Installing vim-plug")
        install_vimplug()
        install_python_dependencies()
    update_installed()
    print("Setting up NeoVim")
    setup_neovim()
    print("dun")


if __name__ == "__main__":
    main()

