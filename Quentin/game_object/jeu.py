import os
from personnage import Personnage
from combat import combat
from menu import choix_personnage, chargement, afficher_menu_principal

def afficher_sauvegardes():
    """Affiche les sauvegardes disponibles dans le dossier save."""
    chemin_sauvegardes = "./Quentin/game_object/save/"
    if not os.path.exists(chemin_sauvegardes):
        print("Aucune sauvegarde disponible. Le dossier n'existe pas.")
        return []

    fichiers = os.listdir(chemin_sauvegardes)
    fichiers_json = [f for f in fichiers if f.endswith(".json")]

    if fichiers_json:
        print("======= Chargement d'une sauvegarde existante =======")
        print("Sauvegardes disponibles :")
        for i, fichier in enumerate(fichiers_json, 1):
            print("")
            print(f"| {i}. {fichier[:-5]}")
        print("")
    else:
        print("Aucune sauvegarde disponible.")

    return fichiers_json

def main():
    print("======= Bienvenue dans le jeu de combat ! ========")
    print("")
    
    while True:  # Boucle principale pour afficher le menu tant qu'on ne sort pas
        choix_personnage()
        choix = input("Votre choix : ")

        if choix == "1":
            nom = input("Quel est votre nom ? ")
            classe = input("Quelle est votre classe ? ")
            joueur = Personnage(nom, classe, niveau=1)
            joueur.sauvegarder()
            chargement()
            print(f"| Personnage {joueur.nom} créé et sauvegardé.")
            break  # Quitter la boucle après la création et la sauvegarde du personnage

        elif choix == "2":
            fichiers_disponibles = afficher_sauvegardes()  # Afficher les fichiers de sauvegarde disponibles

            if fichiers_disponibles:
                while True:  # Boucle pour demander un fichier jusqu'à ce qu'un fichier valide soit trouvé
                    fichier = input("Entrez le nom du joueur (ou le numéro) : ")
                    # ajouter l'extension .json si elle n'est pas déjà présente
                    
                    
                    if fichier.isdigit():
                        index = int(fichier) - 1  # Convertir l'input en index si c'est un numéro
                        if 0 <= index < len(fichiers_disponibles):
                            fichier = fichiers_disponibles[index]
                            break  # Sortir de la boucle si un fichier valide est choisi
                        else:
                            print("Numéro invalide.")
                    else:
                        # Si ce n'est pas un numéro, on tente d'entrer directement le nom du fichier
                        if fichier in fichiers_disponibles:
                            break  # Sortir de la boucle si le fichier est valide
                        else:
                            print("| Fichier non trouvé. Veuillez réessayer.")


                    if not fichier.endswith(".json"):
                        fichier += ".json"

                # Charger le personnage depuis le fichier choisi
                try:
                    joueur = Personnage.charger(fichier)
                    if joueur:
                        chargement()
                        print("")
                        print("  ========================================")
                        print(f"| Bon retour parmi nous {joueur.nom} !")
                        print("  ========================================")
                        print("")
                        break  # Quitter la boucle une fois le joueur chargé
                    else:
                        print("| Erreur de chargement du personnage. Retour au menu principal.")
                except FileNotFoundError:
                    print("| Erreur : Fichier introuvable. Veuillez réessayer.")
            else:
                print("Aucune sauvegarde disponible. Retour au menu principal.")
                break  # Retour au menu principal si aucune sauvegarde n'est trouvée
        elif choix == "3":
            print("")
            print("  ========================================")
            print("| Merci d'avoir joué !")
            print("  ========================================")
            exit()
        else:
            print("")
            print("  ========================================")
            print("| Choix invalide.")
            print("  ========================================")
            print("")


    ennemi = Personnage("Ennemi", "Guerrier", niveau=1)

    while True:
        afficher_menu_principal()
        choix = input("Que voulez-vous faire ? ")

        if choix == "1":
            joueur.afficher_statistiques()
        elif choix == "2":
            joueur.inventaire.afficher()
        elif choix == "3":
            joueur.utiliser_potion_de_soin()
        elif choix == "4":
            combat(joueur, ennemi)
        elif choix == "5":
            print("  ========================================")
            joueur.sauvegarder()
            print("| Merci d'avoir joué !")
            print("  ========================================")
            break
        else:
            print("Choix invalide !")
    
if __name__ == "__main__":
    main()
