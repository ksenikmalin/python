from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="std-mysql.ist.mospolytech.ru",
        user="std_717_repairs",
        password="Valera22@",
        database="std_717_repairs",
    ) as connection:
        update_query = "UPDATE lighting SET date = now() WHERE id = 6"
        with connection.cursor() as cursor:
            cursor.execute(update_query)
            connection.commit()
except Error as e:
    print(e)





