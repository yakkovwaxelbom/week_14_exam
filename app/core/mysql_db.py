import mysql.connector
from core.settings import setting
from core.errors import (MySQLAlreadyExist,
                         MySQLGeneralError,
                         MySQLNotExist,
                         SQLSchemaNotExist)

class SQL_Manager:
    cnx = None

    @classmethod
    def connect(cls):
        if cls.cnx is not None:
            raise MySQLAlreadyExist(f'{setting.MYSQL_HOST}:{setting.MYSQL_PORT}')
        
        cls.cnx = mysql.connector.connect(
            host=setting.MYSQL_HOST, 
            port=setting.MYSQL_PORT,
            user=setting.MYSQL_USER,
            password=setting.MYSQL_PASSWORD)
        
    @classmethod
    def close(cls):
        if cls.cnx is None:
            raise MySQLNotExist(f'{setting.MYSQL_HOST}:{setting.MYSQL_PORT}')
        
        cls.cnx.close()
        


    @classmethod
    def bad_init(cls):

        path = 'sql\schema.sql'

        try:
            with open(path, 'r') as f:

                queries = f.read().split(';')

        except FileNotFoundError:
            raise SQLSchemaNotExist(path)

        for query in queries:
            try:
                    cls.cnx.cursor().execute(query.strip())
                    cls.cnx.commit()
                    print("Query executed successfully!")
            except Exception as e:
                raise MySQLGeneralError(str(e))


    
def get_cursor():
    try:
        cnx = SQL_Manager.cnx
        cursor = cnx.cursor(dictionary=True)
        yield cursor
        cnx.commit()
        
    except Exception as e:
        if cnx:
            cnx.rollback()
        raise MySQLGeneralError(str(e))
    
    finally:
        if cursor:
            cursor.close()
