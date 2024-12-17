import random

# creation de la focntion  creer_personnage
def creer_personnage(nom:str, classe="guerrier", niveau=1, points_de_vie=100):
    return {
        "nom": nom,
        "classe": classe,
        "niveau": niveau,
        "points_de_vie": points_de_vie,
        "inventaire": [
            {"nom": "potion de soin", "quantite": 3}
        ]
    }

# creation de la fonction ajouter_objet()
def ajouter_objet(inventaire, objet_nom, quantite):
    for objet in inventaire:
        if objet["nom"] == objet_nom:
            objet["quantite"] += quantite
            return
    inventaire.append({"nom": objet_nom, "quantite": quantite})

# creation de la fonction modifier_statistiques() --> type de  parametre : dict   
def modifier_statistiques(personnage):
    personnage["niveau"] += 1
    personnage["points_de_vie"] += 20

#creation de la focntion utiliser_potion() --> type de parametre: dict 
def utiliser_potion(personnage):
    for objet in personnage["inventaire"]:
        if objet["nom"] == "potion de soin" and objet["quantite"] > 0:
            soin = random.randint(1, 50)
            personnage["points_de_vie"] += soin
            objet["quantite"] -= 1
            print(f"{personnage['nom']} a utilisé une potion de soin et a récupéré {soin} points de vie!")
            return
    print(f"{personnage['nom']} n'a pas de potion de soin!")

#creation de la fonction afficher_personnage()  --> type de parametre : dict  
def afficher_personnage(personnage):
    print(f"Nom : {personnage['nom']}")
    print(f"Classe : {personnage['classe']}")
    print(f"Niveau : {personnage['niveau']}")
    print(f"Points de vie : {personnage['points_de_vie']}")
    print("Inventaire :")
    for objet in personnage["inventaire"]:
        print(f"  - {objet['nom']} : {objet['quantite']}")

#creation de la focntion attaquer() --> type de parametre -->dict,dict  
def attaquer(joueur1, joueur2):
    degats = 10 * joueur1["niveau"]
    joueur2["points_de_vie"] -= degats
    print(f"{joueur1['nom']} attaque {joueur2['nom']} et inflige {degats} points de dégâts!")

    if joueur2["points_de_vie"] <= 0:
        print(f"{joueur2['nom']} a été vaincu!")
        joueur1["inventaire"].extend(joueur2["inventaire"])
        joueur2["inventaire"] = []

def menu():
    personnage1 = creer_personnage(input("Entrez le nom du premier personnage : "))
    personnage2 = creer_personnage(input("Entrez le nom du second personnage : "))

    while True:
        print('|==================================================================================|')
        print("|\t\t               Menu                                                |")
        print("|\t\t1.  Afficher les détails du personnage 1                           |")
        print("|\t\t2.  Afficher les détails du personnage 2                           |")
        print("|\t\t3.  Ajouter un objet à l'inventaire du personnage 1                |")
        print("|\t\t4.  Utiliser une potion pour le personnage 1                       |")
        print("|\t\t5.  Le personnage 1 attaque le personnage 2                        |")
        print("|\t\t6.  Modifier les statistiques du personnage 1                      |")
        print("|\t\t7.  Quitter                                                        |")
        print("|\t\t               Fin du menu                                         |")
        print('|==================================================================================|')

        choix = input("\n\nChoisissez une option : ")

        if choix == "1":
            afficher_personnage(personnage1)
        elif choix == "2":
            afficher_personnage(personnage2)
        elif choix == "3":
            objet_nom = input("Nom de l'objet : ")
            quantite = int(input("Quantité : "))
            ajouter_objet(personnage1["inventaire"], objet_nom, quantite)
        elif choix == "4":
            utiliser_potion(personnage1)
        elif choix == "5":
            attaquer(personnage1, personnage2)
        elif choix == "6":
            modifier_statistiques(personnage1)
        elif choix == "7":
            print("Au revoir!")
            break
        else:
            print("Veillez entrer une option valide !!!!!!!.")

if __name__ == '__main__': 
    menu()
