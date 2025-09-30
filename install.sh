#!/bin/sh
#
# THIS SCRIPT WILL INSTALL THE gterm APP SYSTEM WIDE
# THE SCRIPT MUST BE RUN WITH SUDO
#
# It will create a startup shell script named gterm in /usr/bin,
# the app will be placed in /usr/share/gterm-sprokkel78
# The .desktop file will be placed in /usr/share/applications/ as com.sprokkel78.gterm.desktop

FILE="/usr/share/applications/gterm.desktop"
if [ -f $FILE ]
then
  rm $FILE
fi

mkdir -p /usr/share/gterm-sprokkel78
cp -r ./* /usr/share/gterm-sprokkel78/
echo "#!/bin/sh" > /usr/bin/gterm
echo "cd /usr/share/gterm-sprokkel78" >> /usr/bin/gterm
echo "python3 ./gterm.py" >> /usr/bin/gterm
cp ./gterm.desktop /usr/share/applications/com.sprokkel78.gterm.desktop
chmod 755 /usr/bin/gterm
chmod 644 /usr/share/gterm-sprokkel78/*
