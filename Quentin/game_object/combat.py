from menu import afficher_menu_combat

def combat(personnage1, personnage2):
    print(f"============== COMBAT : {personnage1.nom} VS {personnage2.nom} ===============")
    while personnage1.points_de_vie > 0 and personnage2.points_de_vie > 0:
        afficher_menu_combat()
        choix = input("Que voulez-vous faire ? ")
        if choix == "1":
            if personnage1.attaquer(personnage2):
                print(f"| {personnage2.nom} est vaincu !")
                personnage1.niveau += 1
                print(f"| {personnage1.nom} passe au niveau {personnage1.niveau}.")
                break
            if personnage2.attaquer(personnage1):
                print(f"| {personnage1.nom} est vaincu ! Game Over.")
                exit()
        elif choix == "2":
            personnage1.utiliser_potion_de_soin()
        elif choix == "3":
            print(f"| {personnage1.nom} fuit le combat.")
            break
        else:
            print("| Choix invalide !")

        print(f"| {personnage1.nom} : {personnage1.points_de_vie} PV")
        print(f"| {personnage2.nom} : {personnage2.points_de_vie} PV")
