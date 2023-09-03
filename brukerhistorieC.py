
import sqlite3

# Koble til database

conn = sqlite3.connect('database.db')
c = conn.cursor()
cursor = conn.cursor()

# Introsetning
input("Velkommen! Dette programmet returnerer alle togruter som passerer gjennom en gitt togstasjon på en gitt dag. Trykk 'Enter' for å gå videre.")

# Brukerinput for stasjonsnavn og feilhåndtering
while True:
  stasjonsnavn = input("Oppgi stasjonsnavn: ").strip().capitalize()
  stasjonsnavn = stasjonsnavn[:1] + stasjonsnavn[1:].lower()
  # sjekker om stasjonsnavn eksisterer i jernbanestasjon-tabellen
  exists_query = f'SELECT EXISTS(SELECT 1 FROM jernbanestasjon WHERE stasjonsnavn = "{stasjonsnavn}")'
  exists_cursor = conn.execute(exists_query)
  exists_result = exists_cursor.fetchone()[0]
  if exists_result == 0:
    print(f"Beklager, jernbanestasjonen {stasjonsnavn} finnes ikke i databasen.")
    continue
  break

# Brukerinput for ukedag og feilhåndtering
while True:
  ukedag = input("Oppgi ukedag (Mandag, Tirsdag, osv.): ").capitalize()
  ukedager = ['Mandag', 'Tirsdag', 'Onsdag', 'Torsdag', 'Fredag', 'Lørdag', 'Søndag']
  if ukedag not in ukedager:
      print("Ugyldig ukedag. Vennligst prøv igjen.")
      continue
  break

# SQL spørring som returnerer alle ruter som passerer gjennom {stasjonsnavn} på den gitte ukedagen
query = f'''SELECT DISTINCT m.rutenavn
FROM mellomstasjon AS m
  JOIN togreise AS t
    ON m.rutenavn = t.rutenavn
  WHERE m.stasjonsnavn = "{stasjonsnavn}"
    AND t.ukedag = "{ukedag}"
  UNION
  SELECT DISTINCT r.rutenavn
  FROM togrute AS r
  JOIN togreise AS t
    ON r.rutenavn = t.rutenavn
  WHERE (r.startstasjon = "{stasjonsnavn}" OR r.endestasjon = "{stasjonsnavn}")
  AND t.ukedag = "{ukedag}";'''

cursor = conn.execute(query)
results = cursor.fetchall()
    
if results:
    print(f"Her er togrutene som passerer gjennom {stasjonsnavn} på {ukedag.lower()}er:")
    for row in results:
        print(row[0])
    # Hvis spørringen returnerer null:
else:
    print(f"Beklager, det finnes ingen togruter som passerer gjennom {stasjonsnavn} på {ukedag.lower()}er.")

# Lukke tilkobling til database
conn.close()
