propozitie_intrare = input("Introduceți propoziția: ")
propozitie_fara_punctuatie = propozitie_intrare.replace(".", "").replace(",", "").replace("?", "").replace("!", "")
print("Propoziția fără punctuație:", propozitie_fara_punctuatie)