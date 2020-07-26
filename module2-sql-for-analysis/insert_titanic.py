import os
import pandas as pd
import sqlite3
import psycopg2
from dotenv import load_dotenv

load_dotenv()


create_postgres_table1 = '''
CREATE TABLE IF NOT EXISTS titanic(
    Survived INT,
    Pclass INT,
    Name TEXT,
    Sex TEXT,
    Age Real,
    SiblingsSpousesAboard INT,
    ParentsChilderenAboard INT,
    Fare Real
)
'''
dbname = os.getenv('dbname')
user = os.getenv('user')
password = os.getenv('password')
host = os.getenv('host')

CONN = psycopg2.connect(dbname= dbname, user= user, password= password, host= host)
cursor = CONN.cursor()

create_postgres_table1 = '''
CREATE TABLE IF NOT EXISTS titanic(
    Survived INT,
    Pclass INT,
    Name TEXT,
    Sex TEXT,
    Age Real,
    SiblingsSpousesAboard INT,
    ParentsChilderenAboard INT,
    Fare Real
)
'''

cursor.execute(create_postgres_table1)

f =open(r"titanic.csv","r")
next(f)
cursor.copy_from(f,'titanic',sep=',',null='')
f.close()

query = "ALTER TABLE titanic ADD COLUMN id SERIAL PRIMARY KEY"
cursor.execute(query)
CONN.commit()