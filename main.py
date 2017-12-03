#/usr/local/bin/python3
'''
For setting up your development environment

TODO:
    [] Add these:
        [] https://github.com/Shougo/deoplete.nvim
        [] https://github.com/Shougo/dein.vim
        [] https://github.com/Shougo/denite.nvim
    [] add comments
    [] clean up a bit
    [] additional plugin requirements
    [] homebrew
    [] neovim
    [] dein
    [] bash_profile
    [] iterm
    [] ssh forwarding


definite must haves:
    brew
    neovim
'''

import os
import pwd
import subprocess
import argparse
import json
import logging

from string import Template

INSTALL_HOMEBREW = """/usr/bin/ruby -e $(curl -fsSL \
https://raw.githubusercontent.com/Homebrew/install/master/install)"""
UPDATE_HOMEBREW = "brew upgrade && brew upgrade"
INSTALL_NEOVIM = "brew install neovim/neovim/neovim"

CONFIG = {}


class Dependency():
    """Class for installing / updating dependencies"""
    def __init__(self, name: str, install_command: str, update_command: str, check_install_command: str=None):
        self.name = name
        self.install_command = install_command
        self.update_command = update_command
        self.check_install_command = check_install_command

    def _execute(self, command, command_verb):
        logging.info(' '.join([command_verb, self.name]))
        process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True) #TODO: learn how this works
        process.communicate()

    def install(self):
        self._execute(self.install_command, "installing")

    def update(self):
        self._execute(self.update_command, "updating")
    
    def is_installed(self):
        if self.check_install_command:
            return self._execute(self.check_install_command, "checking")
        elif self.name:
            return subprocess.call(["which", self.name]) == 0 # TODO: replace with _execute
        else:
            return False

class InitVim():

    def __init__(self):
        # TODO: move this into the config.ini
        self.userhome = os.path.expanduser("~")
        self.out_file = ''.join([self.userhome, "/",  CONFIG["paths"]["init.vim"]]) 
        self.in_file = "./templates/init.vim"

    def copy(self):
        print("Copying init.vim")
        logging.info("Copying init.vim")
        os.makedirs(os.path.dirname(self.out_file), exist_ok=True)
        with open(self.in_file, "r") as fi:
            init_vim = Template(fi.read()).safe_substitute(userhome=self.userhome)
            with open(self.out_file, "w") as fo:
                fo.write(init_vim)

def handle_basic_dependencies():
    '''homebrew and neovim will always be either installed or updated'''
    try:
        dep = Dependency("brew", INSTALL_HOMEBREW, UPDATE_HOMEBREW)
        n_dep = Dependency("nvim", INSTALL_NEOVIM, [])
        if dep.is_installed():
            dep.update()
        else:
            dep.install()
        if not n_dep.is_installed(): 
            n_dep.install()
    except Exception as e:
        logging.error("Error installing breq and neovim, possible network error", e)

def install_dependency(dependency):
    if dependency.is_installed():
        dependency.update()
    else:
        dependency.install()

def main(args, dependencies):
    print(dependencies)
    if args.vim:
        InitVim().copy()
    else:
        handle_basic_dependencies()
        #install_dependency(dependencies)
        InitVim().copy()
        print(args)

def parse_config(is_neovim: bool=True, is_homebrew: bool=True):
    check = lambda k, d: d[k] if k in d else ""
    
    with open("./config.json") as f:
        config = json.load(f)
        
        CONFIG["paths"] = config["paths"]
        print(config)

        if is_neovim:
            # Neovim only or both
            for key in config['dependencies']['neovim']:

                dep = config['dependencies']['neovim'][key]
                dependency = Dependency(
                        check("name", dep), 
                        check("install", dep), 
                        check("update", dep),
                        check("check", dep))
                install_dependency(dependency)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--install', '-i', action="store_true", 
            help="Use for initial setup to install all dependencies, can limit with -b/-n")
    parser.add_argument('--update', '-u', action="store_true",
            help="Use to update all dependencies can limit with -b/-n")
    parser.add_argument('--bash_profile', '-b', action="store_true",
            help="Use to only update your .bash_profile")
    parser.add_argument('--neovim', '-n', action="store_true",
            help="Use to only update neovim")
    parser.add_argument('--vim', '-v', action="store_true",
            help="Use to only update init.vim")

    return parser.parse_args()

if __name__ == "__main__":
    main(parse_args(), parse_config())
