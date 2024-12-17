class Inventaire:
    def __init__(self, objets=None):
        self.objets = objets if objets else [{"nom": "potion de soin", "quantité": 3}]

    def ajouter_objet(self, nom_objet, quantité):
        for objet in self.objets:
            if objet["nom"] == nom_objet:
                objet["quantité"] += quantité
                return
        self.objets.append({"nom": nom_objet, "quantité": quantité})

    def retirer_objet(self, nom_objet, quantité):
        for objet in self.objets:
            if objet["nom"] == nom_objet:
                objet["quantité"] -= quantité
                if objet["quantité"] <= 0:
                    self.objets.remove(objet)
                return

    def utiliser_objet(self, nom):
        for objet in self.objets:
            if objet["nom"] == nom and objet["quantité"] > 0:
                objet["quantité"] -= 1
                if objet["quantité"] <= 0:
                    self.objets.remove(objet)
                return True
        return False

    def afficher(self):
        print("")
        print("/ =========== Inventaire ============")
        if not self.objets:
            print("| Votre inventaire est vide.")
        else:
            for objet in self.objets:
                print(f"| - {objet['nom']} (Quantité : {objet['quantité']})")
        print("\ ===================================")
        print("")

    def to_dict(self):
        return {"objets": self.objets}

    @staticmethod
    def from_dict(data):
        return Inventaire(objets=data.get("objets", []))
