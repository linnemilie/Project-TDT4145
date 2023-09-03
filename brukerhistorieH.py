
import sqlite3
import datetime
import re

# Tilkobling til database
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Introsetning
input("Velkommen! Dette programmet gir deg informasjon om alle kjøpene du har gjort for fremtidige reiser . Trykk 'Enter' for å gå videre.")

# mobilnummer = input("Vennligst skriv inn ditt telefonnummer som du har logget inn med ")
# #TODO: validate phonenumber


# Brukerinput for mobilnummer og validering
# Antar at vi kun har norske mobilnummer

while True:
    mobilnummer = input("Vennligst skriv inn ditt telefonnummer som du har logget inn med. ")
    if not re.match(r"^[0-9]{8}$", mobilnummer):
        print("Feil tlf format. Nummeret ditt må ha 8 siffer.")
    else:
        break

# Sjekker om det finnes en kunde registrert med dette telefonnummeret
query = f'''
    SELECT kundenummer FROM kunde WHERE mobilnummer = "{mobilnummer}"
'''
c.execute(query)
existing_customer = c.fetchone()

# Feilhåndtering dersom kunde allerede eksisterer
if not existing_customer:
    print("Det finnes ingen kunder som er registrert med dette mobilnummeret")
    conn.close()
    exit()

# SQL spørring
query = f'''
SELECT b.vognnummer, b.plassnummer, b.reisedato, startstasjon, endestasjon
FROM kunde
INNER JOIN kundeordre AS ko on kunde.kundenummer = ko.kundenummer
INNER JOIN billettkjøp AS bk on ko.ordrenummer = bk.ordrenummer
INNER JOIN billett AS b on bk.billettID = b.billettID
WHERE kunde.mobilnummer = '{mobilnummer}'
AND reisedato >= CURRENT_DATE;
'''

cursor = conn.execute(query)

results = cursor.fetchall()
if results:
    print("\n")
    print("Dine fremtidige reiser:")
    print("-------------------------------------------------------------------------------")
    print("{:<15} {:<15} {:<15}{:<15}{:<15}".format("Vognnummer:", "Plassnummer:", "Reisedato:", "Påstigning:", "Avstigning:"))
    for row in results:
        print("{:<15} {:<15} {:<15}{:<15}{:<15}".format(row[0], row[1], row[2], row[3], row[4]))
    print("\n")
else:
    print(f"Du har ingen kommende reiser registrert på dette telefonnummeret. \n ")

# Lukker tilkobling
conn.close()