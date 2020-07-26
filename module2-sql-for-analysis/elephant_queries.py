import os
import psycopg2
import sqlite3
from dotenv import load_dotenv

load_dotenv()

s1_conn = sqlite3.Connection('rpg_db.sqlite3')
sl_cursor = s1_conn.cursor()
characters = sl_cursor.execute('select * from charactercreator_character LIMIT 10').fetchall()
print(characters)

create_character_table_query = '''
CREATE TABLE IF NOT EXISTS rpg_characters (
    chracter_id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    level INT,
    exp INT,
    hp INT,
    strength INT,
    intelligence INT,
    dexterity INT,
    wisdom INT
)
'''
dbname = os.getenv('dbname')
user = os.getenv('user')
password = os.getenv('password')
host = os.getenv('host')

conn = psycopg2.connect(dbname = dbname, user = user, password = password, host = host)
cursor = conn.cursor()

cursor.execute(create_character_table_query)
conn.commit()

### Insert in POSTGRES ###

for character in characters:
    insert_query = f''' INSERT INTO rpg_characters
    (chracter_id, name, level, exp, hp, strength, intelligence, dexterity, wisdom) VALUES
    {character}
    '''
cursor.execute(insert_query)

conn.commit()