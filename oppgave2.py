"""Oppg 2) Det skal arrangeres en klassefest og man antar at hver elev spiser 1/4 pizza. Lag et
program som tar inn antall elever fra konsollen ved
antall_elever = int(input('Skriv inn antall elever:' ))
Programmet skal så regne ut hvor mange pizzaer som skal handles inn til festen og skrive
svaret til skjerm. Merk, man kan ikke kjøpe 4 og en kvart pizza på butikken (man må da kjøpe
5).
Hint1: Gir programmet ditt et fornuftig svar hvis det f.eks er 21 elever i klassen?
Hint2: Det er ikke vanlig å si/skrive: ‘Det må handles inn 6.0 pizzaer til festen’. Hvordan kan
sikre at antall pizzaer skrives ut som et heltall (ikke desimaltall)?"""


antall_elever = int(input("Skriv inn antall elever:"))

#Sjekker om resultatet av antall pizaer som trengs blir et partall eller oddetall med modulo operatoren
pizza_rest = antall_elever % 4

#Regner ut antall pizzaer som trengs til festen og legger til 1 dersom pizza rest = 1
antall_pizza = (antall_elever / 4)+pizza_rest

print(f"Det må handles inn {antall_pizza:.0f} pizzaer til festen.")

