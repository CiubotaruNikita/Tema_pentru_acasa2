sir = input("Introduceți un șir de caractere: ")
numar_total_litere = len(sir)
space=sir.count(" ")
numar_vocale = sir.lower().count("a") + sir.lower().count("e") \
               + sir.lower().count("i") + sir.lower().count("o") + sir.lower().count("u")
numar_consoane = numar_total_litere - numar_vocale - space
print("Numărul total de litere în carctere:", numar_total_litere)
print("Numărul de vocale în șir:", numar_vocale)
print("Numărul de consoane în șir:", numar_consoane)

