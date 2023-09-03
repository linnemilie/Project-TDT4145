

import datetime
import sqlite3

# Koble til databasen

conn = sqlite3.connect('database.db')
c = conn.cursor()
cursor = conn.cursor()

bestillingsdato = datetime.date.today()

# Introsetning
input("Velkommen! Dette programmet lar deg kjøpe billetter for en togrute gitt en ønsket togrute, dato, vognnummer og plasser. Trykk 'Enter' for å gå videre.")


# While-løkke som vil fortsette frem til brukerinput for rutenavn finnes i databasen.
# Riktige rutenavn er 'Tro-Bod-dag', 'Tro-Bod-natt' og 'Mo-Tro-morg'
while True:
    rutenavn = input("Oppgi rutenavn: ")
    rutenavn_parts = rutenavn.split("-")
    rutenavn = "-".join([part.capitalize() if i < 2 else part for i, part in enumerate(rutenavn_parts)])
    exists_query = f'SELECT rutenavn FROM togrute where rutenavn = "{rutenavn}"'
    exists_cursor = conn.execute(exists_query)
    exists_result = exists_cursor.fetchone()
    if exists_result is None:
        print("Beklager, denne ruten finnes ikke i databasen vår. Vennligst forsøk på nytt. Våre ruter er: Tro-Bod-dag, Tro-Bod-natt, og Mo-Tro-morg.")
        continue
    break

# Hjelpefunksjoner for håndtering av dato til ukedag
def dateToWeekday(dato_string):
    days = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag", "Lørdag", "Søndag"]
    dato = datetime.datetime.strptime(dato_string, '%Y-%m-%d')
    ukedag = days[dato.weekday()]
    return ukedag

# While løkke som vil gå frem til brukerinput for dato enten er 3. eller 4. april 2023
while True:
    dato = input("Hvilken dato ønsker du reise på? Datoen må være på formatet YYYY-MM-DD: ")
    try:
        datetime.datetime.strptime(dato, '%Y-%m-%d')
        break
    except ValueError:
        print("Feil format! Datoen må være på formatet YYYY-MM-DD. Vennligst skriv inn reisedato på nytt.")
if dato not in ['2023-04-03', '2023-04-04']:
    print(f"Beklager, vi selger ikke billetter den dagen. Vi har kun billetter for 3. og 4. april")
    conn.close()    
    exit()
ukedag = dateToWeekday(dato)
   

# Sjekker om brukerinput for endestasjon finnes i databasen
while True:
    startstasjon = input("Hvor vil du reise fra? ").capitalize()

    exists_query = f'SELECT EXISTS(SELECT 1 FROM jernbanestasjon WHERE stasjonsnavn = "{startstasjon}")'
    exists_cursor = conn.execute(exists_query)
    exists_result = exists_cursor.fetchone()[0]
    if exists_result == 0:
        print(f"Beklager, jernbanestasjonen {startstasjon} finnes ikke i databasen.")
        continue
    break

# Sjekker om brukerinput for endestasjon finnes i databasen
while True:
    endestasjon = input("Hvor vil du reise til? ").capitalize()

    exists_query = f'SELECT EXISTS(SELECT 1 FROM jernbanestasjon WHERE stasjonsnavn = "{endestasjon}")'
    exists_cursor = conn.execute(exists_query)
    exists_result = exists_cursor.fetchone()[0]
    if exists_result == 0:
        print(f"Beklager, jernbanestasjonen {endestasjon} finnes ikke i databasen.")
        continue
    break

# Funksjon som henter ut ankomsttiden for en oppgitt stasjon
def getStationTime(stasjonsnavn):
    query = f"""
        SELECT ankomsttid
        FROM mellomstasjon
        WHERE rutenavn = "{rutenavn}" and stasjonsnavn = "{stasjonsnavn}"
        UNION
        SELECT avgangstid
        FROM togrute
        WHERE rutenavn = "{rutenavn}" and startstasjon = "{stasjonsnavn}"
        UNION
        SELECT ankomsttid
         FROM togrute
        WHERE rutenavn = "{rutenavn}" and endestasjon = "{stasjonsnavn}"
    """
    cursor.execute(query)
    # Håndterer av natt-tog fra Trondheim S 
    time = cursor.fetchone()[0]
    if (time == '23:05:00'):
        time = '00:00:00'
    return time

# Feilhåndtering dersom toget ankommer startstasjon etter endestasjon
if getStationTime(startstasjon) > getStationTime(endestasjon):
    print(f"{rutenavn} ruten går i motsatt retning. Denne togruten går ikke fra {startstasjon} til {endestasjon}")
    conn.close()
    exit()

# Hente ut antall distinkte vognnummer for togreisen med det oppgitte rutenavnet og ukedagen
query = f"""
    SELECT COUNT(DISTINCT vognnummer)
    FROM billett
    WHERE rutenavn = "{rutenavn}" and ukedag = "{ukedag}"
"""
cursor.execute(query)
num_vognnummer = cursor.fetchone()[0]

# Hvis det ikke er noen vogner, skal den printe feilmelding og slutte programmet
if num_vognnummer == 0:
    print("Sorry, no results")
    conn.close()
    exit()

# Print the number of distinct vognnummer and ask the user to choose a vognnummer
print(f"There are {num_vognnummer} unique vognnummer for {rutenavn} on {ukedag}")
vognnummer = input("Choose a vognnummer: ")

# Henter oppsettID til den oppgitte ruten
query = f"""
    select oppsettID from togreise
    WHERE rutenavn = '{rutenavn}'
"""
cursor.execute(query)
oppsettID = cursor.fetchone()[0]

# Henter vognID til den vognen bruker hae valgt
query = f"""
   SELECT distinct vognID
    FROM vognIOppsett
    JOIN togreise on vognIOppsett.oppsettID = togreise.oppsettID
    WHERE vognIOppsett.oppsettID = '{oppsettID}' and vognnummer = '{vognnummer}';
"""
cursor.execute(query)
vognID = cursor.fetchone()[0]

# Sjekker om vogn er sovevogn eller sittevogn. Her har vi definert vogner som starter på 'S' som sovevogner
if 'S' in vognID:
    vogntype = 'sove'
    print("Du har valgt en sovevogn!")
else:
    vogntype = 'sitte'
    print("Du har valgt en sittevogn!")

# Spørring som returnerer alle ledige plasser gitt all den oppgitte informasjonen
query = f"""
    SELECT plassnummer
    FROM billett
    WHERE rutenavn = '{rutenavn}' AND ukedag = '{ukedag}' AND vognnummer = '{vognnummer}' AND NOT EXISTS (
        SELECT billettID FROM seteErOpptatt 
        WHERE billett.billettID = seteErOpptatt.billettID)

    UNION 

    SELECT plassnummer
    FROM seteOpptatt
    JOIN seteErOpptatt
    ON seteOpptatt.opptattID = seteErOpptatt.opptattID
    JOIN billett
    ON seteErOpptatt.billettID = billett.billettID
    WHERE (
    CAST(endetid AS DATETIME) <= CAST('{getStationTime(startstasjon)}' AS DATETIME) 
    or CAST('{getStationTime(endestasjon)}' AS DATETIME)<= CAST(starttid AS DATETIME))
    AND startstasjon != '{startstasjon}'
    AND endestasjon != '{endestasjon}'
    AND rutenavn = '{rutenavn}';
    """
cursor.execute(query)
ledige_plasser = cursor.fetchall()

print(f"Her er de ledige plassene i vogn {vognnummer}: {ledige_plasser}")

plasser = input(f"Hvilke plasser vil du ha? (x, y, z, ...)")

# Setter plasser_list lik plassene bruker har valgt
plasser_list = [int(p.strip()) for p in plasser.split(",")]

def remove_duplicates(lst):
    return list(set(lst))

# Kalles dersom vogn er sovevogn
# Håndterer logikk for å reserverer reserve-senger i en sovekupé
def occupyNextBed(ListNUmbers):
    temporaryList = []
    for plassnummer in ListNUmbers:
        if (plassnummer % 2 == 0):
            temporaryList.append(plassnummer)
            temporaryList.append(plassnummer-1)
        elif(plassnummer % 2 != 0):
            temporaryList.append(plassnummer+1)
            temporaryList.append(plassnummer)
    temporaryList = remove_duplicates(temporaryList)
    return temporaryList

# henter ut alle plasser i reservasjonen som IKKE ble valgt av brukeren
# kun om vogn er sovevogn
if vogntype == 'sove':
    seatsNotOrdered = []
    for p in occupyNextBed(plasser_list):
        if p not in plasser_list:
            seatsNotOrdered.append(p)
    # plasser_list = occupyNextBed(plasser_list)

# Bruker input for mobilnummer
mobilnumber = input("Oppgi telefonnummeret ditt: ")

# Sjekker om kunde med {mobilnummer} eksisterer i kunderegisteret
query = f"""
    SELECT kunde.kundenummer
    FROM kunde 
    JOIN kunderegister on kunde.kundenummer = kunderegister.kundenummer
    WHERE mobilnummer = "{mobilnumber}"
"""
cursor.execute(query)
result = cursor.fetchone()

# Håndtering dersom kunde ikke finnes
if result is None:
    print("Du er ikke registrert som kunde hos oss. Vennligst registrer deg i brukerhistorieC.py før du kjøper billett.")
    conn.close()
    exit()

# Kundenummer brukes når vi oppretter en kundeordre   
kundenummer = result[0]

# Funksjon for å hente ut ordrenummer
# setter lastrowid lik verdien til ordrenummeret i den siste raden + 1
def getOrdrenummer():
        cursor = conn.cursor()
        query = """
        SELECT COALESCE(MAX(ordrenummer), 0) + 1
        FROM kundeordre
        """
        cursor.execute(query)
        lastrowid = cursor.fetchone()[0]
        if lastrowid is None:
            return 1
        else:
            return lastrowid

ordrenummer = getOrdrenummer()

 # Henter ut opptattID
  # Fungerer på samme måte som da vi hentet ut ordrenummer 
def getOpptattID():
    cursor = conn.cursor()
    query = """
     SELECT COALESCE(MAX(opptattID), 0) + 1
     FROM seteErOpptatt
     """
    cursor.execute(query)
    lastrowid = cursor.fetchone()[0]
    if lastrowid is None:
        return 1
    else:
        return lastrowid

# For alle plasser som blir markert som opptatt men som IKKE er med i kundeordren
# Plassene blir lagt til i seteErOpptatt og seteOpptatt, men ikke i billettkjøp eller kundeordre
# Kun om sovevogn ()

if vogntype == 'sove':
    for plass in seatsNotOrdered:
        query = f"""
        SELECT billettID
        FROM billett
        WHERE rutenavn = "{rutenavn}" and ukedag = "{ukedag}" and vognnummer = "{vognnummer}" and plassnummer = "{plass}"
        """
        cursor.execute(query)
        billettID = cursor.fetchone()[0]
  
        opptattID = getOpptattID()
   
   # Legge inn plass i seteOpptatt og seteErOpptatt
        c.execute("INSERT INTO seteOpptatt (opptattID, startstasjon, endestasjon, starttid, endetid) VALUES (?, ?, ?, ?, ?)", (opptattID, startstasjon, endestasjon, getStationTime(startstasjon), getStationTime(endestasjon)))
        c.execute("INSERT INTO seteErOpptatt (billettID, opptattID) VALUES (?, ?)", (billettID, opptattID))

# For alle plassene som bruker har valgt
# Disse plassene blir med i kundeordre og billettkjøp, i tillegg til å bli satt som opptatt i seteErOpptatt og seteOpptatt
for plass in plasser_list:
    query = f"""
    SELECT billettID
    FROM billett
    WHERE rutenavn = "{rutenavn}" and ukedag = "{ukedag}" and vognnummer = "{vognnummer}" and plassnummer = "{plass}"
    """
    cursor.execute(query)
    billettID = cursor.fetchone()[0]

    opptattID = getOpptattID()

    c.execute("INSERT INTO billettkjøp (billettID, ordrenummer) VALUES (?, ?)", (billettID, ordrenummer))
    c.execute("INSERT INTO seteOpptatt (opptattID, startstasjon, endestasjon, starttid, endetid) VALUES (?, ?, ?, ?, ?)", (opptattID, startstasjon, endestasjon, getStationTime(startstasjon), getStationTime(endestasjon)))
    c.execute("INSERT INTO seteErOpptatt (billettID, opptattID) VALUES (?, ?)", (billettID, opptattID))

# Lage en kundeordre utenfor for-loopen som inkluderer alle billettkjøpene bruker har gjennomført
c.execute("INSERT INTO kundeordre (ordrenummer, bestillingsdato, kundenummer, startstasjon, endestasjon) VALUES (?, ?, ?, ?, ?)", (ordrenummer, bestillingsdato, kundenummer, startstasjon, endestasjon))

#Suksess-melding til bruker
print(f"Billettkjøp gjennomført! Du har kjøpt plasser {plasser_list} fra {startstasjon} til {endestasjon} den {dato}!")

# Lukke koblingen
conn.commit()
conn.close()
