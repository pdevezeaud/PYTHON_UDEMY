import random
#NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN,NOMBRE_MAX)


def poser_question():
    operateur_A = random.randint(NOMBRE_MIN,NOMBRE_MAX)
    operateur_B = random.randint(NOMBRE_MIN,NOMBRE_MAX)
    operande_string = random.randint(0,1)
    if operande_string == 0:
        operande_string = "+"
    else:
        operande_string = "*"
    print(operande_string)

    question = input(f" qu'elle le resultat de {operateur_A} {operande_string} {operateur_B}\n")
    reponse_addition = int(question)
    calcul = operateur_A + operateur_B
    if operande_string == 0:
        calcul = operateur_A + operateur_B
    elif operande_string == 1:
        calcul = operateur_A * operateur_B
    else:
        reponse_addition == calcul
        return True

    return False


NOMBRE_POINTS = 0
NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_QUESTION = 4

for i in range(0, NB_QUESTION):
    print(F"question N° {i + 1} sur {NB_QUESTION}")
    if poser_question() == True:
        print("Réponse correcte")
        NOMBRE_POINTS += 1
    else:
        print("Réponse incorrect")

    print()

print(f"votre note est de {NOMBRE_POINTS}/{NB_QUESTION}")

moyenne_question = int(NB_QUESTION / 2)

if NOMBRE_POINTS == NB_QUESTION:
    print("Excellent")
elif NOMBRE_POINTS == 0:
    print("il va falloir réviser un peu plus")
elif NOMBRE_POINTS > NB_QUESTION:
    print("pas mal")
else:
    print("Tu feras mieux la prochaine fois")



