# Inventaire de Noël
inventaire = [
    {"nom": "Boules de Noël", "quantite": 50, "prix": 1.5},
    {"nom": "Guirlandes", "quantite": 30, "prix": 3.0},
    {"nom": "Sapin de Noël", "quantite": 10, "prix": 25.0},
    {"nom": "Cassoulet de Noël", "quantite": 5, "prix": 8.5}
]

# Affichage de l'inventaire
def afficher_inventaire(inventaire):
    for produit in inventaire:
        print(f"| {produit['nom']} - {produit['quantite']} unités - {produit['prix']} €")


# Ajout d'un produit
def ajouter_produit(inventaire, nom, quantite, prix):
    for produit in inventaire:
        if produit["nom"] == nom:
            produit["quantite"] += quantite
            return inventaire
    inventaire.append({"nom": nom, "quantite": quantite, "prix": prix})
    return inventaire

# Suppression d'un produit
def supprimer_produit(inventaire, nom):
    for produit in inventaire:
        if produit["nom"] == nom:
            inventaire.remove(produit)
            print(f"Le produit {nom} a été supprimé.")
            return inventaire
    print("Le produit n'existe pas.")
    return inventaire


# Modification de la quantité d'un produit
def modifier_quantite(inventaire, nom, quantite):
    for produit in inventaire:
        if produit["nom"] == nom:
            produit["quantite"] = quantite
            return inventaire
    print("Le produit n'existe pas.")
    return inventaire

# Recherche d'un produit
def rechercher_produit(inventaire, nom):
    for produit in inventaire:
        if produit["nom"] == nom:
            print(f"| {produit['nom']} - {produit['quantite']} unités - {produit['prix']} €")
            return
    print("Le produit n'existe pas.")

# Calcul de la valeur totale de l'inventaire
def valeur_totale_inventaire(inventaire):
    total = 0
    for produit in inventaire:
        total += produit["quantite"] * produit["prix"]
    return total


if __name__ == "__main__":
    while True:
        print(" ================ Menu principal ================= ")
        print("| 1. Afficher l’inventaire.                       |")
        print("| 2. Ajouter un produit.                          |")
        print("| 3. Supprimer un produit.                        |")
        print("| 4. Modifier la quantité d’un produit.           |")
        print("| 5. Rechercher un produit.                       |")
        print("| 6. Calculer la valeur totale de l’inventaire.   |")
        print("| 7. Quitter le programme.                        |")
        print(" ================================================= ")
        print("")
        choix = input(" Choix : ")
        print("")
        if choix == "1":
            print(" ============== Inventaire ===============")
            afficher_inventaire(inventaire)
            print(" =========================================")
        elif choix == "2":
            print(" ============== Ajouter un produit ===============")
            nom = input("Nom du produit : ")
            quantite = int(input("Quantité : "))
            prix = float(input("Prix : "))
            inventaire = ajouter_produit(inventaire, nom, quantite, prix)
            print(" ================================================")
        elif choix == "3":
            print(" ============== Supprimer un produit ===============")
            afficher_inventaire(inventaire)
            print("")
            nom = input("Nom du produit : ")
            inventaire = supprimer_produit(inventaire, nom)
            print(" ==================================================")
        elif choix == "4":
            print(" ============== Modifier la quantité d'un produit ===============")
            afficher_inventaire(inventaire)
            print("")
            nom = input("Nom du produit : ")
            quantite = int(input("Nouvelle quantité : "))
            inventaire = modifier_quantite(inventaire, nom, quantite)
            print(" ===============================================================")
        elif choix == "5":
            print(" ============== Rechercher un produit ===============")
            nom = input("Nom du produit : ")
            rechercher_produit(inventaire, nom)
            print(" ===================================================")
        elif choix == "6":
            print(" ============== Valeur totale de l'inventaire ===============")
            print(f"Valeur totale : {valeur_totale_inventaire(inventaire)} €")
            print(" =============================================================")
        elif choix == "7":
            break
        else:
            print("================================================")
            print("Choix invalide.")
            print("================================================")
        print("")