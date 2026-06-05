#!/usr/bin/env bash
echo "THIS SCRIPT WILL NOT INSTALL THE NEEDED PACKAGES: which are fcitx5, fcitx5-table-other, and sometimes fcitx5-chinese-addons depending on the distro."
mkdir -p ~/.local/share/fcitx5/
cp -r ./nasin-mun/* ~/.local/share/fcitx5/
mkdir -p ~/.config/fcitx5/
cp ./nasin-mun/profile ~/.config/fcitx5/profile
pkill fcitx5
echo "this script only copies the needed files, and kill any currently running fcitx5 processes, you will need to do the following yourself:"
echo ""
echo "if using x11, set the envvars \`GTK_IM_MODULE=fcitx\`, and \`QT_IM_MODULE=fcitx\` via whatever method is best suited for your distro"
echo "always set the envvar \`XMODIFIERS=@im=fcitx\`"
echo ""
echo "by default, this script enables the nasin mun input method with a US keyboard layout. if you do not use a US keyboard layout, you will need to change this via \`fcitx5-configtool\` or KDE's system settings"
echo ""
echo "after finishing configing, you need to relaunch fcitx5! it would be best to set fcitx5 so that it autostarts. if using KDE, it is best to use the system settings in 'Keyboard > Virtual Keyboard'"
echo ""
echo "the \`fcitx5-diagnose\` command may be useful to diagnose any errors you have"
echo "fcitx-im.org is the wiki for fcitx5"
echo "wiki.archlinux.org/title/Fcitx5 may have useful information"
