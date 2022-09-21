nom = input("quel est votre nom ?")
age = input("quel est votre age ?")

try:
    age_prochain = int(age) + 1

except ValueError:
    print("Erreur: vous devez rentrer un nombre pour l'age")
else:
    print("vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
