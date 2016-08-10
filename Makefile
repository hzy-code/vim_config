.PHONY: install uninstall

install:
	./install.py
	echo "Done!"

uninstall:
	-rm -f $(HOME)/.vimrc
	-rm -rf $(HOME)/.vim
