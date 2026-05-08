#!/usr/bin/env python3

# the script takes a list of keys, words, and joiners, then generates a file of all possible combos of those
# and writes them to a file, which can be made into a fcitx5 table dictionary using `libime_tabledict`
#
# if you wanna use this as your IME, follow the install structions at https://github.com/mun-luna/nasin-mun
# but make sure to replace `./nasin-mun/table/nasin-mun.dict` with the one outputted by this script
# BEFORE using the nix module or the install script
#
# all keys are generated in the format of "KeyOne-KeyTwo", if you need to use a certain joiner, navigate using the hint

def table_setup():
    return """# Generated using a python script
# Convert to a table using `libime_tabledict`
KeyCode=ptkmnswljaeiou-
Length=15

[Data]"""

def gen_combinations(keys, words, joiners):
    final = table_setup()
    # generate the key-word pairs
    for i, keyOne in enumerate(keys):
        for joiner in joiners:
            for j, keyTwo in enumerate(keys):
                if j == 0:
                    result = "\n" + keyOne + " " + words[i]
                    final = final + result
                    result = ("\n" + keyOne + "-" + keyTwo + " " \
                            + words[i] + joiner + words[j])
                else:
                    result = ("\n" + keyOne + "-" + keyTwo + " " \
                            + words[i] + joiner + words[j])
                final = final + result
    return final

def main():
    keys = [ "a", "akesi", "ala", "alasa", "ale", "anpa", "ante", "anu", "awen", "e", #T1 Word Chars
            "en", "esun", "ijo", "ike", "ilo", "insa", "jaki", "jan", "jelo", "jo",
            "kala", "kalama", "kama", "kasi", "ken", "kepeken", "kili", "kin", "kiwen", "ko",
            "kon", "kule", "kulupu", "kute", "la", "lape", "laso", "lawa", "len", "lete",
            "li", "lili", "linja", "lipu", "loje", "lon", "luka", "lukin", "lupa", "ma",
            "mama", "mani", "meli", "mi", "mije", "moku", "moli", "monsi", "monsuta", "mu",
            "mun", "musi", "mute", "nanpa", "nasa", "nasin", "nena", "ni", "nimi", "noka",
            "o", "olin", "ona", "open", "pakala", "pali", "palisa", "pan", "pana", "pi",
            "pilin", "pimeja", "pini", "pipi", "poka", "poki", "pona", "pu", "sama", "seli",
            "selo", "seme", "sewi", "sijelo", "sike", "sin", "sina", "sinpin", "sitelen", "sona",
            "soweli", "suli", "suno", "supa", "suwi", "tan", "taso", "tawa", "telo", "tenpo",
            "toki", "tomo", "tonsi", "tu", "unpa", "uta", "utala", "walo", "wan", "waso",
            "wawa", "weka", "wile",
            "kijetesantakalu", "kipisi", "ku", "leko", "misikeke", "n", "namako", "soko", #T2 Word Chars
            "epiku", "jasima", "lanpan", "linluwi", "majuna", "meso", "oko", "su" ] #T3 Word Chars, altglyphs excluded
    words = [ "󱤀", "󱤁", "󱤂", "󱤃", "󱤄", "󱤅", "󱤆", "󱤇", "󱤈", "󱤉", #T1 Word Chars
             "󱤊", "󱤋", "󱤌", "󱤍", "󱤎", "󱤏", "󱤐", "󱤑", "󱤒", "󱤓",
             "󱤔", "󱤕", "󱤖", "󱤗", "󱤘", "󱤙", "󱤚", "󱥹", "󱤛", "󱤜",
             "󱤝", "󱤞", "󱤟", "󱤠", "󱤡", "󱤢", "󱤣", "󱤤", "󱤥", "󱤦",
             "󱤧", "󱤨", "󱤩", "󱤪", "󱤫", "󱤬", "󱤭", "󱤮", "󱤯", "󱤰",
             "󱤱", "󱤲", "󱤳", "󱤴", "󱤵", "󱤶", "󱤷", "󱤸", "󱥽", "󱤹",
             "󱤺", "󱤻", "󱤼", "󱤽", "󱤾", "󱤿", "󱥀", "󱥁", "󱥂", "󱥃",
             "󱥄", "󱥅", "󱥆", "󱥇", "󱥈", "󱥉", "󱥊", "󱥋", "󱥌", "󱥍",
             "󱥎", "󱥏", "󱥐", "󱥑", "󱥒", "󱥓", "󱥔", "󱥕", "󱥖", "󱥗",
             "󱥘", "󱥙", "󱥚", "󱥛", "󱥜", "󱥝", "󱥞", "󱥟", "󱥠", "󱥡",
             "󱥢", "󱥣", "󱥤", "󱥥", "󱥦", "󱥧", "󱥨", "󱥩", "󱥪", "󱥫",
             "󱥬", "󱥭", "󱥾", "󱥮", "󱥯", "󱥰", "󱥱", "󱥲", "󱥳", "󱥴",
             "󱥵", "󱥶", "󱥷", 
             "󱦀", "󱥻", "󱦈", "󱥼", "󱦇", "󱦆", "󱥸", "󱦁", #T2 Word Chars
             "󱦃", "󱥿", "󱦅", "󱦤", "󱦢", "󱦂", "󱥺", "󱦦", ] #T3 Word Chars
    joiners = [ chr(0x200d), chr(0xf1995), chr(0xf1996) ] # ZERO-WIDTH, STACKING, NESTING
    with open("table.txt", "w", encoding="utf-8") as f:
        f.write(gen_combinations(keys, words, joiners))

if __name__ == "__main__":
    main()
