class Objet:
    def __init__(self, nom, quantite):
        self.nom = nom
        self.quantite = quantite

    def utiliser(self):
        if self.quantite > 0:
            self.quantite -= 1
            return True
        return False
