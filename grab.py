#!/usr/bin/python3
import sys
import os
import pwd

user = pwd.getpwuid( os.getuid() )[ 0 ]
dotfiles_folder = f"/home/{user}/dotfiles"
dotfiles = {
    '.tmux.conf': f'/home/{user}/',
    
}
if not os.path.isdir(dotfiles_folder):
    os.system('git clone git@github.com:h3x/dotfiles.git ~/dotfiles')

# Grab all dotfiles detailed in the dotfiles dict and place into the dotfiles directory


# push to github
