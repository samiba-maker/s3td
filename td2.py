import math
import matplotlib.pyplot as plt
import numpy as np


def f(x, a=2):
    return x**2 - a  # on def f(x)


def df_f(x):
    return 2*x  # on def df_f(x)


def df_n(x, h=0.1):
    return (f(x + h) - f(x))/h


def newton_list(x0=10.0):
    NMAX = 1000
    eps = 0.0001
    n = 0
    x = x0
    lxn = [x0]
    while n < NMAX and abs(f(x)) > eps:
        x = x - f(x)/df_f(x) 
        lxn.append(x)
        n = n + 1  
    return lxn


def list_of_absc(xmin=0, xmax=10, nb=25):
    l = [xmin]
    n = 0 
    x = xmin
    pas = (xmax-xmin)/(nb-1)
    NMAX = nb-2
    while n < NMAX:
        x = x + pas
        l.append(x)
        n = n + 1
    l.append(xmax)
    return l 
    


if __name__ == "__main__":
    xinit = input("Donner l'abscisse initiale (un réel) : ")
    xinit = float(xinit)

    # Les traitements
    lxn = newton_list(xinit)
    print("Resultat de x^2 = 2 => x = {}".format(lxn[-1]))

    # Création de la figure avec un axe
    fig, ax = plt.subplots()

    # Affichage de quelques points de la fonction f
    lab = list_of_absc()
    # print("list of abscisses = {}".format(lab))
    ax.plot(lab, [f(x) for x in lab], ".b-", label="f(x)")

    # Affichage des abscisses de Newton-Raphson
    ax.plot(lxn, [0 for x in lxn], "gd", label="NR abs")
    
    for i in range(len(lxn) - 1):  # parcourt les estimations voisines
        xi = lxn[i]  # estimation actuelle
        x_suivant = lxn[i + 1]  # estimation suivante
        ax.plot([xi, x_suivant], [f(xi), 0], "r--")  # trace tangente en points rouges

    for i, x_i in enumerate(lxn):
        ax.plot([x_i, x_i], [0, f(x_i)], "k:")  # Verticale en pointillés
        ax.annotate(
            "x{}".format(i),                    # Étiquette x0, x1, ...
            (x_i, 0),
            xytext=(0, -15),
            textcoords="offset points",
            ha="center"
    )
    # Décoration de la figure
    ax.set(
        xlabel="x",
        ylabel="f(x)",
        title="Newton Raphson v1 sur $x^2 - 2 = 0$"
    )
    ax.grid()
    ax.legend()

    # Enregistrement et affichage
    fig.savefig("td2.png")
    plt.show()