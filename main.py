#/usr/local/bin/python3
import sys
import json
import logging
import argparse

from typing import Dict, List, Optional

from config import Config
from template import TemplateFile
from dependency import Dependency, BrewDependency
from util import as_list

def brew():
    '''homebrew will always be either installed or updated'''
    try:
        dep = Dependency(
            "brew", 
            "/usr/bin/ruby -e $(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)",
            "brew upgrade && brew upgrade")
        if dep.is_installed():
            dep.update()
        else:
            dep.install()
    except Exception as e:
        logging.error("Error installing brew, possible network error", e)

def copy_templates(template_configs: List[Dict[str, str]]):
    for template_config in template_configs:
        try:
            name = template_config['name']
            path = template_config['path']
            TemplateFile(name, path).copy()
        except Exception as e:
            logging.error("Failed to copy template:", e)
            raise e

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
    config = Config.load()

    if args.templates:
        copy_templates(config.templates)
    if args.dependencies:
        if not args.quick:
            brew()
        if config.dependencies:
            logging.info("-- Installing Dependencies")
            for name, dep in config.dependencies.items():
                logging.info("---- Installing", name)
                handle_dependency(create_dependency(dep))
        if config.homebrew:
            if 'dependencies' in config.homebrew:
                logging.info("-- Installing Homebrew Dependencies")
                for dep in config.homebrew['dependencies']:
                    if isinstance(dep, str): 
                        dependency = BrewDependency(dep)
                    else:
                        dependency = BrewDependency(
                                dep["brew_name"], 
                                dep["name"], 
                                dep["setup"] if "setup" in dep else None)
                    handle_dependency(dependency)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--quick', '-q', action="store_true",
            help="Use to skip updating brew")
    parser.add_argument('--templates', '-t', action="store_true",
            help="Use to copy templates (implies quick)")
    parser.add_argument('--dependencies', '-d', action="store_true",
            help="Use to install dependencies")
    parser.add_argument("--all", "-a", action="store_true",
            help="Use to run everything. Equivalent to ommitting args")

    args = parser.parse_args()
    if not len(sys.argv) > 1:
        args.all = True
    if args.templates:
        args.quick = True
    if args.all:
        args.templates = True
        args.dependencies = True

    main(args)
