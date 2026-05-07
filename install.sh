#!/bin/bash
echo "THIS SCRIPT WILL NOT INSTALL THE NEEDED PACKAGES: which are fcitx5, fcitx5-table-other, and sometimes fcitx5-chinese-addons depending on the distro."
echo "copying files..."
cp ./nasin-mun/inputmethod/nasin-mun.conf ~/.local/share/fcitx5/inputmethod/nasin-mun.conf
cp ./nasin-mun/punctuation/punc.mb.tok ~/.local/share/fcitx5/punctuation/punc.mb.tok
cp ./nasin-mun/table/nasin-mun.dict ~/.local/share/fcitx5/table/nasin-mun.dict
echo "killing fcitx5"
pkill fcitx5
echo "you need to enable the nasin mun input method, it is easiest to do this via KDE system settings"
echo "after that, you need to relaunch fcitx5! if using KDE, use the system settings in Keyboard > Virtual Keyboard"
