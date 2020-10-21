from typing import Dict, List, Tuple, Union


def flaecheninhalt(
    breite: Union[float, int], laenge: Union[float, int]
) -> Union[float, int]:
    return breite * laenge


def zeichenzaehlen(text: str) -> Dict[str, int]:
    return {character: text.count(character) for character in text}


def fancy_function(
    namen_und_matrikelnummern: List[Tuple[str, int]],
    semester: int,
    bestanden: bool = False,
):
    for eintrag in namen_und_matrikelnummern:
        print(f"Student {eintrag[0]} {eintrag[1]}")
        print(f"Im {semester}. Semester hat")
        print(f"{'nicht ' if not bestanden else ''}bestanden.")


fancy_function([("marc", 123), ("pascua", 456)], 5, True)

zeichenzaehlen("hello there general kenobi")

flaecheninhalt(4.2, 69.420)