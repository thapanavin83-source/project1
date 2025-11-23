import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123",
    database="airports",
    autocommit=True,

)

cursor = connection.cursor()

icao_code = input("Enter the ICAO code of an airport: ").upper()

query = f"SELECT name, municipality FROM flight WHERE ident = '{icao_code}'"
cursor.execute(query)

result = cursor.fetchone()

if result:
    airport_name, location = result
    print(f"Airport name: {airport_name}")
    print(f"Location: {location}")
else:
    print("Airport not found.")