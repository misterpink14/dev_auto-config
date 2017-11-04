package main

import (
	"flag"
	"log"
	"os/exec"
)

// All dependencies should implement this function
type BaseDependency interface {
	Install()
	Update()
	checkInstall()
	CheckInstall()
}

// This is a basic dependency
type Dependency struct {
	command string
	install string
	update  string // command()
}

type BrewDependency struct {
	Dependency
	command string
}

type ModBrewDependency struct {
	BrewDependency
	bashCommand string
}

// Installs a dependency
func (d *Dependency) Install() {
	log.Println(d.install)
}

// Updates a dependency
func (d *Dependency) Update() {
	log.Println(d.update)
}

func (d *Dependency) checkInstall(cmd string) {
	_, err := exec.Command("which", cmd).Output()
	if err != nil {
		if err.Error() == "exit status 1" {
			return false
		}
		log.Fatalln("Failed to execute which command for: ", d.command, err)
	}
	return true
}

// Checks if a dependency needs to be installed
func (d *Dependency) CheckInstall() bool {
	d.checkInstall(d.command)
}

func (d *BrewDependency) Install() {
	log.Println("brew install " + d.command)
}

func (d *BrewDependency) Update() {
	log.Println("brew update " + d.command)
}

func (d *ModBrewDependency) CheckInstall() {
	d.checkInstall(d.bashCommand)
}

func handleDependency(d Dependency) {
	if d.CheckInstall() {
		d.Update()
	} else {
		d.Install()
	}
}

func HandleDependency(dCommand, dInstall, dUpdate string) {
	d := Dependency{
		command: dCommand,
		install: dInstall,
		update:  dUpdate}
	handleDependency(d)
}

func HandleBrewDependency(bCommand) {
	bd := BrewDependency{command: bCommand}
	handleDependency(bd)
}

func HandleModBrewDependency() {
	mbd := ModBrewDependency{command: brewCommand, bashCommand: bashCommand}
	handleDependency(mbd)
}

func main() {
	hasBrew := flag.Bool("brew", false, "Install or update brew")
	hasNeovim := flag.Bool("nvim", false, "Install or update vim")
	hasInitvim := flag.Bool("init.vim", false, "Copy init.vim")

	flag.Parse()

	log.Println(*hasBrew)
	log.Println(*hasNeovim)
	log.Println(*hasInitvim)

	if *hasBrew {
		HandleDependency(
			"brew",
			"/usr/bin/ruby -e $(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)",
			"brew upgrade && brew upgrade")
	}
	if *hasNeovim() {
		HandleNeovimDependency()
	}
}
