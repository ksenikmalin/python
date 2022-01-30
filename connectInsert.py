from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="std-mysql.ist.mospolytech.ru",
        user="std_717_repairs",
        password="Valera22@",
        database="std_717_repairs",
    ) as connection:
        insert_lighting_query = "INSERT INTO lighting (id_status, id_sensor, date) VALUES (1, 4, '2008-10-23 10:37:22')"
        with connection.cursor() as cursor:
            cursor.execute(insert_lighting_query)
            connection.commit()
except Error as e:
    print(e)





