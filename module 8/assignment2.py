
import mysql.connector

def get_airports_by_country(country_code):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123",
        database="airports",
        autocommit=True,
    )
    SQL = f"SELECT type, COUNT(*) as airport_count FROM flight WHERE iso_country='{country_code}' GROUP BY type ORDER BY airport_count DESC"
    SQL_cursor = connection.cursor()
    SQL_cursor.execute(SQL)
    result= SQL_cursor.fetchall()
    return result

def run_country_program():
    country_code = input("Enter country code (e.g., FI for Finland): ").upper()
    airports = get_airports_by_country(country_code)
    print (f"Airports in {country_code}:")
    for airport in airports:
        print(f"{airport[1]} {airport[0]} airports")

run_country_program()
