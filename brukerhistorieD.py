
from calendar import weekday
import sqlite3
import datetime
import time


# Hjelpefunksjoner for håndtering av dato til ukedag
def dateToWeekday(dato_string):
    days = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag", "Lørdag", "Søndag"]
    dato = datetime.datetime.strptime(dato_string, '%Y-%m-%d')
    ukedag = days[dato.weekday()]
    return ukedag

def getNextWeekday(ukedag):
    nesteDagDict = {
        'Mandag': 'Tirsdag',
        'Tirsdag': 'Onsdag',
        'Onsdag': 'Torsdag',
        'Torsdag': 'Fredag',
        'Fredag': 'Lørdag',
        'Lørdag': 'Søndag',
        'Søndag': 'Mandag'
    }
    nesteDag = nesteDagDict[ukedag]
    return nesteDag


# Koble til database
conn = sqlite3.connect('database.db')

# Introsetning
input(" Velkommen! \n Dette programmet lar deg søke etter togruter som går mellom en ønsket start og stopp-stasjon på en valgt dato og klokkeslett. \n Du vil også få opp togrutene som går dagen etter.  \n Husk å skrive stor forbokastav i alle inputene. \n Trykk 'Enter' for å starte programmet.")



# Brukerinput for dato med feilhåndtering
while True:
    dato = input("Skriv inn dato du ønsker å reise. Datoen må være på formatet YYYY-MM-DD: ")
    try:
        datetime.datetime.strptime(dato, '%Y-%m-%d')
        break
    except ValueError:
        print("Feil format! Datoen må være på formatet YYYY-MM-DD. Vennligst skriv inn reisedato på nytt.")
ukedag = dateToWeekday(dato)


# Brukerinput for startstasjon og feilhåndtering
while True:
    startstasjon = input("Skriv inn stasjonen du ønsker å gå på toget: ").strip().capitalize()
    startstasjon = startstasjon[:1] + startstasjon[1:].lower()
  # sjekker om startstasjon eksisterer i jernbanestasjon-tabellen
    exists_query = f'SELECT EXISTS(SELECT 1 FROM jernbanestasjon WHERE stasjonsnavn = "{startstasjon}")'
    exists_cursor = conn.execute(exists_query)
    exists_result = exists_cursor.fetchone()[0]
    if exists_result == 0:
        print(f"Beklager, jernbanestasjonen {startstasjon} finnes ikke i databasen.")
        continue
    break

# Brukerinput for klokkeslett med feilhåndtering
while True:
    klokkeslett = input("Skriv inn klokkeslettet når du ønsker å reise fra stasjonen. Oppgi klokkeslett på formen TT:MM:SS: ")
    try:
        time.strptime(klokkeslett, '%H:%M:%S')
        break
    except ValueError:
        print("Feil format! Klokkeslettet må være på formen TT:MM:SS. Prøv igjen.")

# Brukerinput for sluttstasjon og feilhåndtering
while True:
    sluttstasjon = input("Skriv inn stasjonen du ønsker å reise til: ").strip().capitalize()
    sluttstasjon = sluttstasjon[:1] + sluttstasjon[1:].lower()
  # sjekker om sluttstasjon eksisterer i jernbanestasjon-tabellen
    exists_query = f'SELECT EXISTS(SELECT 1 FROM jernbanestasjon WHERE stasjonsnavn = "{sluttstasjon}")'
    exists_cursor = conn.execute(exists_query)
    exists_result = exists_cursor.fetchone()[0]
    if exists_result == 0:
        print(f"Beklager, jernbanestasjonen {sluttstasjon} finnes ikke i databasen.")
        continue
    break


nesteDag = getNextWeekday(ukedag)

# SQL spørring som returnerer togruter går mellom startstasjon og endestasjon på en gitt dato, og neste dag, sortert på tid. 

query = '''
SELECT rutenavn, ankomsttid, ukedag
FROM (
  SELECT togreise.rutenavn, togrute.avgangstid as ankomsttid, togreise.ukedag,
         0 AS ukedagsort, NULL AS stasjonsnavn, NULL AS avgangstidSort
  FROM togreise
  INNER JOIN togrute ON togrute.rutenavn = togreise.rutenavn
  WHERE ((togreise.ukedag = "{}" and togrute.avgangstid >= "{}") or togreise.ukedag = "{}")
  AND togrute.startstasjon = "{}"
  AND togrute.endestasjon = "{}"
  
  UNION
  
  SELECT togr.rutenavn, startm.ankomsttid AS ankomsttid, togr.ukedag,
         1 AS ukedagsort, startm.stasjonsnavn, startm.ankomsttid AS avgangstidSort
  FROM togreise AS togr
  INNER JOIN mellomstasjon AS startm ON togr.rutenavn = startm.rutenavn
  INNER JOIN mellomstasjon AS sluttm ON togr.rutenavn = sluttm.rutenavn
  WHERE (togr.ukedag = "{}" and startm.ankomsttid >= "{}"
  OR togr.ukedag = "{}")
  AND startm.stasjonsnavn = "{}"
  AND sluttm.stasjonsnavn = "{}"
  AND CAST(startm.ankomsttid AS DATETIME) < CAST(sluttm.ankomsttid AS DATETIME)
  
  UNION 
  
 SELECT togreise.rutenavn, togrute.avgangstid AS ankomsttid, togreise.ukedag,
        2 AS ukedagsort, sluttm.stasjonsnavn, sluttm.ankomsttid AS avgangstidSort
 FROM togreise 
 INNER JOIN mellomstasjon as sluttm ON togreise.rutenavn = sluttm.rutenavn
 INNER JOIN togrute ON (togreise.rutenavn = togrute.rutenavn)
 WHERE ((togreise.ukedag = "{}" and togrute.avgangstid >= "{}") or togreise.ukedag = "{}")
 AND togrute.startstasjon = "{}"
 AND sluttm.stasjonsnavn = "{}"
 
 UNION 
 
SELECT togreise.rutenavn,  startm.ankomsttid AS ankomsttid, togreise.ukedag, 
	3 AS ukedagsort, startm.stasjonsnavn, startm.ankomsttid AS avgangstidSort
FROM togreise
INNER JOIN mellomstasjon as startm ON togreise.rutenavn = startm.rutenavn
INNER JOIN togrute ON togreise.rutenavn = togrute.rutenavn
WHERE (togreise.ukedag = "{}" and startm.ankomsttid >= "{}" or togreise.ukedag = "{}")
AND startm.stasjonsnavn = "{}"
AND togrute.endestasjon = "{}"
  
) AS subquery
ORDER BY
CASE ukedag
WHEN "{}" THEN 1
ELSE 2
END,
ankomsttid ASC;
'''.format(ukedag, klokkeslett, nesteDag, startstasjon, sluttstasjon,
    ukedag, klokkeslett, nesteDag, startstasjon, sluttstasjon,
    ukedag, klokkeslett, nesteDag, startstasjon, sluttstasjon,
    ukedag, klokkeslett, nesteDag, startstasjon, sluttstasjon,
    ukedag
     )

cursor = conn.execute(query)

results = cursor.fetchall()

# Resultat fra spørring med formatering
if results:
    print("{:<15} {:<15} {:<10}".format("Rutenavn", "Ankomsstid", "Dag")) #TODO: endre til avgangsstid? idk
    for row in results:
        print("{:<15} {:<15} {:<10}".format(row[0], row[1], row[2]))
else:
    print(f"Beklager, det finnes ingen togruter som passerer gjennom valgte stasjoner.")

# Lukke tilkobling
conn.close()

