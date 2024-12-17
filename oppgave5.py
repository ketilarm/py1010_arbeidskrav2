"""Oppg 5) Lag et program med en funksjon som tar a og b som inn-argumenter og som så
regner ut arealet og «ytre» omkrets til en figur satt sammen av en rettvinklet trekant og en
halvsirkel, se figuren under. Med «ytre» omkrets menes samlet lengde av de sorte strekene.
Funksjonen skal returnere arealet og «ytre» omkrets, som så skrives til skjerm med passende
tekst.



Areal sirkel = pi*r^2
Omkrets sirkel = 2*pi*r
Areal trekant = (g*h)/2
Omkrets trekant = a+b+c
"""
import numpy as np


print(np.pi)


def utregning_areal_og_omkrets(a,b):
    # Utreginger sirkel
    r=(a/2)
    areal__halv_sirkel=(np.pi*(r**2))/2
    omkrets_halv_sirkel=2*np.pi*r
    # print(f"Areal halvsirkel: {areal__halv_sirkel}")
    # print(f"Omkrets halvsirkel: {omkrets_halv_sirkel}")

    # utregninger trekant
    g=a
    h=b
    hyppotenusen = np.sqrt(a**2 + b**2)
    areal_trekant=(g*h)/2
    omkrets_trekant=(b+hyppotenusen)

    # print(f"Areal trekant: {areal_trekant}")
    # print(f"Omkrets trekant: {omkrets_trekant}")

    total_areal_halvsirkel_trekant=areal__halv_sirkel+areal_trekant
    total_omkrets_halvsirkel_trekant=omkrets_halv_sirkel+omkrets_trekant
    return total_areal_halvsirkel_trekant, total_omkrets_halvsirkel_trekant

total_areal_halvsirkel_trekant, total_omkrets_halvsirkel_trekant=(
    utregning_areal_og_omkrets(2, 3)
)


print(f"Totalt areal av halvsirkel og trekant: {total_areal_halvsirkel_trekant}")
print(f"Totalt omkrets av halvsirkel og trekant: {total_omkrets_halvsirkel_trekant}")
