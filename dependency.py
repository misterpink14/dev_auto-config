import logging
import subprocess

from typing import List

from util import get_command, append_or_merge

class Dependency(object):
    """Class for installing / updating dependencies"""
    def __init__(self, 
            name: str, 
            install_command: str or List[str], 
            update_command: str or List[str], 
            check_install_command: str=None):
        self.name = name
        self.install_command = get_command(install_command)
        self.update_command = get_command(update_command)
        self.check_install_command = get_command(check_install_command)

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
            return self._execute(' '.join(["which", self.name]), "checking")
        else:
            return False


class BrewDependency(Dependency):
    TAP="tap"
    CASK="cask"

    def __init__(self, 
            brew_name: str, 
            name: str=None, 
            setup: str or List[str]=None, 
            brew_type: str=""):
        if not name:
            name = brew_name
        install_command = ' '.join(["brew", brew_type, "install", brew_name])
        if setup:
            install_command = get_command(append_or_merge([install_command], setup))
        update_command = ' '.join(["brew", brew_type, "upgrade", brew_name])
        super(BrewDependency, self).__init__(name, install_command, update_command)

