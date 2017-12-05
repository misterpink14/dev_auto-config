#/usr/local/bin/python3
'''
For setting up your development environment

TODO:
    [] Add these:
        [] https://github.com/Shougo/deoplete.nvim
        [x] https://github.com/Shougo/dein.vim
        [] https://github.com/Shougo/denite.nvim
    [] add comments
    [] clean up a bit
    [] additional plugin requirements
    [x] homebrew
    [x] neovim
    [x] bash_profile
    [x] iterm
    [] ssh forwarding
    [] merge bash_profiles


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
        _, stderr_data = process.communicate()
        if stderr_data: 
            raise Exception("stderr_data")

    def install(self):
        if self.install_command:
            self._execute(self.install_command, "installing")

    def update(self):
        if self.update_command:
            self._execute(self.update_command, "updating")
    
    def is_installed(self):
        if self.check_install_command:
            return self._execute(self.check_install_command, "checking")
        elif self.name:
            return subprocess.call(["which", self.name]) == 0 # TODO: replace with _execute
        else:
            return False


class BrewDependency(Dependency):
    def __init__(self, brew_name: str, name: str=None):
        if not self.name:
            name = brew_name
        install_command = ' '.join(["brew", "install", brew_name])
        update_command = ' '.join(["brew", "upgrade", brew_name])
        Dependency.__init__(name, install_command, update_command)


class TemplateFile():

    def __init__(self, template_file, out_path):
        # TODO: move this into the config.ini
        self.userhome = os.path.expanduser("~")
        self.in_file = '/'.join([".", "templates", template_file])
        self.out_file = ''.join([self.userhome, "/",  out_path]) 

    def copy(self):
        print("Copying", self.in_file, "to", self.out_file)
        logging.info("Copying", self.in_file, "to", self.out_file)
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

def handle_dependency(dependency):
    try:
        if not dependency.is_installed():
            dependency.install()
            return
    except:
        print("Install failed, attempting to update")
    dependency.update()

def main(args):
    check = lambda k, d: d[k] if k in d else ""
    create_dependency = lambda dep: Dependency(
                        check("name", dep), 
                        check("install", dep), 
                        check("update", dep),
                        check("check", dep))
    
    with open("./config.json") as f:
        config = json.load(f)
        if args.vim:
            TemplateFile("init.vim", config["templates"]["init.vim"]).copy()
        if args.bash_profile:
            TemplateFile("bash_profile", config["templates"]["bash_profile"]).copy()
        if args.iterm:
            TemplateFile("com.googlecode.iterm2.plist", config["templates"]["iterm2"]).copy()
        if args.dependencies:
            if not args.quick:
                handle_basic_dependencies(config["paths"])
            for key in config['dependencies']['neovim']:
                handle_dependency(create_dependency(config['dependencies']['neovim'][key]))
            """
            for key in config['dependencies']['homebrew']:
                dep = config['dependencies']['homebrew'][key]
                if isinstance(dep, str): 
                    dependency = BrewDependency(dep)
                else:
                    dependency = BrewDependency(dep["brew_name"], dep["name"])
            """


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--quick', '-q', action="store_true",
            help="Use to skip updating brew and neovim")
    parser.add_argument('--bash_profile', '-b', action="store_true",
            help="Use to update .bash_profile (implies quick)")
    parser.add_argument('--vim', '-v', action="store_true",
            help="Use to update init.vim (implies quick)")
    parser.add_argument('--iterm', '-i', action="store_true",
            help="Use to update iterm preferences (implies quick)")
    parser.add_argument('--dependencies', '-d', action="store_true",
            help="Use to install dependencies")
    parser.add_argument("--all", "-a", action="store_true",
            help="Use to run everything")

    args = parser.parse_args()
    if args.vim or args.bash_profile:
        args.quick = True
    if args.all:
        args.vim = True
        args.bash_profile = True
        args.dependencies = True
        args.iterm = True
    return args

if __name__ == "__main__":
    main(parse_args())
