package main

import (
	"flag"
	"fmt"
)

// All dependencies should implement this function
type BaseDependency interface {
	Install()
	Update()
	CheckInstall()
}

// This is a basic dependency
type Dependency struct {
	command string
	install string
	update  string // command()
}

// Installs a dependency
func (d *Dependency) Install() {
	fmt.Println(d.install)
}

// Updates a dependency
func (d *Dependency) Update() {
	fmt.Println(d.update)
}

// Checks if a dependency needs to be installed
func (d *Dependency) CheckInstall() {
	fmt.Println("which " + d.command)
}

//func NewDependency (brewCommand string) d Dependency {
//	d := Dependency{
//		command: brewCommand,
//		install: "brew install " + command,
//		install: "brew update " + command
//	}
//
//	return d
//}

type BrewDependency struct {
	*Dependency
	command string
}

func (d *BrewDependency) Install() {
	fmt.Println("brew install " + d.command)
}

func (d *BrewDependency) Update() {
	fmt.Println("brew update " + d.command)
	fmt.
}

//type NeoVim struct {
//}

func main() {
	hasBrew := flag.Bool("brew", false, "Install or update brew")
	hasNeovim := flag.Bool("nvim", false, "Install or update vim")
	hasInitvim := flag.Bool("initnvim", false, "Copy init.vim")

	flag.Parse()

	test := BrewDependency{command: "nvim"}
	test.CheckInstall()
	test.Install()
	test.Update()

	fmt.Println(*hasBrew)
	fmt.Println(*hasNeovim)
	fmt.Println(*hasInitvim)
}
