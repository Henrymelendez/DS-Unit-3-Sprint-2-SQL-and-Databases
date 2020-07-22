import pandas as pd
import sqlite3

CONN = sqlite3.connect('buddymove_holidayiq.sqlite3')
cursor = CONN.cursor()

df = pd.read_csv('buddymove_holidayiq.csv')

df.to_sql('review', CONN, if_exists = 'replace', index = False)

query1 = 'SELECT count(*) FROM review'
cursor.execute(query1)
print(f'Number of Rows: {cursor.execute(query1).fetchall()[0][0]}')

query2 = '''SELECT count(*)
            FROM review
            WHERE Nature >= 100 and Shopping >=100;'''
cursor.execute(query2)

print(f'users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping: {cursor.execute(query2).fetchall()[0][0]}')