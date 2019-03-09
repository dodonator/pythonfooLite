#!/usr/bin/env python3

# Schleifen:

# 2. Die for-Schleife:

# Die for-Schleife durchläuft ein iterierbares
# Objekt. Alle oben genannten Listen sind solche
# iterierbaren Objekte.
String = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for char in String: # type: str
    print(char)

# Beim Durchlaufen eines Dictionary wird jedoch nur
# der key zurückgegeben:
Dictionary = {"one": "Eins", "two": "Zwei", "three": "drei"}
for key in Dictionary:
    print(key)
    print(Dictionary[key])

# besser:
for key, value in Dictionary.items():
    print(key, value)

# Ebenso kann ein Tupel oder eine Liste durchlaufen werden

# Mit dem Befehl range() erschafft man ein iterierbares
# Objekt, das mit Zahlen gefüllt ist:
R = range(10)
print(list(R))

# Dabei kann man auch den Startwert und die Schrittweite
# angeben:
R = range(0, 101, 2)
print(list(R))

# Somit kann man eine Zählschleife implementieren:
R = range(10)
for i in R:
    print(i)

# oder:

for i in range(10):
    print(i)
