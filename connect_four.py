import tkinter
import random
import copy

couleur_joueurs = ["red", "yellow"]
couleur_victoire = ["firebrick", "gold"]
couleur_plateau = "blue"
couleur_fond = "white"
taille_fenetre = (1200, 650)  # largeur / hauteur
taille_rectangles = (115, 600)

x0 = (taille_fenetre[0] - 7 * taille_rectangles[0]) / 2
y0 = (taille_fenetre[1] - taille_rectangles[1]) / 2

jeux_contre_ordinateur = False
nombre_de_simulation = 200


def dessin_cercle(x, y, r, colone, couleur):  # de centre x,y et de rayon r
    can.create_oval(x - r, y - r, x + r, y + r, outline="black", fill=couleur, tag=colone)


def dessin_rectangle(x, y, colone):  # largeur et hauteur changeable au début du programme
    can.create_rectangle(x, y, x + taille_rectangles[0], y + taille_rectangles[1], outline="black",
                         fill=couleur_plateau, tag=colone)


def dessin_plateau():
    for i in range(0, 7):
        dessin_rectangle(x0 + i * taille_rectangles[0], y0, i)
    for i in range(0, 7):
        for j in range(0, 6):
            dessin_cercle(x0 + taille_rectangles[0] / 2 + taille_rectangles[0] * i,
                          y0 + taille_rectangles[1] / 12 + taille_rectangles[1] / 6 * j,
                          taille_rectangles[1] / 12 * 0.9, i, couleur_fond)


def change_joueur(joueur_actuel):
    if joueur_actuel == 1:
        return 2
    elif joueur_actuel == 2:
        return 1


def initialisation():
    global joueur, joueur_ordinateur, plateau, victoire
    dessin_plateau()
    joueur = 1
    joueur_ordinateur = change_joueur(joueur)
    plateau = []
    for i in range(0, 7):
        plateau.append([0, 0, 0, 0, 0, 0])
    victoire = False


def trouver_pion_libre(tablier, colone):
    trouve = False
    pion = 5  # on commence par vérifier le 7ème pion
    while not trouve and pion >= 0:
        if tablier[colone][pion] != 0:
            pion -= 1
        else:
            trouve = True
    if not trouve:
        pion = None
    return trouve, pion


def ajout_pion(tablier, colone, ligne, joueur_actuel):
    tablier[colone][ligne] = joueur_actuel
    return tablier


def dessin_ajout_pion(colone, ligne, joueur_actuel):
    dessin_cercle(x0 + taille_rectangles[0] / 2 + taille_rectangles[0] * colone,
                  y0 + taille_rectangles[1] / 12 + taille_rectangles[1] / 6 * ligne,
                  taille_rectangles[1] / 12 * 0.9, colone, couleur_joueurs[joueur_actuel-1])


def verification_de_victoire(tablier, colone, ligne):  # 4 vérif : horizontal, vertical, diag+, diag-
    couleur_a_verifier = tablier[colone][ligne]





def on_click(event):
    global joueur, plateau, victoire
    items = can.find_withtag("current")
    if len(items):
        iid = items[0]
        col = (can.itemcget(iid, "tag"))
        col = int(col[0])
        recherche = trouver_pion_libre(plateau, col)

        if recherche[0]:  # vrai si le joueur a cliqué dans une colone avec un pion libre
            plateau = ajout_pion(plateau, col, recherche[1], joueur)
            dessin_ajout_pion(col, recherche[1], joueur)
            joueur = change_joueur(joueur)




fen = tkinter.Tk()
can = tkinter.Canvas(fen, width=taille_fenetre[0], height=taille_fenetre[1], bg=couleur_fond)
can.pack()

initialisation()
print(plateau)

can.bind("<Button-1>", on_click)
fen.mainloop()
