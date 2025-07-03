filme = {} 
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
filme_anzeigen()