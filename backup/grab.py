#!/usr/bin/python3

#-- Grabs all the dotfiles from around the file system and puts them in ~/dotfiles then pushes them up --#

import sys
import os
import pwd

user = pwd.getpwuid( os.getuid() )[ 0 ]
dotfiles_folder = f"/home/{user}/dotfiles"
dotfiles = {
    '.tmux.conf': f'/home/{user}',
    '.vimrc': f'/home/{user}',
    '.zshrc': f'/home/{user}',
    '.gitconfig': f'/home/{user}',
    '.bashrc': f'/home/{user}',
    'init.vim':f'/home/{user}/.config/nvim',
    '*':f'/home/{user}/.local/share/konsole',
    }
if not os.path.isdir(dotfiles_folder):
    os.system('git clone git@github.com:h3x/dotfiles.git ~/dotfiles')

for i, (f,loc) in enumerate(dotfiles.items()):
    os.system(f"cp {loc}/{f} {dotfiles_folder}/")

os.system(f'cd /home/{user}/dotfiles && git add . && git commit -m "Automated Push" && git push && cd /home/{user}')
# push to github
