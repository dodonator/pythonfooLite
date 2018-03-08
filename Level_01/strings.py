#!/usr/bin/env python3

# zur Bedeutung von `print` siehe Ein_Ausgabe.py

ein = "Dies ist ein einzeiliger String."
print(ein)

mehr = """
Dies ist ein mehrzeiliger String.

	Leerzeilen, Zeilenumbrüche und Einrückung
	werden mit in den String übernommen.
"""

print(mehr)

f = "foo"
b = "bar"

# Operatoren auf Strings anwenden:
# (für mehr Informationen siehe die Wiki-Seite zu Operatoren)
print(f + b)
print(5 * f)
print(5 * (f + " "))

# Daten anderer Typen in Strings umwandeln:
s = str(5)
print(s)