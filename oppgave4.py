"""Oppg 4)
a) Opprett en dictionary som gitt under. Dictionaryen har ulike land som nøkkel (Keys)
og gir info om hovedstaden i landet og antall innbyggere i mill. i hovedstaden.


b) Lag et program som ber brukeren skrive inn et land (eksempelvis England).
Programmet skal på bakgrunn av dette skrive ut følgende setning:
London er hovedstaden i England og det er 8.982 mill. innbyggere i London


c) Lag et program som ber brukeren skrive inn info om et nytt land (altså et land som
ikke allerede finnes i dictionaryen data). Videre skal brukeren oppgi hovedstad og
antall innbyggere for det «nye» landet. Programmet skal så utvide/oppdatere
dictionaryen med den nye informasjonen. Dictionaryen data skrives så til skjerm."""


data={"Norge":["Oslo", 0.634],
      "England":["London", 8.982],
      "Frankrike":["Paris", 2.161],
      "Italia":["Roma", 2.873],
      }

print()
print("Du kan velge mellom følgende land:")
for land in data:
    print(land, end=", ")

print()
velg_land = input("Skriv inn et land: ").title()
if velg_land not in data:
    print("Du har ikke valgt et gyldig land")
else:
    valgt_land= data.get(velg_land)
    print(
        f"{valgt_land[0]} er hovedstaden i {velg_land} og det er {valgt_land[1]} mill. innbyggere i {valgt_land[0]}"
    )


print()
legg_inn_nytt_land= input("Vil du legge inn et nytt land? Skriv J for Ja og N for Nei (J/N): ").lower()
if legg_inn_nytt_land =="j":
    nytt_land = input("Skriv inn et nytt land: ").title()
    ny_hovedstad = input("Skriv inn hovedstaden i landet: ").title()
    ny_innbyggere = float(input("Skriv inn antall innbyggere i mill: "))
    data[nytt_land]=[ny_hovedstad, ny_innbyggere]
    print()
    print("Oppdatert liste over land:")
    print(data)
elif legg_inn_nytt_land == "n":
    print("Du valgte å ikke legge inn et nytt land")
else:
    print("Ha en flott dag")
