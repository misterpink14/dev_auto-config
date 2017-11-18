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
    [] add a check for vim-plug
    [] additional plugin requirements


definite must haves:
    brew
    neovim
'''

import os
import subprocess
import argparse
import configparser
import logging

INSTALL_HOMEBREW = """/usr/bin/ruby -e $(curl -fsSL \
https://raw.githubusercontent.com/Homebrew/install/master/install)"""
UPDATE_HOMEBREW = "brew upgrade && brew upgrade"
INSTALL_NEOVIM = "brew install neovim/neovim/neovim"


class Dependency():
    """Class for installing / updating dependencies"""
    def __init__(self, name: str, install_command: str, update_command: str, check_install_cmd: str=None):
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

    @staticmethod
    def dependency_from_dict(dependency: dict):
        install_dep = dependency['install'] if 'install' in dependency else ''
        update_dep = dependency['update'] if 'install' in dependency else ''
        return Dependency(name, dependency['install'], dependency['update'])

    def is_installed(self, dependency: str):
        if self.check_install_command:
            return self._execute(self.check_install_command, "checking")
        else:
            return subprocess.call(["which", self.name]) == 0 # TODO: replace with _execute

class InitVim():

    def __init__(self):
        # TODO: move this into the config.ini
        user_home = os.path.expanduser("~")
        self.out_file = user_home + "/.config/nvim/init.vim"
        self.in_file = "./init.vim"

    def copy(self):
        print("Copying init.vim")
        logging.info("Copying init.vim")
        os.makedirs(os.path.dirname(self.out_file), exist_ok=True)
        with open(self.in_file, "r") as fi:
            with open(self.out_file, "w") as fo:
                fo.write(fi.read())

def handle_basic_dependencies():
    '''homebrew and neovim will always be either installed or updated'''
    try:
        dep = Dependency("homebrew", INSTALL_HOMEBREW, UPDATE_HOMEBREW)
        if Dependency.is_installed("brew"):
            dep.update()
        else:
            dep.install()
        if not Dependency.is_installed("nvim"): 
            n_dep = Dependency("neovim", INSTALL_NEOVIM, [])
            n_dep.install()
    except Exception as e:
        logging.error("Error installing basic dependencies, possible network error", e)

def install_dependencies(dependencies):
    for name in dependencies:
        dep = Dependency.dependency_from_dict(dependencies[name])
        if dep.is_installed():
            dep.update()
        else:
            dep.install()

def main(args, dependencies):
    if args.vim:
        InitVim().copy()
    else:
        handle_basic_dependencies()
        install_dependencies(dependencies)
        InitVim().copy()
        print(args)

def parse_config(is_neovim: bool=True, is_homebrew: bool=True):
    config = configparser.ConfigParser()
    dependencies = {}

    conf = config.read('config.ini')
    if not is_homebrew:
        # Neovim only or both
        for key in conf['Dependencies']['Neovim']:
            dependencies[key] = conf['Dependencies']['Neovim']
            #if 'type' in conf['Dependencies']['Neovim'][key]:

    #if not is_neovim:
        # Bash Profile only or both

        # if is_work: # append .work_profile source to .bash_profile

    return dependencies


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
