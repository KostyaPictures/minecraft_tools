#WIP
outp=""

lines=14
column_pix=114 #6*19
author="Kostya Pct."
generation=0
title="Book with custom text"
#splitting with - �
letters={
    "q": 6,
    "w": 6,
    "e": 6,
    "r": 6,
    "t": 4,
    "y": 6,
    "u": 6,
    "i": 2,
    "o": 6,
    "p": 6,
    "a": 6,
    "s": 6,
    "d": 6,
    "f": 5,
    "g": 6,
    "h": 6,
    "j": 6,
    "k": 5,
    "l": 3,
    "z": 6,
    "x": 6,
    "c": 6,
    "v": 6,
    "b": 6,
    "n": 6,
    "m": 6,
    " ": 5,
    "й": 6,
    "ц": 6,
    "у": 6,
    "к": 5,
    "е": 6,
    "н": 6,
    "г": 5,
    "ш": 6,
    "щ": 7,
    "з": 6,
    "х": 6,
    "ъ": 7,
    "ф": 6,
    "ы": 7,
    "в": 6,
    "а": 6,
    "п": 6,
    "р": 6,
    "о": 6,
    "л": 6,
    "д": 7,
    "ж": 6,
    "э": 6,
    "я": 6,
    "ч": 6,
    "с": 6,
    "м": 6,
    "и": 6,
    "т": 6,
    "ь": 6,
    "б": 6,
    "ю": 7,
    ",": 2,
    ".": 2,
    "!": 2,
    "?": 6,
    ":": 2,
    ";": 2,
    "\"": 4,
    "'": 2,
    "*": 4,
    "%": 6,
    "$": 6,
    "&": 6,
    "0": 6,
    "1": 6,
    "2": 6,
    "3": 6,
    "4": 6,
    "5": 6,
    "6": 6,
    "7": 6,
    "8": 6,
    "9": 6,
    "§": -6,
    "�": 0
}


text=open("input.txt", "r", encoding="UTF-8").read()
text=text.replace("\n", "\\\\n")
text=text.replace("�", "\"\'},{\"raw\":\'\"")


print(text)
with open("output.txt", "w", encoding="UTF-8") as f:
    outp=f"/give @p minecraft:written_book[written_book_content={{author:\"{author}\", generation:{generation}, title:\"{title}\",pages:[{{\"raw\":\'\""+text+"\"\'}]}]"
    f.write(outp)
