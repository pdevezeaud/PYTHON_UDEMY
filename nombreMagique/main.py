def demander_nombre(nb_min, nb_max):
    nombre_str = input(f"quel est le nombre magique (entre {nb_min} et {nb_max})") 
    # cast du string en in
    nombre_int = int(nombre_str)
    return nombre_int


NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = 5

nombre = demander_nombre(NOMBRE_MIN,NOMBRE_MAX)

if nombre 