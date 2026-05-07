
# nasin mun

a fcitx5 IME for sitelen pona

ive tried to comment the table as much as possible, so edits should be easy enough

## installation
`./install.sh` will copy the needed files to the correct destination, you will then need to enable the input method (which is easiest via KDE system settings) and start fcitx5. **the install script will not install the needed packages**, which are `fcitx5`, `fcitx5-table-other`, and sometimes `fcitx5-chinese-addons` depending on the distro.

if using nixos, there is an included module (requires home manager) that will enable fcitx5, and symlink the needed files. you will still need to enable the input method via system settings, however this file is saved to `~/.config/fcitx5/profile` *when fcitx5 closes*, the module can then be edited to symlink this too.

