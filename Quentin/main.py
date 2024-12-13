from random import randint

def menu():
    print("  ==================Menu==================  ")
    print("| 1. Statistiques                          |")
    print("| 2. Inventaire                            |")
    print("| 3. Utiliser une potion de soin           |")
    print("| 4. Combat                                |")
    print("| 5. Quitter                               |")
    print("  ========================================  ")

def menu_combat():
    print("  ==================Menu==================  ")
    print("| 1. Attaquer                              |")
    print("| 2. Utiliser une potion de soin           |")
    print("| 3. Fuir                                  |")
    print("  ========================================  ")

def creer_personnage(nom, classe, niveau, points_de_vie,):
    return {
        "nom": nom,
        "classe": classe,
        "niveau": niveau,
        "points_de_vie": points_de_vie,
        "inventaire": [
            {"nom": "potion de soin", "quantité": 3},
            {"nom": "épée", "quantité": 1}
        ]
    }

personnage1 = creer_personnage("Quentin", "Guerrier", 1, 100)
personnage2 = creer_personnage("Ennemi", "Guerrier", 1, 100)

def ajouter_objet(personnage, objet):
    personnage["inventaire"].append(objet)
    return personnage

def utiliser_potion_de_soin(personnage):
    gain = randint(1, 50)
    for objet in personnage["inventaire"]:
        if objet["nom"] == "potion de soin":
            personnage["points_de_vie"] += gain
            objet["quantité"] -= 1
            if objet["quantité"] == 0:
                personnage["inventaire"].remove(objet)
            break
    print("Vous avez utilisé une potion de soin")
    print(f"Vous avez gagé {gain} points de vie")
    return personnage

def informations_personnage(personnage):
    print(f"| Nom : {personnage['nom']}")
    print(f"| Classe : {personnage['classe']}")
    print(f"| Niveau : {personnage['niveau']}")
    print(f"| Points de vie : {personnage['points_de_vie']}")

def afficher_inventaire(personnage):
    for objet in personnage["inventaire"]:
        print(f"| {objet['nom']} : {objet['quantité']}")

def combat(personnage1, personnage2):
    # menu de combat, avec les choix d'attaque, de potion, de fuite
    
    print("============== COMBAT ================")
    print(f"{personnage1['nom']} VS {personnage2['nom']}")
    menu_combat()
    choix = input("Que voulez-vous faire ? ")
    while choix != "3":
        if choix == "1":
            
            print(" ======================================================================================== ")
            degats = randint(1,10) * personnage1["niveau"]
            personnage2["points_de_vie"] -= degats

            print(f"{personnage1['nom']} attaque {personnage2['nom']} et lui inflige {degats} points de dégats")

            if personnage2["points_de_vie"] <= 0:
                personnage1["inventaire"].extend(personnage2["inventaire"])
                personnage2["inventaire"] = []
                personnage1["niveau"] += 1
                print(" ===================================== ")
                print("|          Vous avez gagné !          |")
                print(" ===================================== ")
                break

            degats = randint(1,10) * personnage2["niveau"]
            personnage1["points_de_vie"] -= degats

            print(f"{personnage2['nom']} attaque {personnage1['nom']} et lui inflige {degats} points de dégats")	

            if personnage1["points_de_vie"] <= 0:
                print(" ===================================== ")
                print("|          Vous avez perdu !          |")
                print(" ===================================== ")
                exit()

            print(" ================ STAT PV ===================== ")
            print(f"| {personnage1['nom']} : {personnage1['points_de_vie']} PV")
            print(f"| {personnage2['nom']} : {personnage2['points_de_vie']} PV")
            print(" =============================================== ")

        elif choix == "2":
            personnage1 = utiliser_potion_de_soin(personnage1)
        else:
            print(" ===================================== ")
            print("|           Choix invalide !          |")
            print(" ===================================== ")
        menu_combat()
        choix = input("Que voulez-vous faire ? ")

if __name__ == "__main__":

    menu()
    choix = input("Que voulez-vous faire ? ")

    while choix != "5":

        if choix == "1":
            print(" =======================================")
            informations_personnage(personnage1)
            print(" =======================================")
        elif choix == "2":
            print("========================================")
            afficher_inventaire(personnage1)
            print("========================================")
        elif choix == "3":
            print("========================================")
            personnage1 = utiliser_potion_de_soin(personnage1)
            print("========================================")
        elif choix == "4":
            print("========================================")
            combat(personnage1, personnage2)
            print("========================================")
        else:
            print(" ====================================== ")
            print("|           Choix invalide !           |")
            print(" ====================================== ")
        
        menu()
        choix = input("Que voulez-vous faire ? ")
        


    
