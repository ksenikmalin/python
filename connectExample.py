from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="std-mysql.ist.mospolytech.ru",
        user="std_717_repairs",
        password="Valera22@",
        database="std_717_repairs",
    ) as connection:
        select_lighting_query = "Select  * from lighting Where id_sensor = 4 order by date desc limit 1"
        with connection.cursor() as cursor:
            cursor.execute(select_lighting_query)
            result = cursor.fetchall()
            for row in result:
                print(row)
except Error as e:
    print(e)





