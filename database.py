import os
import mysql.connector as connector

## Initialise Connection
connection = connector.connect(
    user="root",
    password="testpassword",
    host="localhost",
    database="mulesoft")

if(connection):
    print("Connection Successfull!!!")
else:
    print("Connection Failed :-(")

mycursor = connection.cursor()

## Creating a Table
def create_table():
    mycursor.execute("CREATE TABLE movies (title VARCHAR(50), actor CHAR(35), actress CHAR(50), director CHAR(35), year_of_release INT)")

## Insert Data into Table
def insert_values(title,actor,actress,director,year):
    query = "INSERT INTO demo VALUES (%s, %s, %s, %s, %s)"
    values = (title,actor,actress,director,year,)
    mycursor.execute(query,values)
    connection.commit()

## Get All Details
def get_all():
    query = "SELECT * from movies"
    mycursor.execute(query)
    for x in mycursor:
        print(x)

## Get Movie by actor name
def get_movie_by_actor(actor):
    query = "SELECT title from movies WHERE actor = %s"
    values = (actor,)
    mycursor.execute(query,values)
    for x in mycursor:
        print(x)

#### MAIN ####
get_all()
get_movie_by_actor("Leonardo DiCaprio")


connection.close()