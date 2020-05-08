import pymysql
import datetime

from Person import Person
from Vehicle import Vehicle


def create_connection():
    mydb = None
    try:
        mydb = pymysql.connect("lefti.cm.upt.ro", "garbanlarisa", "madalina_111", "starwars")
        return mydb
    except BaseException as e:
        if not (mydb is None):
            mydb.close()
        print("Nu s-a putut face conexiunea")


def get_int(message):
    nr = -1
    try:
        nr = int(input(message))
    except BaseException as exception:
        print("Textul introdus nu este un numar")
        return get_int(message)
    return nr


def get_date(message):
    print(message)
    year = get_int('Introduceti anul:')
    month = get_int('Introduceti luna:')
    day = get_int('Introduceti ziua: ')
    date1 = datetime.date(year, month, day)

    return date1


def get_index(people_name_array, name):
    length = len(people_name_array)
    for i in range(length):
        if people_name_array[i] == name:
            return i
    return -1


def get_gender():
    nr = -1
    while nr != 1 and nr != 2:
        print("Introduceti 1 daca persoana este barbat")
        print("Introduceti 2 daca persoana este femeie")
        nr = get_int("Introduceti numarul: ")

    if nr is 1:
        return "male"
    else:
        return "female"


def get_vehicles_with_person_ID(id):
    mydb = None
    my_cursor = None
    try:
        vehicle_array = []
        mydb = create_connection()
        my_cursor = mydb.cursor()
        my_cursor.execute("SELECT * FROM people_vehicles WHERE peopleID=%s", id)
        vehicle_fields_array = my_cursor.fetchall()
        for vehicle_fields in vehicle_fields_array:
            vehicle = Vehicle(vehicle_fields[0], vehicle_fields[1], vehicle_fields[2])
            vehicle_array.append(vehicle)
            return vehicle_array
    except BaseException as ex:
        mydb.close()
        my_cursor.close()
        print(ex)
        return None


def get_starships_with_person_id(id):
    mydb = None
    my_cursor = None
    try:
        starship_array = []
        mydb = create_connection()
        my_cursor = mydb.cursor()
        my_cursor.execute("SELECT * FROM people_starships WHERE peopleID=%s", id)
        starship_fields_array = my_cursor.fetchall()
        for starship_fields in starship_fields_array:
            vehicle = Vehicle(starship_fields[0], starship_fields[1], starship_fields[2])
            starship_array.append(vehicle)
            return starship_array
    except BaseException as ex:
        mydb.close()
        my_cursor.close()
        print(str(ex))
        return None


def get_persoane_care_se_numesc():
    name = input("Introduceti numele persoanei respective: ")

    mydb = create_connection()
    my_cursor = mydb.cursor()

    try:
        my_cursor.execute("SELECT * FROM people  WHERE people_name = %s", name)
        people_fields_array = my_cursor.fetchall()
        for people_fields in people_fields_array:
            person = Person(people_fields[0], people_fields[1], people_fields[2], people_fields[3],
                            people_fields[4], people_fields[5], people_fields[6], people_fields[7],
                            people_fields[8], people_fields[9], people_fields[10])
            person.add_vehicles(get_vehicles_with_person_ID(person.peopleID))
            person.add_starships(get_starships_with_person_id(person.peopleID))
            print(str(person))
    except BaseException as ex:
        mydb.close()
        my_cursor.close()
        print(str(ex))


def get_persoane_dupa_anul_nasterii():
    an = input("Introduceti anul nasterii: ")

    mydb = create_connection()
    my_cursor = mydb.cursor()

    try:
        my_cursor.execute("SELECT * FROM people  WHERE people_birth_year = %s", an)
        people_fields_array = my_cursor.fetchall()
        if len(people_fields_array) is 0:
            raise Exception("Nu este nimeni in baza de date cu anul nasterii" + str(an))

        for people_fields in people_fields_array:
            person = Person(people_fields[0], people_fields[1], people_fields[2], people_fields[3],
                            people_fields[4], people_fields[5], people_fields[6], people_fields[7],
                            people_fields[8], people_fields[9], people_fields[10])
            person.add_vehicles(get_vehicles_with_person_ID(person.peopleID))
            person.add_starships(get_starships_with_person_id(person.peopleID))
            print(str(person))
    except BaseException as ex:
        mydb.close()
        my_cursor.close()
        print(str(ex))


def afisare_dupa_people_gender(gender):
    mydb = create_connection()
    my_cursor = mydb.cursor()

    try:
        my_cursor.execute("SELECT * FROM people  WHERE people_gender = %s", gender)
        people_fields_array = my_cursor.fetchall()
        if len(people_fields_array) is 0:
            raise Exception('Nu este niciun barbat in baza de date')

        for people_fields in people_fields_array:
            person = Person(people_fields[0], people_fields[1], people_fields[2], people_fields[3],
                            people_fields[4], people_fields[5], people_fields[6], people_fields[7],
                            people_fields[8], people_fields[9], people_fields[10])
            person.add_vehicles(get_vehicles_with_person_ID(person.peopleID))
            person.add_starships(get_starships_with_person_id(person.peopleID))
            print(str(person))
    except BaseException as ex:
        mydb.close()
        my_cursor.close()
        print(str(ex))


def afiseaza_persoane_cu_cel_putin_un_vehicul():
    mydb = create_connection()
    my_cursor = mydb.cursor()

    try:
        my_cursor.execute("SELECT people_name FROM people "
                          "INNER JOIN people_vehicles "
                          "ON people.peopleID = people_vehicles.peopleID")
        people_names = my_cursor.fetchall()

        people_name_array = []
        nr_vehicles_array = []

        for person_name in people_names:
            index = get_index(people_name_array, person_name[0])
            if index is -1:
                people_name_array.append(person_name[0])
                nr_vehicles_array.append(1)
            else:
                nr_vehicles_array[index] += 1

        for i in range(len(people_name_array)):
            print(people_name_array[i] + " has " + str(nr_vehicles_array[i]) + " vehicles")
    except BaseException as ex:
        mydb.close()
        my_cursor.close()
        print(str(ex))


def afiseaza_persoanele_cu_cel_putin_un_starship():
    mydb = create_connection()
    my_cursor = mydb.cursor()

    try:
        my_cursor.execute("SELECT people_name FROM people "
                          "INNER JOIN people_starships "
                          "ON people.peopleID = people_starships.peopleID")
        people_names = my_cursor.fetchall()

        people_name_array = []
        nr_starships_array = []

        for person_name in people_names:
            index = get_index(people_name_array, person_name[0])
            if index is -1:
                people_name_array.append(person_name[0])
                nr_starships_array.append(1)
            else:
                nr_starships_array[index] += 1

        for i in range(len(people_name_array)):
            print(people_name_array[i] + " has " + str(nr_starships_array[i]) + " starships")
    except BaseException as ex:
        mydb.close()
        my_cursor.close()
        print(str(ex))


def get_people_with_at_least_one_vehicle_and_one_starship():
    mydb = create_connection()
    my_cursor = mydb.cursor()

    try:
        my_cursor.execute("SELECT people.people_name, COUNT(people_vehicles.peopleID) AS VEHICLE_NUMBER, "
                          "COUNT(people_starships.peopleID) AS STARSHIP_NUMBER"
                          " FROM people"
                          " LEFT JOIN people_vehicles ON people_vehicles.peopleID = people.peopleID"
                          " LEFT JOIN people_starships ON people_starships.peopleID = people.peopleID"
                          " GROUP BY people.people_name"
                          " HAVING COUNT(people_vehicles.peopleID) > 0 AND COUNT(people_starships.peopleID) > 0"
                          " ORDER BY COUNT(people_vehicles.peopleID) DESC")
        results = my_cursor.fetchall()

        if len(results) is 0:
            print("There is nobody with one starship and one vehicle")

        for result in results:
            print("          " + result[0] + " has " + str(result[1]) + " vehicles and " + str(result[2]) + " starships")
    except BaseException as ex:
        mydb.close()
        my_cursor.close()
        print(str(ex))
