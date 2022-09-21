nom = input("quel est votre nom ?")


age_prochain = 0

while age_prochain == 0:
    age = input("quel est votre age ?")

try:
    age_prochain = int(age) + 1

except ValueError:
    print("Erreur: vous devez rentrer un nombre pour l'age")
else:
    print("vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
    print("L'an prochain vous aurez " + str(age_prochain) + " ans")
