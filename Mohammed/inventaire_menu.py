# creation de la fonction   stocker_inventaire() --> stocke les produits dans le stock  
def stocker_inventaire():
    return [
        {"nom": "Boules de Noël", "quantite": 50, "prix": 1.5},
        {"nom": "Guirlandes", "quantite": 30, "prix": 3.0},
        {"nom": "Sapin de Noël", "quantite": 10, "prix": 25.0}
    ]

# creation de la methode afficher_inventaire(inventaire) --> affiche les produits du stock  
def afficher_inventaire(inventaire):
    
    for produit in inventaire:
        #print(f"Nom: {produit['nom']}, Quantité: {produit['quantite']}, Prix: {produit['prix']} €")
        for k,v  in produit.items(): 
            print(f'{k} : {v}')  


def ajouter_produit(inventaire):
    nom = input("Nom du produit : ")
    quantite = int(input("Quantité : "))
    prix = float(input("Prix : "))

    for produit in inventaire:
        if produit["nom"] == nom:
            produit["quantite"] += quantite
            print(f"La quantité du produit '{nom}' a été mise à jour.")
            return inventaire.append({"nom": nom, "quantite": quantite, "prix": prix})
        
        print(f"Le produit '{nom}' a été ajouté.")
         
            
     

def supprimer_produit(inventaire):
    nom = input("Nom du produit à supprimer : ")
    for produit in inventaire:
        if produit["nom"] == nom:
            inventaire.remove(produit)
            print(f"Le produit '{nom}' a été supprimé.")
            return

    print(f"Erreur : Le produit '{nom}' n'existe pas dans l'inventaire.")

def modifier_quantite(inventaire):
    nom = input("Nom du produit : ")
    nouvelle_quantite = int(input("Nouvelle quantité : "))

    for produit in inventaire:
        if produit["nom"] == nom:
            produit["quantite"] = nouvelle_quantite
            print(f"La quantité du produit '{nom}' a été mise à jour.")
            return

    print(f"Erreur : Le produit '{nom}' n'existe pas dans l'inventaire.")

def rechercher_produit(inventaire):
    nom = input("Nom du produit à rechercher : ")

    for produit in inventaire:
        if produit["nom"] == nom:
            print(f"Produit trouvé : Nom: {produit['nom']}, Quantité: {produit['quantite']}, Prix: {produit['prix']}")
            return

    print(f"Erreur : Le produit '{nom}' n'existe pas dans l'inventaire.")

def valeur_totale_inventaire(inventaire):
    valeur_totale = sum(produit["quantite"] * produit["prix"] for produit in inventaire)
    print(f"La valeur totale de l'inventaire est de {valeur_totale}")

def menu():
    inventaire = stocker_inventaire()

    while True:
        print("\n--- Menu ---")
        print("1. Afficher l'inventaire")
        print("2. Ajouter un produit")
        print("3. Supprimer un produit")
        print("4. Modifier la quantité d'un produit")
        print("5. Rechercher un produit")
        print("6. Calculer la valeur totale de l'inventaire")
        print("7. Quitter le programme")

        choix = input("Choisissez une option : ")

        if choix == "1":
            afficher_inventaire(inventaire)
        elif choix == "2":
            ajouter_produit(inventaire)
        elif choix == "3":
            supprimer_produit(inventaire)
        elif choix == "4":
            modifier_quantite(inventaire)
        elif choix == "5":
            rechercher_produit(inventaire)
        elif choix == "6":
            valeur_totale_inventaire(inventaire)
        elif choix == "7":
            print("Fin du programme --> quitter")
            break
        else:
            print("Option invalide, veuillez réessayer.")

menu()
if __name__ == '__main__':  
    menu()
