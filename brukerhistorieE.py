import sqlite3
import re

# Koble til database

conn = sqlite3.connect('database.db')
c = conn.cursor()

# Introsetning
input("Velkommen! Dette programmet lar deg registrere deg som kunde i vår database. Trykk 'Enter' for å gå videre.")

# Brukerinput for navn
while True:
    navn = input("Oppgi navnet ditt (fornavn og etternavn): ").title()
    if len(navn.split()) < 2:
        print("Vennligst oppgi både fornavn og etternavn.")
    else:
        break

# Brukerinput for epost og validering
while True:
    epost = input("Oppgi e-postadressen din: ")
    if not re.match(r"[^@]+@[^@]+\.[^@]+", epost):
        print("Feil e-post format. Vennligst prøv igjen.")
    else:
        break

# Brukerinput for mobilnummer og validering
# Antar at vi kun har norske mobilnummer
while True:
    mobilnummer = input("Oppgi telefonnummeret ditt (8 siffer): ")
    if not re.match(r"^[0-9]{8}$", mobilnummer):
        print("Feil tlf format. Nummeret ditt må ha 8 siffer.")
    else:
        break

# Sjekker om kunde allerede eksisterer 
# epost og mobilnummer må være unikt for hver kunde
c.execute("SELECT kundenummer FROM kunde WHERE epost = ? OR mobilnummer = ?", (epost, mobilnummer))
existing_customer = c.fetchone()

# Feilhåndtering dersom kunde allerede eksisterer
if existing_customer:
    print("Du er allerede registrert som kunde hos oss.")
else:
    # Legger kunden til i databasen
    c.execute("INSERT INTO kunde (navn, epost, mobilnummer) VALUES (?, ?, ?)", (navn, epost, mobilnummer))

    # Hente ut kundenummer
    kundenummer = c.lastrowid

    # Legge til kunde i kunderegisteret
    operatørID = 1  # Setter operatørID til 1 da vi kun har 1 operatør i databasen (med ID 1)
    c.execute("INSERT INTO kunderegister (operatørID, kundenummer) VALUES (?, ?)", (operatørID, kundenummer))

    # Lukke tilkobling
    conn.commit()
    conn.close()

    print("Gratulerer, du er nå registrert som kunde hos oss!")

