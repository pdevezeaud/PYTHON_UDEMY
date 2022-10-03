"""Premier programme
Formation Python
apprendre la programmation"""

def afficher_informations_personne(nom, age):
    print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
    print("L'an prochain vous aurez " + str(age+1) + " ans")

    # == egal
    # < inférieur
    # <= inférieur ou égal
    # > supérieur
    # >= supérieur ou égal
    # True / False (Boolean=)

    # 17 ans -> vous etes presque majeur
    # 18 ans -> Tout juste majeur : felicitation

    # elif sinon si    
    #condition = age >= 18   # ou ajouter seulement age >= 18:

# si age est superieur à 60 ---> senior
# si age est inferieur à 10 ---> enfants

# simplification : 12 <= age < 18

#Adolescent si age > 12 et age < 18
#bébé si age == 1 ou age == 2

    
    if age == 17:
        print("Vous etes presque majeur")
    elif age >= 12 and age < 18:
        print("Vous etes adolescent")
    elif age == 1 or age == 2:
        print("Vous êtes un bébé !!")
    elif age == 18:
        print("Tous juste majeur : Felecitation")
    elif age < 10:
        print("Vous etes un enfant")
    elif age > 60:
        print("Vous êtes un senior")
    elif age > 18:
        print("Vous êtes majeur")
    else:
        print("vous êtes mineur")

def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? ")
    return reponse_nom

def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + " quel est votre age ? ")
        try:
            age_int = int(age_str)
        except ValueError:
            print("ERREUR: Vous devez rentrer un nombre pour l'age")
    return age_int

#-----------------------------------------------------------------------------
            
# demander le nom
# nom1 = demander_nom()
# nom2 = demander_nom()

# # demander l'age
# age1 = demander_age(nom1)
# age2 = demander_age(nom2)

# # Afficher les résultats
# afficher_informations_personne(nom1, age1)
# afficher_informations_personne(nom2, age2)

#constante
NB_PERSONNE = 1

for i in range(1,NB_PERSONNE):
    nom = "personne" + str(i+1)
    age = demander_age(nom)
    afficher_informations_personne(nom, age)
