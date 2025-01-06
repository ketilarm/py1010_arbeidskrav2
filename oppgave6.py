"""Oppg 6) Skriv en kode som plotter funksjonen f(x) = -x2 - 5, for x på intervallet [-10,10].
Hint: np.linspace(-10, 10, 200) gir en array med 200 punkter jevnt fordelt på intervallet
."""



import numpy as np
import matplotlib.pyplot as plt

x=np.array([-10,10])
# fx = -x**2-5


def f(x):
    return -x**2-5

xa = np.linspace(-10,10,200)

plt.close('all')
plt.plot(xa,f(xa))
plt.show()

