import csv
import sqlite3


def main():
    con = sqlite3.connect("adult.db")
    cur = con.cursor()

    file = open("adult.csv")
    writen_file = csv.reader(file)
    cur.execute("CREATE TABLE adult (age, relationship, race, gender);")
    cur.executemany("INSERT INTO adult   VALUES  (?, ?, ?, ?)", writen_file)


    cur.execute("SELECT * FROM adult")
    print(cur.fetchall())

    con.commit()
    con.close()


main()
