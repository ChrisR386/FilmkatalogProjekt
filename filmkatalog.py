filme = {}  # Dictionary zum Speichern der Filme: Titel -> Details

def filme_anzeigen():
    if not filme:
        print("Der Katalog ist leer.")
        return

    print("\n--- Dein Filmkatalog ---")
    for titel, details in filme.items():
        print(f"Titel: {titel}")
        print(f"  Regisseur: {details.get('regisseur', 'N/A')}")
        print(f"  Jahr: {details.get('jahr', 'N/A')}")
        print("-----------------------")

def film_hinzufuegen():
    print("\n--- Film hinzufügen ---")
    titel = input("Titel des Films: ")
    regisseur = input("Regisseur des Films: ")
    jahr = input("Erscheinungsjahr des Films: ")

    if titel in filme:
        print(f"Fehler: Film '{titel}' existiert bereits im Katalog.")
        return

    filme[titel] = {
        "regisseur": regisseur,
        "jahr": jahr
    }
    print(f"Film '{titel}' wurde hinzugefügt.")

def film_suchen():
    print("\n--- Film suchen ---")
    suchbegriff = input("Geben Sie einen Suchbegriff für den Titel ein: ").lower()
    gefundene_filme = {}

    for titel, details in filme.items():
        if suchbegriff in titel.lower():
            gefundene_filme[titel] = details

    if not gefundene_filme:
        print(f"Keine Filme gefunden, die '{suchbegriff}' im Titel enthalten.")
        return

    print(f"\n--- Gefundene Filme für '{suchbegriff}' ---")
    for titel, details in gefundene_filme.items():
        print(f"Titel: {titel}")
        print(f"  Regisseur: {details.get('regisseur', 'N/A')}")
        print(f"  Jahr: {details.get('jahr', 'N/A')}")
        print("-----------------------")

def zeige_menue():
    print("\n--- Filmkatalog Menü ---")
    print("1. Film hinzufügen")
    print("2. Filme anzeigen")
    print("3. Film suchen")
    print("4. Beenden")
    print("------------------------")

def main():
    while True:
        zeige_menue()
        wahl = input("Ihre Wahl: ")

        if wahl == '1':
            film_hinzufuegen()
        elif wahl == '2':
            filme_anzeigen()
        elif wahl == '3':
            film_suchen()
        elif wahl == '4':
            print("Programm wird beendet. Auf Wiedersehen!")
            break
        else:
            print("Ungültige Eingabe. Bitte versuchen Sie es erneut.")

if __name__ == "__main__":
    main()
