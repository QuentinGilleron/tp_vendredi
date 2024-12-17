import json
import re
import os
from random import randint
from inventaire import Inventaire

class Personnage:
    def __init__(self, nom, classe, niveau, points_de_vie=100, inventaire=None):
        # Initialisation des attributs du personnage
        self.nom = nom
        self.classe = classe
        self.niveau = niveau
        self.points_de_vie = points_de_vie
        # Si aucun inventaire n'est passé, on initialise un inventaire avec une potion de soin par défaut
        if inventaire is None:
            self.inventaire = Inventaire()
            self.inventaire.ajouter_objet("potion de soin", 3)  # Ajouter 3 potions de soin par défaut
        else:
            self.inventaire = inventaire

    def utiliser_potion_de_soin(self):
        if self.inventaire.utiliser_objet("potion de soin"):
            gain = randint(1, 50)
            self.points_de_vie += gain
            print(f"| {self.nom} utilise une potion et regagne {gain} points de vie.")
        else:
            print("| Pas de potion de soin disponible !")

    def afficher_statistiques(self):
        print("")
        print(f"/ ================== Statistiques {self.nom} ==================")
        print(f"| Nom : {self.nom}")
        print(f"| Classe : {self.classe}")
        print(f"| Niveau : {self.niveau}")
        print(f"| Points de vie : {self.points_de_vie}")
        print("\ ====================================================")
        print("")

    def attaquer(self, cible):
        degats = randint(1, 10) * self.niveau
        cible.points_de_vie -= degats
        print(f"| {self.nom} attaque {cible.nom} et inflige {degats} dégâts.")
        return cible.points_de_vie <= 0

    @staticmethod
    def _get_save_path(fichier):
        """Générer le chemin complet pour sauvegarder/charger."""
        dossier_sauvegarde = "./Quentin/game_object/save/"
        os.makedirs(dossier_sauvegarde, exist_ok=True)  # Créer le dossier si nécessaire
        if not fichier.endswith(".json"):
            fichier += ".json"
        fichier = re.sub(r'[^a-zA-Z0-9._-]', '_', fichier)  # Nettoyage
        return os.path.join(dossier_sauvegarde, fichier)

    def sauvegarder(self, fichier=None):
        """Sauvegarder le personnage dans un fichier JSON."""
        if fichier is None:
            fichier = f"{self.nom}.json"
        chemin_complet = self._get_save_path(fichier)

        try:
            with open(chemin_complet, "w") as f:
                json.dump({
                    "nom": self.nom,
                    "classe": self.classe,
                    "niveau": self.niveau,
                    "points_de_vie": self.points_de_vie,
                    "inventaire": self.inventaire.to_dict()  # Sérialisation de l'inventaire
                }, f, indent=4)
            
            print(f"| Personnage sauvegardé")

        except PermissionError:
            print(f"| Erreur : Permission refusée pour accéder au fichier {chemin_complet}.")

    @staticmethod
    def charger(fichier):
        """Charger un personnage depuis un fichier JSON."""
        chemin_complet = Personnage._get_save_path(fichier)

        try:
            with open(chemin_complet, 'r') as f:
                data = json.load(f)

            # Vérification des clés nécessaires
            required_keys = ['nom', 'classe', 'niveau', 'inventaire']
            for key in required_keys:
                if key not in data:
                    raise KeyError(f"Clé manquante dans le fichier : {key}")

            print("")
            personnage = Personnage(data['nom'], data['classe'], data['niveau'])
            personnage.points_de_vie = data.get('points_de_vie', 100)  # Utiliser 100 comme valeur par défaut si non spécifiée
            personnage.inventaire = Inventaire.from_dict(data['inventaire'])
            return personnage
        
        except FileNotFoundError:
            print(f"| Erreur : Le fichier {chemin_complet} n'existe pas.")
        except PermissionError:
            print(f"| Erreur : Permission refusée pour accéder au fichier {chemin_complet}.")
        except json.JSONDecodeError:
            print(f"| Erreur : Le fichier {chemin_complet} n'est pas un JSON valide.")
        except KeyError as e:
            print(f"| Erreur : Clé manquante dans le fichier : {e}")
        
        return None

    def to_dict(self):
        """Convertir un personnage en dictionnaire pour JSON."""
        return {
            "nom": self.nom,
            "classe": self.classe,
            "niveau": self.niveau,
            "points_de_vie": self.points_de_vie,
            "inventaire": self.inventaire.to_dict()
        }
