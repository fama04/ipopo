# Import d'un module
import pelix
 
# Définition d'une classe
class MaClasse:
   # Constructeur
   def __init__(self):
       self.default = "stanger"
       print("Classe construite")
 
   # Méthode, avec un argument
   def sayHello(self, name):
       if not name:
           # Nom vide ou nul
           return "Hello, " + str(self.default)
       else:
           # Nom valide
           return "Hello, " + str(name)
 
objet = MaClasse()
print(objet.sayHello(""))
print(objet.sayHello("World"))
