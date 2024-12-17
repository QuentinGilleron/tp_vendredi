from time import sleep
import sys
import time

def afficher_menu_principal():
    print("  ================== Menu ==================  ")
    print("| 1. Statistiques                          |")
    print("| 2. Inventaire                            |")
    print("| 3. Utiliser une potion de soin           |")
    print("| 4. Combat                                |")
    print("| 5. Quitter                               |")
    print("  ========================================  ")

def afficher_menu_combat():
    print("  ================== Menu ==================  ")
    print("| 1. Attaquer                                |")
    print("| 2. Stat de combat                          |")
    print("| 3. Utiliser une potion de soin             |")
    print("| 0. Fuir                                    |")
    print("  ==========================================  ")

def espace():
    for _ in range(3):
        print()

def choix_adversaire():
    print("")
    print("  ================== Qui affronter ? ==================  ")
    print("| 1. Rat (Facile)                                       |")
    print("| 2. Gobelin (Moyen)                                    |")
    print("| 3. Ogre (Difficile)                                   |")
    print("| 4. Titan (Très difficile)                             |")
    print("| 5. Démons (Boss final)                                |")
    print("| 0. Retourner au menu principal                        |")
    print("  =====================================================  ")
    print("")

def chargement():

    # Durée totale du chargement (en secondes)
    duree_chargement = 2
    # Nombre d'étapes pour simuler la barre de chargement
    n = 50  # Plus le nombre est grand, plus la barre se met à jour rapidement
    
    # Boucle pour simuler la progression de la barre
    for i in range(n + 1):
        # Calculer le pourcentage de progression
        progression = (i / n) * 100
        
        # Calculer le nombre d'espaces à remplir pour simuler la barre
        remplissage = int((i / n) * 50)
        barre = f"[{'#' * remplissage}{'.' * (50 - remplissage)}] {progression:.2f}%"
        
        # Effacer la ligne précédente
        sys.stdout.write('\r' + barre)
        sys.stdout.flush()
        
        # Attendre une fraction de seconde pour simuler le temps de chargement
        time.sleep(duree_chargement / n)
    
    print()


def choix_personnage():
    print("  ================== Menu ==================  ")
    print("| 1. Créer un nouveau personnage           |")
    print("| 2. Charger un personnage existant        |")
    print("| 3. Quitter                               |")
    print("  ========================================  ")
    