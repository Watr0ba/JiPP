# Utwórz słownik filmów. Niech kluczem będzie nazwa filmu, 
# a parą wartości dwie liczby: kryteria wiekowe oraz liczba dostępnych biletów

movies = {
    "Finding Nemo": [5, 2],
    "Moana": [6, 3],
    "Batman": [18, 5],
    "The Lion King": [10, 4]
}

# Utwórz pętlę, która będzie działać w nieskończoność
while True:
    
    # Pobierz tytuł filmu od użytkownika, usuń spacje z początku i końca 
    # a następnie zamień frazę na format tytułowy (pierwsza litera każdego słowa jest wielka)
    movie = input("Podaj tytuł filmu: ").strip().title()
    
    # Stwórz instrukcję warunkową if. Jeśli wybrany film jest dostępny w słowniku, kontynuuj
    if movie in movies:
        
        # Zapytaj użytkownika o wiek
        age = int(input("Podaj swój wiek: "))
        
        # Sprawdź użytkownika pod kątem kwalifikowalności
        required_age = movies[movie][0]
        
        if age >= required_age:
            
            # Jeśli użytkownik znajduje się w grupie docelowej, sprawdź dostępność miejsc
            tickets = movies[movie][1]
            
            # Jeśli liczba dostępnych miejsc jest wartością dodatnią, zmiejsz pulę dostępnych miejsc o 1
            if tickets > 0:
                movies[movie][1] -= 1
                print("Bilet zakupiony! Pozostało miejsc:", movies[movie][1])
            else:
                print("Brak dostępnych biletów na ten film.")
        
        else:
            print("Nie spełniasz kryterium wiekowego dla tego filmu.")
    
    else:
        print("Nie ma takiego filmu w repertuarze.")
