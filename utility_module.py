import pymysql

def create_connection() :
    try :
        mydb = pymysql.connect ( "lefti.cm.upt.ro" , "garbanlarisa" , "madalina_111" , "starwars" )
        print("Conexiunea a functionat")
        return mydb
    except BaseException as e :
        mydb.close ( )
        raise Exception ( "Nu s-a putut face conexiunea" )


