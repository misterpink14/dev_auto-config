#!/bin/bash
function re-source_ssh_agent(){
    rm -f "$HOME"/.ssh/`hostname`.agent
    ssh-agent -t 28800 > "$HOME"/.ssh/`hostname`.agent > /dev/null
    source "$HOME"/.ssh/`hostname`.agent > /dev/null
    ssh-add > /dev/null
}

## SSH agent script
if [ -e "$HOME"/.ssh/`hostname`.agent ]
then
    source "$HOME"/.ssh/`hostname`.agent > /dev/null
fi
ssh-add -l 2>&1 > /dev/null
ident=$?
if [ $ident -ne 0 ] 
then
    ssh-add > /dev/null
    ident=$?
    if [ $ident -ne 0 ] 
    then
        re-source_ssh_agent
    fi  
fi

echo 'done'
