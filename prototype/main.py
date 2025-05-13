def optellen(a, b):
    return a + b 

def aftrekken(a, b):
    return a - b

def vermeningvuldigen(a, b):
    return a * b

def delen(a, b):
    if b == 0:
        return "Fout: kan niet delen door nul."
    return a / b

def rekenmachine():
    print("Welkom bij de Pyhton Rekenmachine")
    while True:
        try:
            getal1 = float(input("Voer het eerst getal in: "))
            bewerking = input("Kies een bewerking (+, -, *, /): ")
            getal2 = float(input("Voer het tweede getal in: "))

            if bewerking == "+":
                resultaat = optellen(getal1, getal2)
            elif bewerking == "-":
                resultaat = aftrekken(getal1, getal2)
            elif bewerking == "*":
                resultaat = vermeningvuldigen(getal1, getal2)
            elif bewerking == "/":
                resultaat = delen(getal1, getal2)
            else:
                print("Ongeldige bewerking. Kies uit +, -, *, /")
                continue

            print(f"Het resultaat is: {resultaat}")

        except ValueError:
            print("Ongeldige invoer. Voer alleen getallen in.")

rekenmachine()