import os
import logging

from string import Template

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

