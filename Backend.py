

class Transfo:
    def __init__(self,opé):
        self.opérant=str(opé)
        
    def opérant_show(self):
        return self.opérant
        
    def binaire(self,nombre):
        try:
            if nombre == 0 or nombre == 1:
                return str(nombre)
            else:
                return str(self.binaire(nombre//2)) + str(self.binaire(nombre%2))
        except Exception as t0:
            return f"Erreur : {t0}"

    def hexadecimal(self,nombre):
        try:
            dic={0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
            if nombre < 16 and nombre >= 0:
                return dic[nombre]
            else:
                return str(self.hexadecimal(nombre//16)) + str(dic[nombre%16])
        except Exception as t1:
            return f"Erreur : {t1}"
        
    def deci_color(self, nombre, longueur_idéale=6):
        try:
            if nombre > 16777215:
                return "#FFFFFF"
            else:
                k = str(self.hexadecimal(nombre))
                zeros= longueur_idéale-len(k)
                return "#" + "0"*zeros + k
        except Exception as t2:
            return f"Erreur : {t2}"
                      