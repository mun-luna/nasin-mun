#!/usr/bin/env bash
echo "THIS SCRIPT WILL NOT INSTALL THE NEEDED PACKAGES: which are fcitx5, fcitx5-table-other, and sometimes fcitx5-chinese-addons depending on the distro."
echo "copying files..."
mkdir -p ~/.local/share/fcitx5/
cp -r ./nasin-mun/ ~/.local/share/fcitx5/
echo "killing fcitx5"
pkill fcitx5
echo "you need to enable the nasin mun input method, it is easiest to do this via KDE system settings"
echo "after that, you need to relaunch fcitx5! if using KDE, use the system settings in Keyboard > Virtual Keyboard"
