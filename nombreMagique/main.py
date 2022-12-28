def demander_nombre(nb_min, nb_max):
    nombre_int = 0
    while nombre_int == 0:
        nombre_str = input(f"quel est le nombre magique (entre {nb_min} et {nb_max})")
        try: 
            nombre_int = int(nombre_str)
        except ValueError:
            print("Désolais la valeur saisie n'est pas un nombre.")
        else:
            if nombre_int < nb_min or nombre_int > nb_max:
                print(f"Erreur: Le nombre doit etre compris entre {NOMBRE_MIN} et {NOMBRE_MAX}")
                nombre_int = 0
    # cast du string en in
    return nombre_int


NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = 5

nombre= 0
while not nombre== NOMBRE_MAGIQUE:
    nombre = demander_nombre(NOMBRE_MIN,NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE:
        print("Bravo vous avez gagné !")
    elif nombre > NOMBRE_MAGIQUE:
        print("Le nombre magique est plus petit !")
    else:
        print("Le nombre magique est plus grand !")
