"""Oppg 1) Du skal her lage et program som skal starter med
alder = int(input('Hvilket år er du født? ') )
Programmet skal så regne ut hvor gammel personen blir nå i løpet av år 2024 og skrive
svaret til skjerm med passende tekst"""

import datetime
# Henter dagens år istden for å hardkode det til 2024
year_now = datetime.datetime.now().year
# spør bruker om hvilket år de er født
alder = int(input("Hvilket år er du født? "))

print(f"Du blir i løpet av {year_now} {year_now - alder} år gammel.")
