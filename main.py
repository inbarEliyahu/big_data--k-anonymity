import csv
import sqlite3

from queue import Queue

def main():
    con = sqlite3.connect("adult.db")
    cur = con.cursor()

    file = open("adult.csv")
    writen_file = csv.reader(file)
    cur.execute("CREATE TABLE adult (age, relationship, race, gender);")
    cur.executemany("INSERT INTO adult   VALUES  (?, ?, ?, ?)", writen_file)


    cur.execute("SELECT * FROM adult")
    print(cur.fetchall())
    dimension_tables_set={"age", "relationship", "race", "gender"}
    k = input("enter a k:")
    quasi_identifier_set = {"age", "relationship", "race", "gender"}
    queue =  Queue(maxsize = 0)
    for i in quasi_identifier_set:


    con.commit()
    con.close()


main()
