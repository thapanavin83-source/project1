
import mysql.connector
from geopy.distance import geodesic

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123",
    database="airports",
    autocommit=True,
)

def get_airport_corordinates(icao_code):
   SQL = f"SELECT latitude_deg, longitude_deg FROM flight WHERE ident = '{icao_code}'"
   SQL_cursor = connection.cursor()
   SQL_cursor.execute(SQL)
   result = SQL_cursor.fetchone()
   return result


def run_airport_distance():
    icao_code1 = input("Enter the ICAO code of the first airport: ").upper()
    icao_code2 = input ("Enter the ICAO code of the second airport: ").upper()
    airport1_coordinates = get_airport_corordinates(icao_code1)
    airport2_coordinates = get_airport_corordinates(icao_code2)
    distance = geodesic(airport1_coordinates, airport2_coordinates).km
    print (f"Distance between {icao_code1} and {icao_code2}: {distance:0.2f} kilometres")

run_airport_distance()
