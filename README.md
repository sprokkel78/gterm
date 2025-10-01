![Screenshot](https://github.com/sprokkel78/gterm/blob/main/screenshots/title.png)

![Screenshot](https://github.com/sprokkel78/gterm/blob/main/screenshots/gterm-1.png)

A simple Terminal App in PyGtk3. (Linux) 
It requires Python3.10 and the PyGTK apps. Developed on Fedora 42 and tested on Ubuntu 24.04.

Runs out of the	box after default installation of Fedora or Ubuntu.

Installation on Fedora 42 & Ubuntu 24.04

1. $git clone https://github.com/sprokkel78/gterm.git
2. $cd gterm
3. $python3 ./gterm.py 

For System-Wide Installation, run:
- $sudo ./install.sh

Then start with:
- $gterm
- or by clicking the application icon.

Added 'install.sh' script for system-wide installation.
- The startup shell script will be /usr/bin/gterm
- The application is installed in /usr/share/gterm-sprokkel78
- The .desktop file is placed in /usr/share/applications/com.sprokkel78.gterm.desktop

Added 'uninstall.sh' script for system-wide uninstallation.
- This will delete /usr/bin/gterm and /usr/share/gterm-sprokkel78,
  This will also remove /usr/share/applications/com.sprokkel78.gterm.desktop

Check https://www.github.com/sprokkel78/gterm for contributing, development features and pre-releases.
