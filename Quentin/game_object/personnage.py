import json
import re
import os
from random import randint
from inventaire import Inventaire

class Personnage:
    def __init__(self, nom, classe, niveau, points_de_vie=100, inventaire=None):
        self.nom = nom
        self.classe = classe
        self.niveau = niveau
        if nom == "Rat":
            self.points_de_vie = 40
        elif nom == "Gobelin":
            self.points_de_vie = 80
        elif nom == "Ogre":
            self.points_de_vie = 160
        elif nom == "Titan":
            self.points_de_vie = 320
        elif nom == "Démons":
            self.points_de_vie = 500
        else:
            self.points_de_vie = points_de_vie
        if inventaire is None:
            self.inventaire = Inventaire()
            self.inventaire.ajouter_objet("potion de soin", 3)  # Ajouter 3 potions par défaut
        else:
            self.inventaire = inventaire

    def utiliser_potion_de_soin(self):
        if self.inventaire.utiliser_objet("potion de soin"):
            gain = randint(10, 50)
            self.points_de_vie += gain
            print(f"| {self.nom} utilise une potion de soin et récupère {gain} points de vie.")
        else:
            print("| Vous n'avez pas de potion de soin.")

    def afficher_statistiques(self):
        print("")
        print(f"/ ========== Statistiques {self.nom} ============")
        print(f"| Nom : {self.nom}")
        print(f"| Classe : {self.classe}")
        print(f"| Niveau : {self.niveau}")
        print(f"| Points de vie : {self.points_de_vie}")
        print("\ ==========================================")
        print("")

    def attaquer(self, cible):
        degats = randint(1, 10) * self.niveau
        cible.points_de_vie -= degats
        print(f"| {self.nom} attaque {cible.nom} et inflige {degats} dégâts.")
        return cible.points_de_vie <= 0

    @staticmethod
    def _get_save_path(fichier):
        dossier_sauvegarde = "./Quentin/game_object/save/"
        os.makedirs(dossier_sauvegarde, exist_ok=True)
        if not fichier.endswith(".json"):
            fichier += ".json"
        fichier = re.sub(r'[^a-zA-Z0-9._-]', '_', fichier)
        return os.path.join(dossier_sauvegarde, fichier)

    def sauvegarder(self, fichier=None):
        if fichier is None:
            fichier = f"{self.nom}.json"
        chemin_complet = self._get_save_path(fichier)

        try:
            with open(chemin_complet, "w") as f:
                json.dump(self.to_dict(), f, indent=4)
            print(f"| Personnage sauvegardé.")
        except PermissionError:
            print(f"| Erreur : Impossible d'écrire dans {chemin_complet}.")

    @staticmethod
    def charger(fichier):
        chemin_complet = Personnage._get_save_path(fichier)

        try:
            with open(chemin_complet, 'r') as f:
                data = json.load(f)

            personnage = Personnage(data['nom'], data['classe'], data['niveau'])
            personnage.points_de_vie = data.get('points_de_vie', 100)
            personnage.inventaire = Inventaire.from_dict(data['inventaire'])
            return personnage
        except FileNotFoundError:
            print(f"| Erreur : Le fichier {fichier} est introuvable.")
        except json.JSONDecodeError:
            print("| Erreur : Le fichier n'est pas valide.")
        return None

    def to_dict(self):
        return {
            "nom": self.nom,
            "classe": self.classe,
            "niveau": self.niveau,
            "points_de_vie": self.points_de_vie,
            "inventaire": self.inventaire.to_dict()
        }
