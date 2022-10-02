#creation fonction

def demander_nom():
    nom_str = ""
    while nom_str == "":
        nom_str = input("Quel est votre nom ?")
    return nom_str



def demander_age():
    age_int = 0
    while age_int == 0:
        age_str = input("Quel est votre age ? ")
        try:
            age_int = int(age_str)
        except ValueError:
            print("ERREUR: Vous devez rentrer un nombre pour l'age")
    return age_int


#Demander le nom
nom = demander_nom()

#Demander Age
age = demander_age()

#Affichage resultat
print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
print("L'an prochain vous aurez " + str(age+1) + " ans")