#on peut utiliser des variable globales en
#en dehors des fonctions mais il faudra le préciser
# en ajoutant globale devant la varialbe
# ex --> global age

#creation fonction

def demander_nom():
    nom_str = ""
    while nom_str == "":
        nom_str = input("Quel est votre nom ?")
    return nom_str

# utilisation de global avec age
age = 0
def demander_age():
    global age
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
print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
print("L'an prochain vous aurez " + str(age+1) + " ans")