from objet import Objet

class Inventaire:
    def __init__(self, objets=None):
        # Par défaut, initialise avec 3 potions de soin si aucun objet n'est fourni
        self.objets = objets if objets else [{"nom": "potion de soin", "quantité": 3}]

    def ajouter_objet(self, nom_objet, quantité):
        """Ajoute un objet à l'inventaire."""
        for objet in self.objets:
            if objet["nom"] == nom_objet:
                objet["quantité"] += quantité
                return
        self.objets.append({"nom": nom_objet, "quantité": quantité})
    
    def retirer_objet(self, nom_objet, quantité):
        """Retire une quantité d'un objet de l'inventaire."""
        for objet in self.objets:
            if objet["nom"] == nom_objet:
                objet["quantité"] -= quantité
                if objet["quantité"] <= 0:
                    self.objets.remove(objet)
                return

    def utiliser_objet(self, nom):
        if nom in self.objets and self.objets[nom].utiliser():
            if self.objets[nom].quantite == 0:
                del self.objets[nom]
            return True
        return False

    def afficher(self):
        print("")
        print("/ ============= Inventaire =================")
        if not self.objets:
            print("| Votre inventaire est vide.")
        else:
            for objet in self.objets:
                print(f"| - {objet['nom']} (Quantité : {objet['quantité']})")
        print("\ ====================================")
        print("")

    def to_dict(self):
        """Convertir l'inventaire en un dictionnaire JSON-serializable."""
        return {"objets": self.objets}

    @staticmethod
    def from_dict(data):
        """Créer un inventaire à partir d'un dictionnaire."""
        return Inventaire(objets=data.get("objets", []))
