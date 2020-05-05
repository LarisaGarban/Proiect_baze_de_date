from utility_module import get_int, adauga_persoana_noua, sterge_persoana

while True:
    print("Introduceti 1 daca doriti sa inserati o persoana in baza de date")
    print("Introduceti 2 daca doriti sa stergeti o persoana din baza de date")
    print("Introduceti orice alt numar  daca doriti sa iesiti din aplicatie")

    optiune = get_int("Introduceti optiunea dumneavoastra: ")

    if optiune is 1:
        adauga_persoana_noua()
    elif optiune is 2:
        sterge_persoana()
    else:
        break

