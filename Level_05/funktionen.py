#!/usr/bin/env python3

# Funktionen:

def funktion() -> None:
    print("Hallo!")
funktion()
# OUT: Hallo!


def funktion(text: str) -> None:
    print(text)
funktion("a")
# OUT: a


def funktion(text, wirklich):
    if wirklich:
        print(text)

funktion("Hallo", True)
# OUT: Hallo

funktion(True, "Hallo")
# OUT: True


def funktion(text: str = "Beispiel", wirklich: bool = False):
    if wirklich:
        print(text)

funktion()
# OUT: None

funktion(wirklich=True)
# OUT: Beispiel

funktion(wirklich=True, text="Abc")
# OUT: Abc


def ja() -> str:
    return "Ja"
ja()
# OUT: 'Ja'


# Rekursion:

def fun() -> None:
    print("Fun!")
    fun()

# Quersumme:
def quersumme(zahl: int) -> int:
    qs = 0
    for ziffer in str(zahl):
        qs += int(ziffer)
    return qs
