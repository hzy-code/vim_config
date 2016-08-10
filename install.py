#!/usr/bin/python
#-*-coding: utf-8-*-

import os
import shutil

def is_install_powerline():
    res=os.system("rpm -q vim-powerline")   
    return res==0

def install_vim_powerline():
    f_con=open("extra/powerline.conf","r")
    vim_path=os.path.join(os.environ["HOME"],".vimrc")
    f_vim=open(vim_path,"a")
    f_vim.write("\"powerline config\n")
    for line in f_con:
        f_vim.write(line)
    f_vim.close()
    f_con.close()

    
def setup_powerline():
    is_install_powerline() and install_vim_powerline()

def setup_vundle():
	cmd='git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim'
	os.system(cmd)

def setup_vimrc():
	home = os.getenv('HOME')
	shutil.copyfile("config/vimrc", os.path.join(home, ".vimrc"))

def main():
	setup_vundle()
	setup_vimrc()
	setup_powerline()

if __name__=="__main__":
    main()
