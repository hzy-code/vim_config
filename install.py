#!/usr/bin/python
#-*-coding: utf-8-*-

import os

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

    
def main():
    is_install_powerline() and install_vim_powerline()

if __name__=="__main__":
    main()
