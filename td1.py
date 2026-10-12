import math
import matplotlib.pyplot as plt

def f(x):
    return 1 + math.sin(2 * math.pi * x)  # on def f(x)

if __name__ == '__main__':

    fig, ax = plt.subplots()  # fig : figure complete ; # ax : le repere ou on trace les points

    lx=[]
    ly=[]
    t = 0.0
    while (t < 2.0):
        lx.append(t)  # Ajoute t a la liste des abscisses
        ly.append(f(t))  # Calcule f(x) et l'ajoute aux ordonnes 
        t = t + 0.05
    ax.plot(lx, ly, "ob")

ax.set(
    xlabel='time (s)', 
    ylabel='voltage (mV)',
    title='About as simple as it gets, folks')
ax.grid()  # grille 

fig.savefig("test.td1.png") # save le graph dans un fichier
plt.show()  # affichage a l'ecran


    

