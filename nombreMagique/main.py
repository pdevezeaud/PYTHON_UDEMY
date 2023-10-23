import random
# Jeu de devinette

def demander_nombre(nb_min, nb_max):
    nombre_int = 0
    while nombre_int == 0:
        nombre_str = input(f"quel est le nombre magique (entre {nb_min} et {nb_max})")
        try: 
            nombre_int = int(nombre_str)
        except ValueError:
            print("ERREUR: Vous devez rentrer un nombre. Réessayez")
         
            
        else:
            if nombre_int < nb_min or nombre_int > nb_max:
                print(f"Erreur: Le nombre doit etre compris entre {NOMBRE_MIN} et {NOMBRE_MAX}")
                nombre_int = 0
    # cast du string en in
    return nombre_int


NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN,NOMBRE_MAX)
NB_VIES = 4
vies = NB_VIES

nombre= 0
while not nombre == NOMBRE_MAGIQUE and vies > 0:
    print(f"Il vous reste {vies}")
    nombre = demander_nombre(NOMBRE_MIN,NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE:
        print("Bravo vous avez gagné !")
    elif nombre > NOMBRE_MAGIQUE:
        print("Le nombre magique est plus petit !")
        NB_VIES -= 1
    else:
        print("Le nombre magique est plus grand !")
        NB_VIES -= 1

if vies == 0:
    print(f"Vous avez perdu, le nombre magique est {NOMBRE_MAGIQUE} ") 
