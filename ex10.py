propozitie_intrare = input("Introduceți propoziția: ")
subsir_tinta = input("Introduceți subșirul țintă: ")
subsir_inlocuire = input("Introduceți subșirul de înlocuire: ")
propozitie_inlocuita = propozitie_intrare.replace(subsir_tinta, subsir_inlocuire)
print("Propoziția înlocuită:", propozitie_inlocuita)