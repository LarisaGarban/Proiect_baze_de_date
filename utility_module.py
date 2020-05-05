import pymysql
import datetime


def create_connection() :
    mydb = None
    try :
        mydb = pymysql.connect ( "lefti.cm.upt.ro" , "garbanlarisa" , "madalina_111" , "starwars" )
        print ( "Conexiunea a functionat" )
        return mydb
    except BaseException as e :
        if not (mydb is None) :
            mydb.close ( )
        print ( "Nu s-a putut face conexiunea" )


def get_int(message) :
    nr = -1
    try :
        nr = int ( input ( message ) )
    except BaseException as exception :
        print("Textul introdus nu este un numar")
        return get_int ( message )
    return nr


def get_date(message) :
    print ( message )
    year = get_int ( 'Introduceti anul:' )
    month = get_int ( 'Introduceti luna:' )
    day = get_int ( 'Introduceti ziua: ' )
    date1 = datetime.date ( year , month , day )

    return date1


def get_gender() :
    nr = -1
    while nr != 1 and nr != 2 :
        print ( "Introduceti 1 daca persoana este barbat" )
        print ( "Introduceti 2 daca persoana este femeie" )
        nr = get_int ( "Introduceti numarul: " )

    if nr is 1 :
        return "male"
    else :
        return "female"


def adauga_persoana_noua() :
    mydb = create_connection ( )
    name = input ( "Introduceti numele persoanei: " )
    height = get_int ( "Introduceti inaltimea persoanei in centimetri: " )
    mass = get_int ( "Introduceti greutatea persoanei in kiligrame: " )
    hair_color = input ( "Introduceti culoarea parului a persoanei: " )
    skin_color = input ( "Introduceti culoarea pielii a persoanei: " )
    eye_color = input ( 'Culoarea ochilor: ' )
    birth_year = get_int ( "Introduceti anul nasterii persoanei respective: " )
    gender = get_gender ( )
    homeworld_id = get_int ( "Introduceti indetificatorul lumii persoanei: " )
    species_id = get_int ( "Introduceti identificatorul speciei persoanei: " )

    my_cursor = mydb.cursor ( )

    try :
        my_cursor.execute ( "INSERT INTO people ("
                            "people_name ,"
                            " people_height,"
                            " people_mass , "
                            "people_hair_color , "
                            "people_skin_color , "
                            "people_eye_color,"
                            " people_birth_year,"
                            " people_gender,"
                            " people_homeworld_id, "
                            "people_species_id)"
                            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" ,
                            (name ,
                             height ,
                             mass ,
                             hair_color ,
                             skin_color ,
                             eye_color ,
                             birth_year ,
                             gender ,
                             homeworld_id ,
                             species_id ,
                             ) )

        mydb.commit ( )

    except BaseException as ex :
        print ( str ( ex ) )
    mydb.close ( )


def sterge_persoana():
    name = input("Introduceti numele persoanei: ")
    birth_year = get_int("Introduceti anul nasterii persoanei: ")

    mydb = create_connection()
    my_cursor = mydb.cursor()
    try:
        my_cursor.execute("DELETE FROM pople WHERE people_name=%s AND people_birth_year=%s", name, birth_year)
        count = my_cursor.rowcount
        mydb.commit()
        print("Au fost sterse " + str( count ) + " inregistrari din baza de date")
    except BaseException as ex:
        print( ex )

    mydb.close()