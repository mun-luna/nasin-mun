
# nasin mun

a fcitx5 IME for sitelen pona

ive tried to comment the table as much as possible, so edits should be easy enough

## installation
`./install.sh` will copy the needed files to the correct destination, you will then need to enable the input method (which is easiest via KDE system settings) and start fcitx5.

if using nixos, there is an included module (requires home manager) that will enable fcitx5, and symlink the needed files. you will still need to enable the input method via system settings, however this file is saved to `~/.config/fcitx5/profile` *when fcitx5 closes*, the module can then be edited to symlink this too.

