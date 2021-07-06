import matplotlib.pyplot as plt
import warnings
import numpy as np

#mydata = np.arange(0, 20)

# print(mydata)


#print(np.reshape(mydata, (5, 4), order='C'))

#Matriz2 = np.reshape(mydata, (5, 4), order='F')

# print(Matriz2)

#print(Matriz2[2, 2])


#-----------------Numpy Array -----------#
# Primero creamos un par de listas


Players = ["Alejandro", "Campero", "Angel", "Dilan",
           "Estudillo", "Nava", "Edgar", "Alejandro"]


dict = {"Alejandro": 0, "Campero": 1, "Angel": 2, "Dilan": 3,
        "Estudillo": 4, "Nava": 5, "Edgar": 6, "Alejandro": 7}
col = {"Alejandro": "Black", "Campero": "Green", "Angel": "Yellow", "Dilan": "Blue",
       "Estudillo": "Gray", "Nava": "Pink", "Edgar": "Red", "Alejandro": "Brown"}

r1 = [10, 20, 30, 40, 50, 60, 100, 70]
r2 = [30, 31, 32, 33, 34, 35, 36, 37]
r3 = [80, 81, 82, 83, 84, 85, 86, 87]

r4 = [40, 41, 42, 43, 44, 45, 46, 47]

r5 = [51, 52, 53, 54, 55, 56, 70, 57]
r6 = [100, 101, 102, 103, 104, 105, 150, 107]

r7 = [58, 59, 60, 61, 62, 63, 80, 65]
r8 = [70, 71, 72, 73, 74, 75, 76, 77]


# Poner listas entre las listas
#[r1, r2, Players]

# funcion np.array

Juegos = np.array([r1, r2, r3, r4, r5, r6, r7, r8])
Puntos = np.array([r5, r6, r7, r8, r1, r2, r3, r4])

warnings.filterwarnings('ignore')

# print(np.matrix.round(Juegos/Puntos))
print(Puntos)


####----------------Visualizacion-----------------####

""" plt.plot(Puntos[0], c='Red', ls=':', marker='D', ms='10', label=Players[0])
plt.plot(Puntos[1], c='Blue', ls='--', marker=5, ms='10', label=Players[3])
plt.plot(Puntos[2], c='Black', ls='dashdot',
         marker='p', ms='10', label=Players[6])
plt.legend()
plt.legend(loc='upper left', bbox_to_anchor=(0, 0))
plt.xticks(list(range(0, 8)), r4, rotation='horizontal')
plt.show() """


def myplot(data, playerlist):
    for name in playerlist:
        plt.plot(data[dict[name]], c=col[name], ls=':',
                 marker='D', ms='10', label=Players[dict[name]])

    plt.legend()
    ''' plt.legend(loc='upper left', bbox_to_anchor=(0, 0)) '''
    plt.xticks(list(range(0, 8)), r4, rotation='horizontal')
    plt.show()


myplot(Juegos, ["Alejandro", "Dilan", "Edgar"])
