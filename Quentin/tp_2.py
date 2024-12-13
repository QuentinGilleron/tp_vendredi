import tkinter as tk
from tkinter import messagebox

# Inventaire de Noël
inventaire = [
    {"nom": "Boules de Noël", "quantite": 50, "prix": 1.5},
    {"nom": "Guirlandes", "quantite": 30, "prix": 3.0},
    {"nom": "Sapin de Noël", "quantite": 10, "prix": 25.0},
    {"nom": "Cassoulet de Noël", "quantite": 5, "prix": 8.5}
]

def afficher_inventaire():
    output.delete(1.0, tk.END)
    for produit in inventaire:
        output.insert(tk.END, f"| {produit['nom']} - {produit['quantite']} unités - {produit['prix']} €\n")

def ajouter_produit():
    nom = entry_nom.get()
    quantite = entry_quantite.get()
    prix = entry_prix.get()
    
    if not nom or not quantite or not prix:
        messagebox.showwarning("Erreur", "Veuillez remplir tous les champs.")
        return

    quantite = int(quantite)
    prix = float(prix)

    for produit in inventaire:
        if produit["nom"] == nom:
            produit["quantite"] += quantite
            afficher_inventaire()
            return

    inventaire.append({"nom": nom, "quantite": quantite, "prix": prix})
    afficher_inventaire()

def supprimer_produit():
    nom = entry_nom.get()
    for produit in inventaire:
        if produit["nom"] == nom:
            inventaire.remove(produit)
            afficher_inventaire()
            return
    messagebox.showwarning("Erreur", "Produit introuvable.")

def modifier_quantite():
    nom = entry_nom.get()
    quantite = entry_quantite.get()

    if not nom or not quantite:
        messagebox.showwarning("Erreur", "Veuillez remplir les champs nom et quantite.")
        return

    quantite = int(quantite)

    for produit in inventaire:
        if produit["nom"] == nom:
            produit["quantite"] = quantite
            afficher_inventaire()
            return
    messagebox.showwarning("Erreur", "Produit introuvable.")

def valeur_totale_inventaire():
    total = sum(produit["quantite"] * produit["prix"] for produit in inventaire)
    messagebox.showinfo("Valeur totale", f"Valeur totale de l'inventaire : {total:.2f} €")

# Interface graphique
root = tk.Tk()
root.title("Inventaire de Noël")

# Champs de saisie
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Nom du produit:").grid(row=0, column=0, padx=5, pady=5)
entry_nom = tk.Entry(frame)
entry_nom.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Quantité:").grid(row=1, column=0, padx=5, pady=5)
entry_quantite = tk.Entry(frame)
entry_quantite.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Prix:").grid(row=2, column=0, padx=5, pady=5)
entry_prix = tk.Entry(frame)
entry_prix.grid(row=2, column=1, padx=5, pady=5)

# Zone d'affichage de l'inventaire
output = tk.Text(root, width=50, height=15, wrap=tk.WORD)
output.pack(pady=10)

# Boutons d'action
actions = tk.Frame(root)
actions.pack(pady=10)

tk.Button(actions, text="Afficher l'inventaire", command=afficher_inventaire).grid(row=0, column=0, padx=5, pady=5)
tk.Button(actions, text="Ajouter", command=ajouter_produit).grid(row=0, column=1, padx=5, pady=5)
tk.Button(actions, text="Supprimer", command=supprimer_produit).grid(row=0, column=2, padx=5, pady=5)
tk.Button(actions, text="Modifier Quantité", command=modifier_quantite).grid(row=0, column=3, padx=5, pady=5)
tk.Button(actions, text="Valeur Totale", command=valeur_totale_inventaire).grid(row=0, column=4, padx=5, pady=5)

# Initialiser l'affichage de l'inventaire
afficher_inventaire()

root.mainloop()
