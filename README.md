
# nasin mun

a fcitx5 IME for sitelen pona

ive tried to comment the table as much as possible, so edits should be easy enough

## installation
`./install.sh` will copy the needed files to the correct destination, you will then need to enable the input method (which is easiest via KDE system settings) and start fcitx5. **the install script will not install the needed packages**, which are `fcitx5`, `fcitx5-table-other`, and sometimes `fcitx5-chinese-addons` depending on the distro.

if using nixos, there is an included module (requires home manager) that will enable fcitx5, and symlink the needed files. you will still need to enable the input method via system settings, however this file is saved to `~/.config/fcitx5/profile` *when fcitx5 closes*, the module can then be edited to symlink this too.

## usage

type any toki pona word, and confirm it by pressing `space` or any punctuation shown below. pressing `enter` will release the raw text instead.

fcitx5 will show a candidate list as you type, which could help you type faster. use the arrow keys and `space` to select a candidate, or the numbers on your keyboard.

### punctuation
- `[` and `]` for start and end of cartouche
- `(` and `)` for start and end of long glyph
- `-` for joining glyphs in a non-standard way
- `=` for stacking glyphs on top of each other
- `+` for nesting glyphs inside of each other
- `|` for ideographic space
- `'`, or `"` for corner bracket quotes
- `.` for middle dot
- `:` for colon
- `,` for tally mark
