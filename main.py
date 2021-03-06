#/usr/local/bin/python3
import sys
import json
import logging
import argparse

from typing import Dict, List, Optional

from config import Config
from template import TemplateFile
from dependency import Dependency, BrewDependency
from util import check_in_dict_failback

def install_brew():
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
            logging.error("Failed to copy template:", template_config, e)
            raise e

def handle_dependency(dependency: Dependency):
    try:
        if not dependency.is_installed():
            dependency.install()
            return
    except:
        logging.warn("Install failed, attempting to update", dependency.name) 
        try:
            dependency.update()
        except:
            logging.error("Failed to install dependency:", dependency)

def handle_dependencies(dependencies_config: List[Dict[str, List[str] or str]]):
    for dep in dependencies_config:
        dependency = Dependency(
            dep["name"],
            check_in_dict_failback("install", dep),
            check_in_dict_failback("update", dep),
            check_in_dict_failback("check", dep))
        handle_dependency(dependency)

def handle_hombrew_dependencies(dep: str or Dict[str or List[str]], brew_type: str=""):
    for dep in homebrew_config['dependencies']:
        if isinstance(dep, str): 
            dependency = BrewDependency(
                    dep,
                    None,
                    None,
                    brew_type)
        else:
            dependency = BrewDependency(
                    dep["brew_name"], 
                    check_in_dict_failback("name", dep),
                    check_in_dict_failback("setup", dep),
                    brew_type)
        handle_dependency(dependency)

def handle_homebrew(homebrew_config: Dict[str, List[str or Dict[str, str]]]):
    if 'dependencies' in homebrew_config:
        logging.info("-- Installing Homebrew Dependencies")
        #handle_hombrew_dependencies(homebrew_config['dependencies'])
    if 'taps' in homebrew_config:
        logging.info("-- Installing Homebrew Taps")
        print(homebrew_config['taps'])
        #handle_hombrew_dependencies(homebrew_config['taps'], BrewDependency.TAP)
    if 'casks' in homebrew_config:
        logging.info("-- Installing Homebrew Casks")
        print(homebrew_config['casks'])
        #handle_hombrew_dependencies(homebrew_config['taps'], BrewDependency.CASK)

def main(args: argparse.Namespace, configs: Dict):
    for group in configs:
        config = configs[group]
        if args.templates:
            copy_templates(config.templates)
        if args.dependencies:
            if not args.quick:
                install_brew()
            if config.dependencies:
                handle_dependencies(config.dependencies)
            if config.homebrew:
                handle_homebrew(config.homebrew)


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
    parser.add_argument("--skip", "-s", 
            help="Comma separated list of configs to ignore")

    args = parser.parse_args()
    if args.skip:
        args.skip = [x.strip() for x in args.skip.split(",")]
    if not len(sys.argv) > 1:
        args.all = True
    if args.templates:
        args.quick = True
    if args.all:
        args.templates = True
        args.dependencies = True

    main(args, Config.load_configs())
