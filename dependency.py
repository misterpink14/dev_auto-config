import logging
import subprocess

from typing import List

from util import get_command

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
            return subprocess.call(["which", self.name]) == 0 # TODO: replace with _execute
        else:
            return False


class BrewDependency(Dependency):
    def __init__(self, brew_name: str, name: str=None, setup: str=None):
        if not name:
            name = brew_name
        install_command = ' '.join(["brew", "install", brew_name])
        if setup:
            install_command = get_command([install_command, setup])
        update_command = ' '.join(["brew", "upgrade", brew_name])
        super(BrewDependency, self).__init__(name, install_command, update_command)

"""
class BrewTap(BrewDependency):
    def __init__(self, brew_name: str, name: str=None, setup: str=None):

class BrewCask(BrewDependency):
    def __init__(self, brew_name: str, name: str=None, setup: str=None):
"""
