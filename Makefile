.PHONY: install uninstall

install:
	cp config/vimrc $(HOME)/.vimrc
	cp -r config/vim $(HOME)/.vim
	echo "apply extra config"
	./install.py
	echo "Done!"
uninstall:
	-rm -f $HOME/.vimrc
	-rm -rf $HOME/.vim
