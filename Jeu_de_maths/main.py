import random
#NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN,NOMBRE_MAX)

NOMBRE_MIN = 1
NOMBRE_MAX = 10

def poser_question():
    operateur_A = random.randint(NOMBRE_MIN,NOMBRE_MAX)
    operateur_B = random.randint(NOMBRE_MIN,NOMBRE_MAX)
    #addition = operateur_A + operateur_B
    question = input(f" qu'elle le resultat de {operateur_A} + {operateur_B}\n")
    reponse_addition = int(question)

    if reponse_addition == operateur_A + operateur_B:
        print(f"Bonne réponse le resultat est bien {reponse_addition}")
    else:
        print(f"Mauvaise réponse, la bonne réponse est {reponse_addition}")

   
    

poser_question()

