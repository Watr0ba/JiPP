#Zadanie: Napisz program, który:
#pyta użytkownika o jego imię i wiek
#zapisuje dane do user.txt w tym formacie:
#Imię: Jan Wiek: 12
#Wskazówka: Użyj input() aby odczytać dane od użytkownika, i write() aby formatować tekst za pomocą f-stringów.
name = input("Podaj imię: ")
age = input("Podaj wiek: ")
with open("user.txt", "w", encoding="utf-8") as file:
    file.write(f"Imię: {name} Wiek: {age}")
