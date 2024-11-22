from whisky import WhiskyKlasse

print("Hello World and Whisky is great")

def main():
    # Erstelle eine Instanz von MeineKlasse
    taliskerWhisky = WhiskyKlasse("Talisker","smoky","Scotland")

    # Nutze eine Methode der Klasse
    print(f"Name: {taliskerWhisky.GetName()}")
    print(f"Taste: {taliskerWhisky.GetTaste()}")
    print(f"Country: {taliskerWhisky.GetCountry()}")


# Main Funktion ausführen
if __name__ == "__main__":
    main()