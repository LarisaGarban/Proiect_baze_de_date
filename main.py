from utility_module import get_int, get_persoane_care_se_numesc, \
    get_persoane_dupa_anul_nasterii, afisare_dupa_people_gender,\
    afiseaza_persoane_cu_cel_putin_un_vehicul, afiseaza_persoanele_cu_cel_putin_un_starship

while True:
    print("Introduceti 1 daca doriti sa afisati o anumita persoana cu vehiculele si starship-urile aferente dupa nume")
    print("Introduceti 2 daca doriti sa afisati anumite persoane cu vehiculele si starship-urile aferente dupa anul "
          "nasterii" )
    print("Introduceti 3 daca doriti sa afisati persoanele care au cel putin un vehicul" )
    print("Introduceti 4 daca doriti sa afisati persoanele care au cel putin un starship" )
    print("Introduceti 5 daca doriti sa afisati toti barbatii din baza de date cu vehiculele aferente " )
    print("Introduceti 6 daca doriti sa afisati toate femeile din baza de date cu vehiculele aferente " )
    print("Introduceti orice alt numar  daca doriti sa iesiti din aplicatie")

    optiune = get_int ( "Introduceti optiunea dumneavoastra: " )

    if optiune is 1:
        get_persoane_care_se_numesc()
    elif optiune is 2:
        get_persoane_dupa_anul_nasterii()
    elif optiune is 3:
        afiseaza_persoane_cu_cel_putin_un_vehicul()
    elif optiune is 4:
        afiseaza_persoanele_cu_cel_putin_un_starship()
    elif optiune is 5:
        afisare_dupa_people_gender('male')
    elif optiune is 6:
        afisare_dupa_people_gender ('female')
    else:
        break



