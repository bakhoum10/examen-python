import random

class Personne:
    def __init__(self, nom):
        self.nom = nom
        self.annee = None
        self.temps = None

def saisie():
    t = []
    while True:
        nom = input("Saisir le nom de la personne (ou 'q' pour quitter) : ")
        if nom.lower() == 'q':
            break
        personne = Personne(nom)
        t.append(personne)
    return t

def calculAnnee(t, annee_min, annee_max):
    for personne in t:
        periode_valide = False
        while not periode_valide:
            periode = input(f"{personne.nom}, choisissez une période en années entre {annee_min} et {annee_max} : ")
            try:
                annee_debut, annee_fin = map(int, periode.split('-'))
                if annee_min <= annee_debut <= annee_fin <= annee_max:
                    periode_valide = True
                    personne.annee = random.randint(annee_debut, annee_fin)
                else:
                    print("Période invalide. Réessayez.")
            except ValueError:
                print("Format de période invalide. Réessayez.")

def calculTemps(t):
    periode_saut_debut = 2012
    periode_saut_fin = 2022
    temps_saut = 10
    annee_actuelle = 2023

    for personne in t:
        annees_restantes = abs(personne.annee - annee_actuelle)
        sauts = annees_restantes // 10
        if annee_actuelle < personne.annee:
            personne.temps = sauts * temps_saut
        else:
            temps_retour = (sauts + 1) * temps_saut
            temps_attente = (annee_actuelle - personne.annee) % 10
            personne.temps = temps_retour + temps_attente

# Programme principal
t = saisie()
calculAnnee(t, -10000, 10000)
calculTemps(t)

# Affichage des résultats
for personne in t:
    print("Nom :", personne.nom)
    print("Année choisie :", personne.annee)
    print("Temps nécessaire pour revenir en 2017 :", personne.temps)
    print("-----------------------")
