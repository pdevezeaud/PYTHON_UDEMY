

#creation fonction

#afficher_information_personne
# Parametres: nom, age

def afficher_information_personne(nom,age):
    print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
    print("L'an prochain vous aurez " + str(age+1) + " ans")



def demander_nom():
    nom_str = ""
    while nom_str == "":
        nom_str = input("Quel est votre nom ?")
    return nom_str


def demander_age():
    age = 0
    while age == 0:
        age_str = input("Quel est votre age ? ")
        try:
            age = int(age_str)
        except ValueError:
            print("ERREUR: Vous devez rentrer un nombre pour l'age")
    return age


#Demander le nom
nom = demander_nom()

#Demander Ager
age = demander_age()

#Affichage resultat
afficher_information_personne(nom,age)
print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
print("L'an prochain vous aurez " + str(age+1) + " ans")
