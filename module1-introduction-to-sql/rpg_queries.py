import sqlite3
import pandas as pd

CONN = sqlite3.connect('rpg_db.sqlite3')
curs = CONN.cursor()

query1 = 'SELECT count(character_id) FROM charactercreator_character'
curs.execute(query1)
print(f'Total RPG characters: {curs.execute(query1).fetchall()[0][0]}')

query2 = '''SELECT count(m.character_ptr_id)-
                    (SELECT count(mage_ptr_id)
                    FROM charactercreator_necromancer) as Mage,
                            (SELECT count(character_ptr_id)
                            FROM charactercreator_cleric) AS Cleric,
                                (SELECT count(character_ptr_id)
                                FROM charactercreator_fighter) as Fighter,
                                    (SELECT count(mage_ptr_id)
                                    FROM charactercreator_necromancer) as Necromancer,
                                        (SELECT count(character_ptr_id)
                                        FROM charactercreator_thief) as Thief
            FROM charactercreator_mage as m'''

curs.execute(query2)
print(f'Total Mages: {curs.execute(query2).fetchall()[0][0]}')
print(f'Total Clerics: {curs.execute(query2).fetchall()[0][1]}')
print(f'Total Fighters: {curs.execute(query2).fetchall()[0][2]}')
print(f'Total Necromancers: {curs.execute(query2).fetchall()[0][3]}')
print(f'Total Thiefs: {curs.execute(query2).fetchall()[0][4]}')

query3 = '''SELECT count(item_id) + 
             (SELECT count(item_ptr_id)
              FROM armory_weapon) as Total_items  
            FROM armory_item'''

curs.execute(query3)
print(f'Total Items: {curs.execute(query3).fetchall()[0][0]}')

query4 = '''SELECT count(item_id) as total_items,
               (SELECT count(item_ptr_id)
                FROM armory_weapon) as Total_weapons
            FROM armory_item'''

curs.execute(query4)
print(f'Total non weapon Items:{curs.execute(query4).fetchall()[0][0]}')
print(f'Total weapon Items:{curs.execute(query4).fetchall()[0][1]}')

query5 = '''SELECT character_id, COUNT(item_id)
            FROM charactercreator_character_inventory
            GROUP BY character_id
            LIMIT 20;'''

curs.execute(query5)
print(f'Total items in first 20 players inventory: {curs.execute(query5).fetchall()}')

query6 = '''SELECT character_id, COUNT(item_id)
FROM charactercreator_character_inventory
WHERE item_id IN(SELECT item_ptr_id
                 FROM armory_weapon)
GROUP BY character_id
LIMIT 20;'''

curs.execute(query6)
print(f'number of weapons in players Inventory: {curs.execute(query6).fetchall()}')

query7 = '''SELECT avg(items) as Average_items
            FROM (SELECT count(item_id) as items
                  FROM charactercreator_character_inventory
                  GROUP BY character_id),
            charactercreator_character_inventory'''

curs.execute(query7)
print(f'Average Item per Character: {curs.execute(query7).fetchall()}')

query8 = '''SELECT count(cci.character_id) / count(aw.item_ptr_id) as average_weapon_per_character
            FROM charactercreator_character_inventory as cci,
            armory_item as ai,armory_weapon as aw
            WHERE ai.item_id = aw.item_ptr_id'''

curs.execute(query8)
print(f'Average weapon per character: {curs.execute(query8).fetchall()}')