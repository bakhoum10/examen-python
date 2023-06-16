class Personne:
    def __init__(self, nom, prenom, numero_rue, numero_telephone, code_postal, ville):
        self.nom = nom
        self.prenom = prenom
        self.numero_rue = numero_rue
        self.numero_telephone = numero_telephone
        self.code_postal = code_postal
        self.ville = ville

def saisie_tab():
    annuaire = []
    nb_entries = int(input("Combien d'entrées voulez-vous ajouter à l'annuaire ? "))

    for i in range(nb_entries):
        print(f"\n--- Saisie de l'entrée {i+1} ---")
        nom = input("Nom: ")
        prenom = input("Prénom: ")
        numero_rue = input("Numéro dans la rue: ")
        numero_telephone = input("Numéro de téléphone: ")
        code_postal = input("Code postal: ")
        ville = input("Ville: ")
        personne = Personne(nom, prenom, numero_rue, numero_telephone, code_postal, ville)
        annuaire.append(personne)

    return annuaire

def critere_recherche():
    print("\n--- Critères de recherche ---")
    print("1. Nom")
    print("2. Prénom")
    print("3. Numéro de rue")
    print("4. Numéro de téléphone")
    print("5. Code postal")
    print("6. Ville")

    choix = input("Choisissez le critère de recherche : ")
    return choix

def recherche(annuaire, critere):
    valeur_recherche = input(f"Entrez la valeur de recherche pour le critère {critere}: ")
    resultats = []

    for personne in annuaire:
        if critere == "1" and valeur_recherche.lower() == personne.nom.lower():
            resultats.append(True)
        elif critere == "2" and valeur_recherche.lower() == personne.prenom.lower():
            resultats.append(True)
        elif critere == "3" and valeur_recherche == personne.numero_rue:
            resultats.append(True)
        elif critere == "4" and valeur_recherche == personne.numero_telephone:
            resultats.append(True)
        elif critere == "5" and valeur_recherche == personne.code_postal:
            resultats.append(True)
        elif critere == "6" and valeur_recherche.lower() == personne.ville.lower():
            resultats.append(True)
        else:
            resultats.append(False)

    return resultats

def affiche_tab(annuaire, resultats):
    print("\n--- Résultats de recherche ---")

    for personne, resultat in zip(annuaire, resultats):
        if resultat:
            print("Nom :", personne.nom)
            print("Prénom :", personne.prenom)
            print("Numéro dans la rue :", personne.numero_rue)
            print("Numéro de téléphone :", personne.numero_telephone)
            print("Code postal :", personne.code_postal)
            print("Ville :", personne.ville)
            print("-----------------------")

# Programme principal
annuaire = saisie_tab()

print("\n--- Recherche dans l'annuaire ---")
critere = critere_recherche()
resultats = recherche(annuaire, critere)
affiche_tab(annuaire, resultats)
