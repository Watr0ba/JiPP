#Zadanie: Masz plik raw.txt, który zawiera puste i niepuste linie.
#Napisz program, który:
#odczytuje wszystkie linie z raw.txt
#usuwa puste linie (linie, które są puste lub zawierają tylko białe znaki)
#zapisuje tylko niepuste linie do nowego pliku o nazwie clean.txt
#Wskazówka: Użyj .strip() aby sprawdzić czy linia jest pusta; if line.strip() != "", zachowaj ją.
with open("raw.txt", "r", encoding="utf-8") as source:
    lines = source.readlines()

with open("clean.txt", "w", encoding="utf-8") as target:
    for line in lines:
        if line.strip() != "":
            target.write(line)
