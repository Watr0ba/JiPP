#Zadanie: Napisz program, który:
#odczytuje zawartość numbers.txt
#kopiuje wszystko do nowego pliku o nazwie copy.txt
#Wskazówka: Użyj read() aby pobrać całą zawartość na raz, lub kopiuj linię po linii.
with open("numbers.txt", "r", encoding="utf-8") as source:
    content = source.read()

with open("copy.txt", "w", encoding="utf-8") as target:
    target.write(content)
