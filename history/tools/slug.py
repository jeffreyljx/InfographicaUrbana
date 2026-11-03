"""Shared slug rule for the EmpireMap project (every builder imports this).

slugify(name): start from the Cliopatria Name; if it starts with "(", strip the
parentheses and remember the prefix "rel-"; NFKD-normalise, drop combining
marks, lower-case, replace every run of characters outside [a-z0-9] with "-",
strip leading and trailing "-", then add the "rel-" prefix if remembered.

  "Tang Dynasty"                      -> "tang-dynasty"
  "Chámpa"                            -> "champa"
  "(British Empire)"                  -> "rel-british-empire"
  "Abbasid Caliphate/Buyid Dynasty"   -> "abbasid-caliphate-buyid-dynasty"
"""
import re
import unicodedata

_NON_ALNUM = re.compile(r"[^a-z0-9]+")


def slugify(name: str) -> str:
    name = str(name)
    rel = False
    if name.startswith("("):
        rel = True
        name = name[1:]
        if name.endswith(")"):
            name = name[:-1]
    name = unicodedata.normalize("NFKD", name)
    name = "".join(ch for ch in name if not unicodedata.combining(ch))
    name = name.lower()
    name = _NON_ALNUM.sub("-", name).strip("-")
    return ("rel-" + name) if rel else name


if __name__ == "__main__":
    import sys
    for a in sys.argv[1:] or ["Tang Dynasty", "Chámpa", "(British Empire)",
                              "Abbasid Caliphate/Buyid Dynasty"]:
        print(repr(a), "->", slugify(a))
