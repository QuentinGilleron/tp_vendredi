from menu import afficher_menu_combat, choix_adversaire
from personnage import Personnage
import os

def combat(personnage1):

    choix_adversaire()
    choix = input("Qui voulez-vous affronter ? ")
    if choix == "1":
        personnage2 = Personnage("Rat", "Bestiole", niveau=1)
    elif choix == "2":
        personnage2 = Personnage("Gobelin", "Saloperie", niveau=2)
    elif choix == "3":
        personnage2 = Personnage("Ogre", "Grosse saloperie", niveau=5)
    elif choix == "4":
        personnage2 = Personnage("Titan", "Gros méchant", niveau=8)
    elif choix == "5":
        personnage2 = Personnage("Démons", "Il te nique", niveau=10)
    elif choix == "0":
        return
    else:
        print("| Choix invalide !")
        return
    
    print("")

    print(f"============== COMBAT : {personnage1.nom} VS {personnage2.nom} ===============")
    while personnage1.points_de_vie > 0 and personnage2.points_de_vie > 0:
        afficher_menu_combat()
        choix = input("Que voulez-vous faire ? ")
        print("|")
        print("/ =====================================================")
        print("|")
        if choix == "1":
            if personnage1.attaquer(personnage2):
                print(f"| {personnage2.nom} est vaincu !")
                personnage1.niveau += 1
                print(f"| {personnage1.nom} passe au niveau {personnage1.niveau}.")
                #ajouter une potion de soin
                if personnage2.nom == "Rat":
                    personnage1.inventaire.ajouter_objet("potion de soin", 1)
                elif personnage2.nom == "Gobelin":
                    personnage1.inventaire.ajouter_objet("potion de soin", 2)
                elif personnage2.nom == "Ogre":
                    personnage1.inventaire.ajouter_objet("potion de soin", 3)
                elif personnage2.nom == "Titan":
                    personnage1.inventaire.ajouter_objet("potion de soin", 4)
                elif personnage2.nom == "Démons":
                    personnage1.inventaire.ajouter_objet("potion de soin", 5)
                    personnage1.inventaire.ajouter_objet("Crane de démon", 1)
                #sauvegarder le personnage
                personnage1.sauvegarder()
                break
            if personnage2.attaquer(personnage1):
                print("| ==========================================")
                print("|")
                print(f"| {personnage1.nom} est vaincu ! Game Over.")
                # supprimer le fichier de sauvegarde
                os.remove(Personnage._get_save_path(f"{personnage1.nom}.json"))
                exit()
        elif choix == "2":
            personnage1.afficher_statistiques()
            personnage2.afficher_statistiques()
        elif choix == "3":
            personnage1.utiliser_potion_de_soin()
        elif choix == "0":
            print(f"| {personnage1.nom} fuit le combat.")
            break
        else:
            print("| Choix invalide !")
        print("|")
        print(f"| {personnage1.nom} : {personnage1.points_de_vie} PV")
        print(f"| {personnage2.nom} : {personnage2.points_de_vie} PV")
        print("|")
        print("\ =====================================================")
