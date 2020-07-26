import os
import pandas as pd
import sqlite3
import psycopg2
from dotenv import load_dotenv

load_dotenv()

df = pd.read_csv("titanic.csv")

conn = sqlite3.connect("titanic.sqlite3")
curs = conn.cursor()
#df.to_sql('titanic', con=conn)
print(curs.execute("SELECT COUNT(*) FROM titanic;").fetchall())

dbname = os.getenv('dbname')
user = os.getenv('user')
password = os.getenv('password')
host = os.getenv('host')

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)

pg_curs = pg_conn.cursor()

sl_conn = sqlite3.connect('titanic.sqlite3')
sl_curs = sl_conn.cursor()

pg_curs.execute("""DROP TABLE IF EXISTS titanic;""")
pg_conn.commit()

create_titanic_table = """
CREATE TABLE titanic (
  index SERIAL PRIMARY KEY,
  Survived INT,
  Pclass INT,
  Name TEXT,
  Sex TEXT,
  Age REAL,
  Siblings_Spouses_Aboard INT,
  Parents_Children_Aboard INT,
  Fare REAL
);
"""

pg_curs = pg_conn.cursor()
pg_curs.execute(create_titanic_table)
pg_conn.commit()

sl_curs.execute(""" UPDATE titanic
SET Name = REPLACE(Name, "'", ' '); """)

get_person = 'SELECT * FROM titanic;'
people = sl_curs.execute(get_person).fetchall()


for person in people:
    insert_person = """
    INSERT INTO titanic
    (Survived,Pclass,Name,Sex,Age,Siblings_Spouses_Aboard,Parents_Children_Aboard,fare)
    VALUES """ + str(person[1:]) + ";"
    pg_curs.execute(insert_person)

pg_conn.commit()