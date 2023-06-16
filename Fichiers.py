def nbMotsAvecVoyelle(nomf):
    voyelles = ['a', 'e', 'i', 'o', 'u']
    nb_mots = 0

    try:
        with open(nomf, 'r') as fichier:
            for ligne in fichier:
                mot = ligne.strip().lower()
                if mot[0] in voyelles:
                    nb_mots += 1

    except FileNotFoundError:
        print(f"Le fichier '{nomf}' est introuvable.")

    return nb_mots
